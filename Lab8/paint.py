import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

#Color palette
white = (255, 255, 255)
purple = (128, 0, 128)
orange = (255, 140, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

radius = 10
mode = (red)  # Default color is red
drawing_mode = 'line'  # To select the drawing mode: line, circle or rectangle. Default mode is line
strokes = []  # List of strokes, each stroke is a list of points for lines
current_stroke = []  # Current stroke being drawn
rects = []  # List of rectangles to draw
circles = []  # List of circles to draw
start_pos = None  # Starting position for drawing shapes
colors = [(red), (orange), (yellow), (green), (blue), (purple), (white)] # List of colors to make it easier
font = pygame.font.Font(None, 40) 

done = False

# Function to draw lines
def draw_rounded_line(screen, start, end, color, radius):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(screen, color, (x, y), radius)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the display
            done = True
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r:
                drawing_mode = 'rect'  # Switch to rectangle drawing mode
            elif event.key == pygame.K_c:
                drawing_mode = 'circle'  # Switch to circle drawing mode

            #erasing
            elif event.key == pygame.K_e: 
                strokes = []
                rects = [] 
                circles = []
                squares = []
                rights = []
                triangles = []
                rhombuses = []

            else:
                drawing_mode = 'line'  # Default to line drawing mode
                # Determine which color is picked
                for i, color in enumerate(colors, start=1):
                    if event.key == getattr(pygame, f'K_{i}'):
                        mode = color # 1 is red, 2 is orange, ... 7 is white (eraser)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                start_pos = event.pos  # Store start position for drawing shapes
                if drawing_mode == 'line':
                    if event.pos[1] < 600:  # Restrict y-coordinate for lines
                        current_stroke.append((event.pos, mode, radius))
        if event.type == pygame.MOUSEMOTION and drawing_mode == 'line':
            if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                if event.pos[1] < 590:  # Restrict y-coordinate for lines
                    current_stroke.append((event.pos, mode, radius))

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left button released
                if drawing_mode == 'line' and current_stroke:
                    strokes.append(current_stroke)
                    current_stroke = []
                elif drawing_mode == 'rect':
                    end_pos = event.pos
                    rects.append((start_pos, end_pos, mode))  # Store rectangle data
                elif drawing_mode == 'circle':
                    end_pos = event.pos
                    circles.append((start_pos, end_pos, mode))  # Store circle data
                start_pos = None  # Reset start position

    screen.fill((white))

    #Draw lines
    for stroke in strokes + [current_stroke]:
        for i in range(len(stroke) - 1):
            start_point, start_color, start_radius = stroke[i]
            end_point, end_color, end_radius = stroke[i + 1]
            draw_rounded_line(screen, start_point, end_point, start_color, start_radius) 
    # Draw rectangles
    for rect in rects:
        start, end, color = rect
        pygame.draw.rect(screen, color, pygame.Rect(start, (end[0] - start[0], end[1] - start[1])))

    # Draw circles
    for circle in circles:
        start, end, color = circle
        radius = max(abs(end[0] - start[0]), abs(end[1] - start[1])) // 2
        center = start[0] + (end[0] - start[0]) // 2, start[1] + (end[1] - start[1]) // 2
        pygame.draw.circle(screen, color, center, radius)
    # Color menu
    for i, color in enumerate(colors, start=1):
        pygame.draw.rect(screen, color, (700 - 70, (i - 1) * 70, 100, 100))
        text = font.render(f"{i}", True, (0, 0, 0))
        screen.blit(text, (660, ((i - 1) * 70)))
    # Guide to keybinds 
    eraser = pygame.transform.scale(pygame.image.load("eraser.webp"), (40, 40))
    screen.blit(eraser, (645, 450))
    text = font.render(f"Key R to rect", True, (0, 0, 0))
    screen.blit(text, (0, 640))
    text = font.render(f"Key C to circle", True, (0, 0, 0))
    screen.blit(text, (0, 670))
    text = font.render(f"Key E to erase all", True, (0, 0, 0))
    screen.blit(text, (350, 670))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
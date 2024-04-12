import pygame
import time
import random

# Initialize speed
snake_speed = 10

# Window size & font
window_x, window_y = 720, 480
font = 'Times New Roman'

# Initialize pygame
pygame.init()

# Display & caption 
pygame.display.set_caption('Snake game')
game_window = pygame.display.set_mode((window_x, window_y))

# Frames per sec
fps = pygame.time.Clock()

# Color palette
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 204)
pink = (255, 51, 255)

# Creating a snake
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# Starting position of a snake
snake_position = [100, 50]

# Random positions of a
fruit_positions = [[random.randrange(1, (window_x//10)) * 10,
                    random.randrange(1, (window_y//10)) * 10]] # We are divide and multiply to 10 to food to not get out of display

# Setting direction
direction = 'RIGHT'
change_to = direction

score = 0 # Initialize score
level = 1  # Initialize level

# Print score & level
def show_score_and_level(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}  Level: {level}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Initialize "Game over" window
def game_over():
    my_font = pygame.font.SysFont(font, 50)
    game_over_surface = my_font.render(
        'Your Score: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/3)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
# Main function
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # To close display
            pygame.quit()
            # To choose direction using keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
# To make the snake move to 10 edinic in selected direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
# To snake constantly move 
    snake_body.insert(0, list(snake_position))

    fruit_eaten = False
# Itteration to make the food constantly appear
    for i, fruit_position in enumerate(fruit_positions):
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 20 # One food is 20 points
            fruit_eaten = True
            del fruit_positions[i]
            break

    if not fruit_eaten:
        snake_body.pop()
    else:
        fruit_positions.append([random.randrange(1, (window_x//10)) * 10,
                                    random.randrange(1, (window_y//10)) * 10])
# Display color
    game_window.fill(blue)
# Creating snake
    for pos in snake_body:
        pygame.draw.rect(game_window, pink,
                         pygame.Rect(pos[0], pos[1], 10, 10))
# Creatin food
    for fruit_position in fruit_positions:
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

# Why does game over?
    if snake_position[0] < 0 or snake_position[0] > window_x - 10: # If snake crashed left or right
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10: # If snake crashed up or down
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

# Show level & score
    show_score_and_level(1, white, 'times new roman', 20)

    if score >= level * 30:  # Increase level every 30 points
        level += 1
        snake_speed += 3  # Increase speed when level goes up

    pygame.display.update()

    fps.tick(snake_speed)
    


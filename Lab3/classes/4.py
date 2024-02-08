import math
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def show(self):
    print(self.x, self.y)

  def move(self, x2, y2):
    self.x = x2
    self.y = y2

  def dist(self, other):
    return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
  
point1 = Point(2, 4)
point2 = Point(5, 8)
point1.show() 
point2.show()  

print(point1.dist(point2))  

point1.move(2, -1)
point1.show()  
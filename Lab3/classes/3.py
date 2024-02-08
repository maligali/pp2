class Shape:
    def area(self):
        return 0
    
class Rectianlge(Shape):
    def __init__(self, length, wildth):
        self.length = length
        self.wildth = wildth
    def area(self):
        return self.length*self.wildth

n = int(input())
k = int(input())
rect = Rectianlge(n, k)
print(rect.area())
from copy import copy
from jupyturtle import make_turtle, jumpto, moveto

class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def translated(self, dx=0, dy=0):
        point = copy(self)
        point.translate(dx, dy)
        return point
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'    
    
    def draw(self):
        jumpto(self.p1.x, self.p1.y)
        moveto(self.p2.x, self.p2.y)

    def __eq__(self, other):
        return (self.p1 == other.p1) and (self.p2 == other.p2)
    
class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self):
        return f'Rectangle({self.width}, {self.height}, {self.corner})'
    
origin = Point(0, 0)

x_axis = Line(origin, Point(300, 0))
y_axis = Line(origin, Point(0, 300))

make_turtle()
x_axis.draw()
y_axis.draw()
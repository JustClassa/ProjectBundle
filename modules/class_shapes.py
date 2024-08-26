from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, leg1, leg2, hyp):
        self.leg1 = leg1
        self.leg2 = leg2
        self.hyp = hyp

    @property
    def area(self):
        return (self.leg1 * self.leg2) / 2
    
    @property
    def perimeter(self):
        return self.leg1 + self.leg2 + self.hyp

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def internal_angles(self):
        return 90

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.pi * (self.radius ** 2)
    
    @property
    def perimeter(self):
        return 2 * self.pi * self.radius
    
if __name__ == "__main__":
    rectangle = Rectangle(3.5, 4.0)
    circle = Circle(3.0)
    triangle = Triangle(12, 9, 4)

    print(triangle.area)
    print(triangle.perimeter)
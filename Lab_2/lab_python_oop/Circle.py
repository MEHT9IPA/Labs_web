from lab_python_oop.AF import Figure
from math import pi

class Circle(Figure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def Area(self):
        return pi*self.radius*self.radius

    def __str__(self):
        return f"{self.color} круг с радиусом {self.radius}\nПлощадь = {self.Area()}"
from lab_python_oop.AF import Figure

class Rectangle(Figure):
    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color

    def Area(self):
        return self.width*self.height

    def __str__(self):
        return f"{self.color} прямоугольник с высотой {self.height} и шириной {self.width}\nПлощадь = {self.Area()}"
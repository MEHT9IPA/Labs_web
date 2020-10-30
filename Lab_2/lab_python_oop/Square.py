from lab_python_oop.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        self.height = side
        self.width = side
        self.color = color

    def __str__(self):
        return f"{self.color} квадрат со стороной {self.height}\nПлощадь = {self.Area()}"
from lab_python_oop import Circle, Rectangle, Square, Color
from lab_python_oop.AF import Figure
from datetime import datetime

def main():
    BLUE = Color.Color("Синий")
    GREEN = Color.Color("Зелёный")
    RED = Color.Color("Красный")

    r = Rectangle.Rectangle(2,2,BLUE)
    print(f"{r}")
    print("="*60)
    c = Circle.Circle(2, GREEN)
    print(f"{c}")
    print("="*60)
    s = Square.Square(2,RED)
    print(f"{s}")
    print("="*60)

    print(f"Текущая дата: {datetime.now()}") #получение текущего времени

if __name__ == "__main__":
    main()
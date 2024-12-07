import math

class ShapeError(Exception):
    # Кастомное исключение для ошибок работы с фигурами.
    pass

class Triangle:
    def __init__(self, identifier: str, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
        self.identifier = identifier
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
    
    def __str__(self):
        return f"Треугольник {self.identifier}: A=({self.x1}, {self.y1}), B=({self.x2}, {self.y2}), C=({self.x3}, {self.y3})"

    # Перемещение треугольника на плоскости
    def move(self, dx: float, dy: float):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
        self.x3 += dx
        self.y3 += dy

    # Вычисление площади по формуле Герона
    def area(self):
        side_a = math.dist((self.x1, self.y1), (self.x2, self.y2))
        side_b = math.dist((self.x2, self.y2), (self.x3, self.y3))
        side_c = math.dist((self.x3, self.y3), (self.x1, self.y1))
        p = (side_a + side_b + side_c) / 2
        try:
            return math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
        except ValueError:
            raise ShapeError("Ошибка вычисления площади треугольника.")

class Rectangle:
    def __init__(self, identifier: str, x: float, y: float, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ShapeError("Ширина и высота прямоугольника должны быть положительными.")
        self.identifier = identifier
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник {self.identifier}: A=({self.x}, {self.y}), B=({self.x}, {self.y+self.height}), C=({self.x+self.width}, {self.y+self.height}), D=({self.x+self.width}, {self.y})"

    # Перемещение прямоугольника на плоскости
    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    # Вычисление площади прямоугольника
    def area(self):
        return self.width * self.height

# Метод сравнения площади треугольника и прямоугольника
def compare(triangle: Triangle, rectangle: Rectangle):
    if not isinstance(triangle, Triangle):
        raise TypeError("Первый аргумент должен быть объектом класса Triangle.")
    if not isinstance(rectangle, Rectangle):
        raise TypeError("Второй аргумент должен быть объектом класса Rectangle.")

    triangle_area = triangle.area()
    rectangle_area = rectangle.area()

    if math.isclose(triangle_area, rectangle_area):
        return f"Площади равны: {triangle_area:.2f}."
    elif triangle_area > rectangle_area:
        return f"Площадь треугольника ({triangle_area:.2f}) больше площади прямоугольника ({rectangle_area:.2f})."
    else:
        return f"Площадь прямоугольника ({rectangle_area:.2f}) больше площади треугольника ({triangle_area:.2f})."

# Тест
try:
    print("\nСозданные фигуры: ")
    triangle = Triangle("T1", 0, 0, 4, 0, 0, 3)
    print(triangle)
    rectangle = Rectangle("R1", 0, 0, 6, 2)
    print(rectangle)

    print("\nСравнение фигур:")
    print(compare(triangle, rectangle))

    print("\nФигуры после перемещения:")
    triangle.move(1, 1)
    print(triangle)
    rectangle.move(-1, -1)
    print(rectangle)
except (ShapeError, TypeError) as e:
    print(f"Ошибка: {e}")
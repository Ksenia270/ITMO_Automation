class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Метод для расчета площади прямоугольника."""
        return self.width * self.height

    def perimeter(self):
        """Метод для расчета периметра прямоугольника."""
        return 2 * (self.width + self.height)


# Создание объектов прямоугольников
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(7, 3)
rectangle3 = Rectangle(6, 8)

# Расчет площади и периметра для каждого прямоугольника
rectangles = [rectangle1, rectangle2, rectangle3]

for i, rect in enumerate(rectangles, start=1):
    area = rect.area()
    perimeter = rect.perimeter()
    print(f"Прямоугольник {i}: Площадь = {area}, Периметр = {perimeter}")


    class Math:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def addition(self):
            result = self.a + self.b
            print(f"Сумма {self.a} и {self.b} равна: {result}")

        def multiplication(self):
            result = self.a * self.b
            print(f"Произведение {self.a} и {self.b} равно: {result}")

        def division(self):
            if self.b != 0:
                result = self.a / self.b
                print(f"Частное {self.a} и {self.b} равно: {result}")
            else:
                print("Ошибка: деление на ноль!")

        def subtraction(self):
            result = self.a - self.b
            print(f"Разность {self.a} и {self.b} равна: {result}")


    # Пример использования класса
    math_operation = Math(10, 5)

    math_operation.addition()  # 10 + 5
    math_operation.subtraction()  # 10 - 5
    math_operation.multiplication()  # 10 * 5
    math_operation.division()  # 10 / 5


  
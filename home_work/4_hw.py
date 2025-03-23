class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(7, 3)
rectangle3 = Rectangle(6, 8)
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

    math_operation = Math(10, 5)

    math_operation.addition()
    math_operation.subtraction()
    math_operation.multiplication()
    math_operation.division()


class Button:
    def __init__(self, text, button_type="Кнопка", locator=""):
        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self):
        return f"Клик по кнопке {self.text}"

buttons = [
    Button("Text Box"),
    Button("Check Box"),
    Button("Radio Button"),
    Button("Web Tables"),
    Button("Buttons"),
    Button("Links"),
    Button("Broken Links - Images"),
    Button("Upload and Download"),
    Button("Dynamic Properties"),
]
for button in buttons:
    print(button.text)

for button in buttons:
    print(button.click())
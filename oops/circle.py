class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        area = 3.14 * self.radius * self.radius
        return area

    def calcPerimeter(self):
        peri = 2 * 3.14 * self.radius
        return peri

c1 = Circle(7)

print(c1.calcArea())
print(c1.calcPerimeter())
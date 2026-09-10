class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumbers(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, other):
        new_real = self.real + other.real
        new_img = self.img + other.img
        return Complex(new_real, new_img)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_img = self.img - other.img
        return Complex(new_real, new_img)
    
c1 = Complex(4, 5)
c2 = Complex(2, 3)
c1.showNumbers()
c2.showNumbers()
c3 = c1 + c2
c4 = c1 - c2
c3.showNumbers()
c4.showNumbers()
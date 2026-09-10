# class Car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class Toyota(Car):
#     def __init__(self, brand_name):
#         self.brand_name = brand_name

# class Fortuner(Toyota):
#     color = "black"
#     torque = "120 Nm"
#     cc = "2500"

#     def __init__(self, brand_name, type):
#         super().__init__(brand_name) 
#         self.type = type

# c1 = Fortuner("4x4", "Electric")

# c1.start()
# c1.stop()
# print(c1.brand_name)
# print(c1.cc)
        
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def calc_percentage(self):
        return str((self.math + self.chem + self.phy) / 3) + "%"

s1 = Student(87,98,78)

print(s1.calc_percentage)
        
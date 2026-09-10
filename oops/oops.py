# class Car:
#     def __init__(self, color, price):
#         self.color = color
#         self.price = price

#     def changeColor(self, newColor):
#         self.color = newColor

#     def changePrice(self, newPrice):
#         self.price = self.price

#     def getData(self):
#         print(f"Car Color is {self.color} and price is Rs.{self.price}")

# c1 = Car("Black", "3500000")
# c1.getData()

# c1.changeColor("Blue")
# c1.getData()


# class Avengers:

#     mission = "Protect Earth"

#     def __init__(self, name, weapon):
#         self.name = name
#         self.weapon = weapon

#     @classmethod
#     def changeMission(cls):
#         cls.mission = "Kill Thanos"

#     @staticmethod
#     def successMsg():
#         print("Mission Successful")

#     def printAvenger(self):
#         print(f"{self.name} with his {self.weapon} is on mission to {self.mission}")


# a1 = Avengers("Thor", "Hammer")
# a1.printAvenger()

# a2 = Avengers("Captain America", "Shield")
# a2.printAvenger()
    
# a1.changeMission()
# a1.printAvenger()
# a1.successMsg()

# class Account:

#     def __init__(self, acc_no, password, balance):
#         self.acc_no = acc_no 
#         self.__password = password
#         self.balance = balance

#     def get_password(self):
#         return self.__password

#     def change_password(self, new_pass):
#         self.__password = new_pass
#         return self.__password

# a1 = Account("7888788455", "secret@_423", "150000")

# print(a1.acc_no)
# print(a1.balance)
# print(a1.get_password())
# print(a1.change_password("secreted_private"))


# class Account:

#     def __init__(self, account_name, balance):
#         self.account_name = account_name
#         self.__balance = balance

#     def deposit_money(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Amount deposited successfully : Rs.{amount}, Remaining balance is Rs.{self.__balance}")
#         else:
#             print("Please enter valid amount to deposit")

#     def withdraw_money(self, amount):
#         if self.__balance > amount:
#             self.__balance -= amount
#             print(f"Amount withdrawn successfully : Rs.{amount}, Remaining balance is Rs.{self.__balance}")
#         else:
#             print(f"You do not have enough money to withdraw. Your current balance is : Rs.{self.__balance}")

#     @property
#     def balance(self):
#         return self.__balance


# a1 = Account("Manish Kumar", 1500000)

# print(a1.account_name)
# print(a1.balance)
# print(a1.deposit_money(-50000000))

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):

#     def start(self):
#         print("CAR Started")

#     def stop(self):
#         print("CAR Stopped")

#     def drive(self):
#         print("Lets go for a drive")

# c1 = Car()
# c1.start()
# c1.drive()
# c1.stop()


class Name:

    def __init__(self, first):
        self.first = first

    def __add__(self, other):
        return f"{self.first} {other.first}" 
        


# a = Name("Manish")
# b = Name("Agrahari")

# print(a + b)


class ComplexNumber:

    def __init__(self, img, real):
        self.img = img
        self.real = real

    def print_complex(self):
        print(f"{self.img}i + {self.real}j")

    def __add__(self, other):
        real_part = self.real + other.real
        img_part = self.img + other.img
        return f"{img_part}i + {real_part}j"

c1 = ComplexNumber(5, 7)
c2 = ComplexNumber(3, 12)
c1.print_complex()
c2.print_complex()
print(c1 + c2)

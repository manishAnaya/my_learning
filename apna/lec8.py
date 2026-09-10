# class Student:

#     college_name = "ABC College of Engineering"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new Student...")

#     def welcome(self):
#         print(f"Welcome Mr. {self.name} to {self.college_name} with {self.marks} marks")

# s1 = Student("Manish", "99")
# s1.welcome()
# # print(f"{s1.name} with marks: {s1.marks}")

# s2 = Student("Raghav", "100")
# s2.welcome()
# # print(f"{s2.name} with marks: {s2.marks}")


class Student:
    def __init__(self, name, english, hindi, maths):
        self.name = name
        self.english = english
        self.hindi = hindi
        self.maths = maths

    @staticmethod
    def hello():
        print("hello Sir")

    def calc_avg(self):
        sum_of_all = self.hindi + self.english + self.maths
        average = sum_of_all / 3
        print(average)
        return average

s1 = Student("Manish", 85, 87, 78)
s1.calc_avg()
Student.calc_avg()
Student.hello()

# class Account:
#     def __init__(self, accountNo, balance):
#         self.accountNo = accountNo
#         self.balance = balance

#     def credit(self, amount):
#         self.balance += amount

#     def debit(self, amount):
#         self.balance -= amount

#     def printBalance(self):
#         print(f"Your account {self.accountNo} has balance of {self.balance}")

# a1 = Account("37874577854", 1254)
# a1.credit(10000)
# a1.printBalance()
# a1.debit(1254)
# a1.printBalance()
    
    
        
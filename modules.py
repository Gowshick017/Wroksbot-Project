# import math
# import random
# import datetime

# # Find the square root of 5

# square_root = math.sqrt(5)
# print("Square root of 5 is:", square_root)

# # Find the factorial of 25

# factorial_value = math.factorial(25)
# print("Factorial of 25 is:", factorial_value)

# # Get the value of pi

# pi_value = math.pi
# print("Pi value is:", pi_value)

# # Generate a random number between 1 and 10

# random_number = random.randint(1, 10)
# print("Random number is:", random_number)


# # Get the current date and time

# today = datetime.datetime.now()
# print("Today's date and time is:", today)


# exception handling

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print("Result =", result)
# except ZeroDivisionError:
#     print("Second number cannot be zero.")
# except ValueError:
#     print("Please enter numbers only.")
# except Exception as e:
#     print("Error:", e)
# else:
#     print("Division completed successfully.")
# finally:
#     print("Program Finished.")



# Class and Object


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print("Employee Name:", self.name)
#         print("Employee Salary:", self.salary)
# e1 = Employee("Gowsi", 25000)
# e1.display()



# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def display(self):
#         print("Car Brand:", self.brand)
#         print("Car Model:", self.model)
# c1 = Car("Toyota", "Innova")
# c1.display()
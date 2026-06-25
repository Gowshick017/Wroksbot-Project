# 1 Greeting program


# def greet(name):
#     print("Hello, Welcome",name)
# while True:
#     name = input("Enter your name or enter exit to terminate: ")
#     if name.lower() == "exit":
#      print("ok.....")
#     break
# greet(name)


#  2 Count Vowels in a String


# def count_vowels(text):
#     count = 0
#     for ch in text.lower():
#         if ch in "aeiou":
#             count += 1
#     print("Vowels =", count)
# count_vowels("Python Programming")


# 3 Sum of Digits

# def sum_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total = total + digit
#         n = n // 10
#     print("Sum =", total)
# sum_digits(1234)

# 4 Count Vowels in a String

# def count_vowels(text):
#     count = 0
#     for ch in text.lower():
#         if ch in "aeiou":
#             count += 1
#     print("Vowels =", count)
# count_vowels("Python Programming")

# 5 Largest of Three Numbers

# def largest(a, b, c):
#     if a >= b and a >= c:
#         print(a)
#     elif b >= c:
#         print(b)
#     else:
#         print(c)
# largest(10, 50, 30)

# 6 Multiplication Table

# def table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)
# table(5)

#  7 Fibonacci Series

# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
# fibonacci(8)

#  8 Check Prime Number

# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             return
#     print("Prime")
# prime(11)

#  9  Print Numbers from 1 to 5

# def numbers():
#     for i in range(1, 6):
#         print(i)
# numbers()

# Check Even or Odd

# def even_odd(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# even_odd(8)


# def even_odd(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd(7)


# 11 Find Cube

# def cube(n):
#     print(n * n * n)
# cube(3)

#  12 Check Positive or Negative Number

# def check(n):
#     if n >= 0:
#         print("Positive")
#     else:
#         print("Negative")
# check(-10)

# def check(n):
#     if n >= 0:
#         print("Positive")
#     else:
#         print("Negative")
# check(7)

# 13 Print a Message Multiple Times

# def message():
#     for i in range(10):
#         print("Python is Easy")
# message()

# 14 Add Two Numbers

# def add(a, b):
#     print("Sum =", a + b)
# add(10, 20)

# 15 Find Maximum of Two Numbers

# def maximum(a, b):
#     if a > b:
#         print(a, "is greater")
#     else:
#         print(b, "is greater")
# maximum(15, 20)
# 1 Greeting program


# def greet(name):
#     print("Hello, Welcome",name)
# while True:
#     name = input("Enter your name or enter exit to terminate: ")
#     if name.lower() == "exit":
#      print("ok.....")
#     break
# greet(name)

#  2Count Vowels in a String


# def count_vowels(text):
#     count = 0
#     for ch in text.lower():
#         if ch in "aeiou":
#             count += 1
#     print("Vowels =", count)
# count_vowels("Python Programming")


# 3 Sum of Digits

def sum_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    print("Sum =", total)

sum_digits(1234)
# def root ():
#     num  = int(input("enter a value  : "))
#     s = num ** 0.5
#     print(s)
#
# root()

# def area_triangle ():
#     base = int(input("enter base value : "))
#     height = int(input("enter height value : "))
#     calculate  = 0.5 * base * height
#     print(calculate)
#
# area_triangle()

#swap variables
# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)

# import random
# print(random.randint(10,50))

# def convert ():
#     kilometers = eval(input("enter a kilometer : "))
#     miles = kilometers * 0.621371
#     print(miles)
#
# convert()

# def convert():
#     fahrenheit = eval(input("enter a value: "))
#     celsius = (fahrenheit - 32 ) / 1.8
#     print(celsius)
#
# convert()

# print in same line not in new line
# print("my name is ", end="")
# print("shashwat jain")

# Python Program to Get the Class Name of an Instance
# class toy:
#       def batman(self,name):
#             return name
#
# t = toy()
# print(t.__class__.__name__)

# Python Program to Differentiate Between type() and isinstance()
# class fruit():
#       def parent_mango(self):
#             pass
#
# class vegetable(fruit):
#       def parent_tomato(self):
#             pass
#
# kingoffruits = fruit()
# kingofvege = vegetable()
#
# print(type(kingoffruits) == fruit)
# print(type(kingoffruits) == vegetable)
#
# print(isinstance(kingofvege , fruit))
# print(isinstance(kingoffruits ,  fruit))

# def check():
#       num = eval(input("enter a value"))
#       if num > 0 :
#             print("its a positive number")
#       elif num < 0:
#             print("its a negative number")
#       else:
#             print("its a zero")
#
# check()
# check()
# check()

# def check():
#       num = int(input("enter a value"))
#       if num % 2 == 0:
#             print("its a even number")
#       else:
#             print("its a odd number")
#
# check()
# check()

# def leapyear():
#       num = int(input("enter a year:-"))
#       if num % 400 == 0 and num % 100 == 0:
#             print("its a leap year")
#       elif num % 4 == 0 and num % 100 != 0:
#             print("its  a leap year")
#       else:
#             print("its not a leap year")
#
# leapyear()
# leapyear()
# leapyear()

# def big_number():
#       num1 = int(input("enter first number:-"))
#       num2 = int(input("enter second number:-"))
#       num3 = int(input("enter third number:-"))
#       if num1 > num2 and num1 > num3:
#             print("num1 is greater")
#       elif num2 > num1 and num2 > num3:
#             print("num2 is greater")
#       else:
#             print("num3 is greater")
#
# big_number()
# big_number()
# big_number()

# def primenumber():
#       num = int(input("enter a number"))
#       if num > 1 :
#           for i in range(2,num,1):
#            if num % i == 0 :
#               print("its not a prime number")
#               break
#           else:
#             print("its a prime number")
#
# primenumber()
# primenumber()

# interval
# def primenumber():
#     num1 = 900
#     num2 = 1000
#     for num in range(num1 , num2 , 1):
#       if num > 1 :
#         for i in range(2,num):
#             if num % i == 0 :
#                break
#         else:
#             print(num)
#
# primenumber()


# def factorial():
#     num = int(input())
#     f = 1
#     if num < 0 :
#         print("nothing")
#     elif num == 0:
#         print("nothing")
#     else:
#         for i in range(1 , num + 1):
#             f = f * i
#             print(f)
#
# factorial()
# factorial()

# def table():
#     num = int(input())
#     for i in range(1,13):
#         print(i*num)
#
# table()
# def fibonacci(num):
#     a = 0
#     b = 1
#     c = 0
#     for i in range(0, num):
#         print(c)
#         a = c + b
#         c = b
#         b = a
#
# fibonacci(8)

#armstrong number
# num = int(input("enter a number:- "))
# s1 = str(num)
# sum = 0
# for i in s1:
#     sum += int(i) ** len(s1)
# if sum == num:
#     print('Given number is armstrong number :', num)
# else:
#     print('Given number is not a armstrong number :', num)


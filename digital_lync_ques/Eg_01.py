# try:
#     a = 5
#     b = 0
#     result = 5 / 0
# except ZeroDivisionError:
#     print("zerodivision error")
#
# try:
#     a = 10
#     b = 20
#     c = 0
#
#     op1 = b / a
#     op2 = a / c
#
#     list1 = [20,50,60]
#     print(list1[8])
# except ZeroDivisionError :
#     print("zero division error")
# finally:
#     print("finally block")

# print("my name is %s jain" %"shashwat")
# print("my age is %d " % 21)
# print("my contact number is %d " %9479674703)

# num = "25555455"
# print(",".join(num))

# marks = "In 10th class my score is {:.0%}"
# print(marks.format(0.62))

# def multiples():
#     for i in range(0,12):
#         if i % 3 != 0 and i % 5 != 0:
#             print(i)
#
# multiples()

# def square():
#     for i in range(0,100):
#         if i % 2 == 0:
#             sum = i ** 0.5
#             print(i)
#
# square()

# def divisible():
#     for i in range(1,100):
#         if i % 2 != 0 :
#             print(i)
#             if i % 7 == 0:
#                print(i)
#
# divisible()

# volwels = "a" , "e" , "i", "o" ,"u"
# name = "my school name is nachiketa school"
# for i in name:
#        if i in volwels:
#               print(i)

# def count_vowels():
#        name = input("enter a string:-")
#        my_vowels = ["a","e","o","u","i"]
#        for i in my_vowels:
#               if i in name:
#                      print(i)
#
# count_vowels()

# l= ["digital","lync","hyderabad","gachibowli","kukatpally"]
# a = "lync"
# for i in l :
#        if i == a :
#               print("yes it is present")

# z  = 65.33
# print(type(z))
# print(type(int(z)))
# squ = z **0.5
# print(squ)

# list1 = [2,3,4,5]
# for i in list1:
#        for s in range(1,13):
#               print(i , s*i)

# def reverse():
#        str = input("enter a string")
#        s = str[::-1]
#        print(s)
#
# reverse()

# list1 = [2,3,8,5,7,6,4,16]
# for i in list1:
#        if i % 2 == 0:
#               print(i)

# def factorial():
#        num = int(input("enter a number :-"))
#        f = 1
#        if num < 0 :
#               print("nothing")
#        elif num == 0 :
#               print("nothing")
#        else:
#               for i in range(1 , num + 1):
#                      f = f * i
#                      print(f)
# factorial()

# list1 = [12,24,35,24,88,120,155,88,120,155]
# list2 = []
# print(sorted((set((list1)))))

# dict1 = {}
# for i in range(1,20):
#     dict1[i] = i ** 0.5
#
# print(dict1)
# print(dict1.keys())
# print(dict1.values())

# set1 = {"name"}
# set1.add("shashwat")
# print(set1)

# list1 = [54,545,64,87,94]
# list2 = [545,78,54,87,64]
# list2.extend(list1)
# print(set(list2))

#
# a  = {55 , 88 , 65 , 74 , 25}
# b = {85 , 65 ,74 , 24 ,  32 }
#
# print(a.symmetric_difference(b))
#
# a = (54 , 85 ,"jain" , "shashwat" , 96 , 55.25, True ,"mahadev" ,["hey"] , {"1":"one"})
# print(type(a[0]))
# print(type(a[2]))
# print(type(a[5]))
# print(type(a[6]))
# print(type(a[8]))
# print(type(a[9]))
# print(type(a))

# a = (54 , 85 ,"jain" , "shashwat" , 96 , 55.25, True ,"mahadev" ,["hey"] , {"1":"one"})
# list1 = list(a)
# list1.remove("shashwat")
# print(list1)

# a = [54 , 85 ,"jain" , "shashwat" , 96 , 55.25, True ,"mahadev" ,("hey" ,"hello") , {"1":"one"}]
# for i in a :
#     if type(i) == tuple :
#         break
#     print(i)

# a = (54 , 85 ,"jain" , "shashwat" , 96 , 55.25, True ,"mahadev" ,["hey"] , {"1":"one"})
# for i in a :
#     print(a.index(i) , i )

# def add_pairs():
#     dict1 = {}
#     dict1 [input()] = input()
#     print(dict1)
#
# add_pairs()

# dict1 = {"s" :"shashwat" , "j":"jain"}
# dict2 = {"v": "vijaynagar" , "city" : "jabalpur"}
# dict1.update(dict2)
# print(dict1)

# dict1 = {'s': 'shashwat', 'j': 'jain', 'v': 'vijaynagar', 'c': 'jabalpur'}
# for i in dict1.items():
#     print(i)

# dict1 = {'s': 'shashwat', 'j': 'jain', 'v': 'vijaynagar', 'c': 'jabalpur'}
# dict1.pop("s")
# print(dict1)
# print(sorted(dict1.items()))

# list1 = [55,64,94,78,21,20,61]
# list1.sort()
# print(list1[5])

# list1 = [55,64,94,78,21,20,61,55,21,94,201,450]
# print(list(set(list1)))

# def table ():
#     num  = int(input("enter number:- "))
#     for i in range(1,13):
#         print(num * i )
#
# table()

# def leapyear():
#     num = int(input("enter year:- "))
#     if num % 400 == 0 and num % 100 == 0:
#         print("its a leap year")
#     elif num % 4 == 0 and num % 100 != 0:
#         print("its a leap year")
#     else :
#         print("its not a leap year")
#
# leapyear()

# def even_odd():
#     num = int(input("enter number: -"))
#     if num % 2 == 0:
#         print("its an even number")
#     else:
#         print("its an odd number")
#
# even_odd()

# def largest_number():
#     num1 = int(input("enter num1 :- "))
#     num2 = int(input("enter num2 :- "))
#     num3 = int(input("enter num3:- "))
#     if num1 > num2 and num1 > num3 :
#         print("num1 is greater than others")
#     elif num2 > num1 and num2 > num3:
#         print("num2 is greater than others")
#     else:
#         print("num3 is greater")
#
# largest_number()

# def grading():
#     num = int(input("enter a number:- "))
#     if num in range (80,101):
#         print("Grade A")
#     elif num in range (60,80):
#         print("Grade B")
#     elif num in range (50,60):
#         print("Grade C")
#     elif num in range (33,50):
#         print("Grade D")
#     else:
#         print("FAIL")
#
# grading()
# grading()
# grading()
# grading()

# def condition():
#         country = input("enter country name :- ")
#         states = input("enter states name: - ")
#         districts = int(input("enter districts number:- "))
#         print(country , states , districts)
#
# condition()

# def fibonaaci():
#     a = 0
#     b = 1
#     c = 0
#     for i in range(1,11):
#         print(c)
#         a = c + b
#         c = b
#         b = a
#
# fibonaaci()

# def multiples():
#     num = int(input("enter number: - "))
#     if num % 9 == 0 :
#         print(num , "its a multiple of 9")
#     else:
#         print(num , "its not a multiple of 9 ")
#
# multiples()

# def check ():
#     num = int(input("enter a number:- "))
#     if num > 1 :
#         for i in range(2, num, 1):
#          if num % i == 0:
#             print("its not a prime number")
#             break
#         else:
#             print("its a prime number")
#
# check()

# def check():
#     for i in range(1,50):
#         if i % 2 == 0 :
#             print(i)
#         elif i % 3 ==0:
#             print(i)
# check()

# num = int(input("enter number"))
# str1 = str(num)
# sum = 0
# for i in str1:
#     sum  += int(i) ** len(str1)
# if sum == num :
#         print(num , "its an armstrong number")
# else:
#         print("not an armstrong number")

# def sum_numbers():
#     num = int(input("enter number:-"))
#     sum = 0
#     for i in str(num):
#         sum += int(i)
#     print(sum)
# sum_numbers()

# str1 = "pythonbestforbeginners"
# print(str1[1::2])


# def reverse():
#     str1 = input("enter string:- ")
#     print(str1[::-1])
#
# reverse()

# def third_position():
#     str1 = input("enter a string:- ")
#     position = str1[::3]
#     print(position)
#
# third_position()

# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)

# n = "my name is shashwat jain"
# print(n.replace("s" , "S", 3))

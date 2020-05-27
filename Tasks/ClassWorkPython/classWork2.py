from random import randint
# 1
# number = int(input("Enter number: "))
# if number % 2 == 0:
#     print("{} is parne".format(number))
# else:
#     print("{} is neparne".format(number))
# ################################################

# num = int(input("Enter some number: "))
# i = 1
# factorial = 1
# while i <= num:
#     factorial *= i
#     i+= 1
#     print(factorial)

#################################################
# 2
# num = list(range(100))
# leng = len(num)
# i = 0
# while i <= leng:
#     i += 1
#     if i == leng:
#         continue
#     elif i % 2 == 0:
#         print(i)
#     else:
#         pass
# print("\n")
# for ind in num:
#     if ind == 0:
#         continue
#     elif ind % 2 == 0:
#         print(ind)

###################################################
# 3
# num = list(range(100))
# leng = len(num)
# i = 0
# while i < leng:
#     if i % 2 == 0:
#         print(i+1)
#     else:
#         pass
#     i += 1
    
# print("\n")
# for ind in num:
#     if ind % 2 == 0:
#         print(ind+1)
#     else:
#         continue

#####################################################
# 4
# list_number = list(range(10))
# j = 0
# for x in list_number:
#     list_number[j] = float(x)
#     j += 1
# print(list_number)
####################################################
# 5
# list_number = []
# x = 0
# j = 0
# i = 1
# n = int(input("Enter number: "))
# for x in range(n):
#     list_number.append(int(input("Enter some number: ")))
# while j <= n :
#     result = list_number[j] + list_number[i]
#     list_number.append(result)
#     j+=1
#     i+=1
# print(list_number)

####################################################
# 6
# list_string = []
# for x in range(4):
#     list_string.append(input("Enter some text type string: "))
# for x in list_string:
#     # task 6
#     # print(x)
#     # task 7
#     for i in x:
#         print(i,end='#')
#####################################################
# 8
# a = input("Enter some number: ")

# if a / a :
#     print()
#  task 9
# a = randint(0,100)
# b = []

# print(a)
# for i in str(a):
#     b.append(int(i))
# print(max(b))
# task 10
# text = str(input("Enter some text: "))
# rev = text[::-1]

# if text == rev:
#     print("Текст є однаковий як і відзеркалений")
# else:
#     print("Текст не є однаковий як і відзеркалений")
# task 2.1
# a = []
# n = int(input("Enter amount indexes: "))
# for i in range(n):
#     a.append(int(input("Enter number: ")))
# print(a)
# print("Max number from a list is {}".format(max(a)))
# print("Min number from a list is {}".format(min(a)))
# # task 2.2
# range_list = list(range(10+1))
# print(range_list)
# for i in range_list:
#     if i == 0:
#         continue
#     if i % 2 == 0:
#         print("Pair number {} divides on 2".format(i))
#     elif i % 3 == 0:
#         print("The unpaired number {} divides on 3 ".format(i))
#     if not i % 2 == 0 and not i % 3 == 0 and i == 0:
#         print("The number {} does not divide on 3 and 2 ".format(i))
#     else:
#         pass

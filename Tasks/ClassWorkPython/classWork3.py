# task 1
# def findSum(*num):
#     n = len(num)
#     sum = 0
#     for x in num:
#         sum += x
#     result = sum / n
#     print(result)
# findSum(1,2,3,4)
#  task 2
# somenum = int(input("Enter some number: "))
# def absval(num):
#     if 0 > num:
#         print(-num)
#     else:
#         print(num)
# absval(somenum)
# task 3
# def maxNumber(*nums):
#     """ We found the max number """
#     print(max(nums))

# maxNumber(15,100)
# print(maxNumber.__doc__)
# task 4
# def findAreaRectangle(a,b):
#     print("Are of rectangle is",a*b)

# def findAreaTriangle(a,b,c):
#     p = (a+b+c)/2
#     s = (p*(p-a)*(p-b)*(p-c))**0.5
#     print("Area of triangle is",s)

# def findAreaCircle(r):
#     s = 3.14*(r**2)
#     print("Area of Circle is",s)

# print("Enter pls some from thise > circle \n"+ " "*28 + "triangle\n" + " "*28 + "rectangle")
# figure = str(input("What figure?: "))

# if figure == "circle" or figure == "Circle":
#     r = float(input("Enter area: "))
#     findAreaCircle(r)
# elif figure == "triangle" or figure == "Triangle":
#     a = float(input("Enter area of a: "))
#     b = float(input("Enter area of b: "))
#     c = float(input("Enter area of c: "))
#     findAreaTriangle(a,b,c)
# elif figure == "rectangle" or figure == "Rectangle":
#     a = float(input("Enter area of a: "))
#     b = float(input("Enter area of b: "))
#     findAreaRectangle(a,b)
# task 5
# num = input("Enter some number: ")

# def findSumNumbers(num):
#     i = 0
#     result = 0
#     for j in range(len(num)):
#         result += int(num[i])
#         i += 1
#     print(result)
# findSumNumbers(num)
# # task 6

# task 7

# num = int(input("Enter some number: "))
# def fiboNumbers(num):
#     fibo = [0,1]
#     while fibo[-1] <= num:
#         fibo.append(fibo[-2] + fibo[-1])
#         if fibo[-1] > num:
#             del fibo[-1]
#             break
#     print(fibo)    
        
# fiboNumbers(num)     

# task 8
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# c = int(input("Enter c number: "))

# def dissqrr(a,b,c):
#     x = (-b + ((b**2)-(4*a*c))**0.5)/(2*a)
#     print(x)
# dissqrr(a,b,c)

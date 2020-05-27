# class Figure:
#     def __init__(self,color):
#         self.color = color

#     def square(self):
#         s = self.x * self.y
    
#     def get_info(self):
#         print("Color is " + str(self.color))
#         print("Width  is " + str(self.x) + " and " + "hight is " + str(self.y))
# class Rectangle(Figure):
#     def __init__(self,color,x=200,y=100):
#         super().__init__(color)
#         self.x = x
#         self.y = y
# a = Rectangle("Red")
# a.get_info()

class Figure:
    def __init__(self,no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSide(self):
        self.sides = [float(input("Enter Side " + str(i+1) + " : ")) for i in range(self.n)]

    def get_info(self):
        for i in range(self.n):
            print("Side " + str(i+1) + " : " + str(self.sides[i]))

class Triangle(Figure):
    def __init__(self,no_of_sides):
        Figure.__init__(self,no_of_sides)
    def findArea(self):
        x,y,z = self.sides
        s = (x+y+z) / 2
        print(s)


a = Triangle(3)
a.inputSide()
a.get_info()
a.findArea()

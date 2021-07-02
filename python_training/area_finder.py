class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth*self.length

class square():
        def __init__(self, side):
            self.side = side
  

        def area(self):
            return self.side*self.side


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
rectangle = rectangle(a, b)
print("Area of rectangle:", rectangle.area())
c = int(input("Enter side of square: "))
square = square(c)
print("Area of square:", square.area())

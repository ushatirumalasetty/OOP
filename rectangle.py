class Rectangle:

   def __init__(self, length, breadth):
       self.length=length
       self.breadth=breadth

   def calculate_area(self):
       area=self.length*self.breadth
       return area

   def calculate_perimeter(self):
       perimeter=2*(self.length+self.breadth)
       return perimeter

if __name__ == "__main__":
   rectangle_one = Rectangle(5, 5)
   print("area of rectangle is ", rectangle_one.calculate_area())
   print("perimeter of rectangle is ",  rectangle_one.calculate_perimeter())

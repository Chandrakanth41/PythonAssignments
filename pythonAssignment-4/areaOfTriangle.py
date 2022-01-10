class Triangle:
 def __init__(self, side1, side2, side3):
  self.side1 = side1
  self.side2 = side2
  self.side3 = side3

class Triangle_Side_Measurements(Triangle):
 def __init__(self, side1, side2, side3):
  super(Triangle_Side_Measurements, self).__init__(side1, side2, side3)

 def calculate_area(self):
  s = (self.side1 + self.side2 + self.side3)/2
  print (str(s))
  return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5


side1 = int(input("Enter side1"))
side2 = int(input("Enter side2"))
side3 = int(input("Enter side3"))
AOT = Triangle_Side_Measurements(side1,side2,side3)
print ("Area of triangle = " + str(AOT.calculate_area()) )
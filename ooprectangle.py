class rectangle:
    def set_dimension(self,height,width):
       self.height=height
       self.width=width


    def area(self):
        return self.height*self.width    

    def perimeter(self):
        return 2*(self.height+self.width)    

# creating objects
rectangle1=rectangle()
rectangle1.set_dimension(4,3)
print("the height and width are:",rectangle1.height,rectangle1.width)
print("the area is :",rectangle1.area())
print("the perimeter is:",rectangle1.perimeter())
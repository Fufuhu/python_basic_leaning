import math
class Circle():
    def __init__(self, radius, color="white"):
        self.__radius = radius
        self.__color = color
        
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    radius = property(get_radius)
    color = property(get_color)
    
class NewCircle(Circle):
    def __init__(self, radius, color="white"):
        super().__init__(radius, color)
    
    def menseki(self):
        return math.pi * (self.radius ** 2)


c1 = NewCircle(10, "black")
print("半径:{}, 色:{}, 面積:{:.2f}".format(c1.radius, c1.color, c1.menseki()))
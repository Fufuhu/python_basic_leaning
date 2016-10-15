class Customer:
    bmi = 22
    def __init__(self, number, name, height=0):
        self.__number = number
        self.__name = name
        self.__height = height
        
    def get_number(self):
        return self.__number
        
    def set_number(self, number):
        self.__number = number
    
    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        self.__height = height
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
     
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2


taro = Customer(101, "斎藤太郎", 180)

name = taro.get_name()
taro.set_number(99)

number = taro.get_number()
height = taro.get_height()

print("{}:{} {} cm".format(number, name, height))

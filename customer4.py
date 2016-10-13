from datetime import date

class Customer:
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
    
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
        
# インスタンス生成
taro = Customer(101, "斎藤太郎", 180)
taro.birthdate = date(1989, 7, 3)
print(str(taro.birthdate))
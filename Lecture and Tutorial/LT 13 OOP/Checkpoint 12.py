class Goodies:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, new_name):
        self.name = new_name

    def set_price(self, new_price):
        self.price = new_price

    def display(self):
        print('name:', self.name)
        print('price:', self.price)



Cookies= Goodies('Cookies', 10)
Love_Letters= Goodies('Love Letters', 8)



class HealthierGoodies(Goodies):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.less_sugar = False
        self.down_size = False

    def get_less_sugar(self):
        return self.less_sugar

    def get_down_size(self):
        return self.down_size

    def set_less_sugar(self):
        self.less_sugar = True

    def set_down_size(self):
        self.down_size = True
        self.price *= 0.75

    def display(self):
        print('name:', self.name)
        print('price:', self.price)
        print('less sugar:', self.less_sugar)
        print('down size:', self.down_size)



tart1 = HealthierGoodies('Pineapple Tarts', 10)






item1 = HealthierGoodies('Pineapple Tarts', 12)
item1.set_less_sugar()

item2 = HealthierGoodies('Almond Cookies', 10)
item2.set_down_size()

item3 = Goodies('Love Letters', 9)

item4 = HealthierGoodies('Cheese Cookies', 10)







    

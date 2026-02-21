class Car:
    def __init__(self, name='BMW', price=5000, year=2022):
        self.name = name
        self.price = price
        self.year = year

    def get_info(self):
        return f'{self.name} {self.price} {self.year}'


class Car_little(Car):
    def __init__(self, name, price, year, color, mator):
        super().__init__(name, price, year)
        self.color = color
        self.mator = mator

    def get_car_little(self):
        return f'{self.name} {self.price} {self.year} {self.color} {self.mator}'


a = Car()
b = Car_little('BMW X5', 32000, 2021, 'red', 3.2)
print(a.get_info())
print(b.get_car_little())

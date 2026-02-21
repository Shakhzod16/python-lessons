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

# Masalalar
# 1 - masala
class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

    def harakatlan(self):
        print(f"{self.nomi} harakatlanmoqda")


class Car(Transport):
    def __init__(self, nomi, tezlik, yoqilgi_turi):
        super().__init__(nomi, tezlik)
        self.yoqilgi_turi = yoqilgi_turi

    def harakatlan(self):
        print("Mashina yo'lda harakatlanmoqda")


transport = Transport("Velosiped", 25)
car = Car("Malibu", 220, "Benzin")

transport.harakatlan()
car.harakatlan()

# 2 - masala
# 2️⃣ Hayvonlar

# Animal klassi:

# nomi, yoshi

# ovoz_ber() metodi (umumiy xabar chiqarsin)

# Dog va Cat klasslari Animal dan voris bo‘lsin.

# Har biri ovoz_ber() metodini o‘ziga xos qilib override qilsin.


class Animal:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz_ber(self):
        print("Hayvon ovoz chiqarmoqda...")


class Dog(Animal):
    def ovoz_ber(self):
        print(f"{self.nomi} vov-vov dedi ")



dog1 = Dog("Rex", 3)

dog1.ovoz_ber()

# 3 - masala

#  Xodimlar tizimi

# Employee klassi:

# ism, maosh

# info() metodi

# Manager klassi:

# Qo‘shimcha bonus

# umumiy_maosh() metodi (maosh + bonus)

# class Employee:

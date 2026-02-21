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


class Employee:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def info(self):
        print(f"Ism: {self.ism}")
        print(f"Maosh: {self.maosh}")

class Manager(Employee):
    def __init__(self, ism, maosh, bonus):
        super().__init__(ism, maosh)
        self.bonus = bonus

    def umumiy_maosh(self):
        return self.maosh + self.bonus


manager1 = Manager("Vali", 1000, 300)
manager1.info()

print(f"Umumiy maosh: {manager1.umumiy_maosh()}")

# 4 - masala
#  Talabalar

# Person klassi:

# ism, familiya

# Student klassi:

# Qo‘shimcha kurs, baholar (ro‘yxat)

# orta_baho() metodini yozing.


class Person:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def full_name(self):
        return f"{self.ism} {self.familiya}"



class Student(Person):
    def __init__(self, ism, familiya, kurs, baholar):
        super().__init__(ism, familiya)
        self.kurs = kurs
        self.baholar = baholar

    def orta_baho(self):
        if len(self.baholar) == 0:
            return 0
        return sum(self.baholar) / len(self.baholar)



student1 = Student("Ali", "Valiyev", 2, [5, 4, 3, 5, 4])

print("Talaba:", student1.full_name())

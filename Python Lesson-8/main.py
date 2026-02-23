
# 1. BANK TIZIMI


class Account:
    def __init__(self, balans):
        self.__balans = balans

    def deposit(self, summa):
        if summa > 0:
            self.__balans += summa
            print(f"{summa} so'm qo'shildi.")
        else:
            print("Noto'g'ri summa!")

    def withdraw(self, summa):
        if 0 < summa <= self.__balans:
            self.__balans -= summa
            print(f"{summa} so'm yechildi.")
        else:
            print("Yetarli mablag' yo'q!")

    def get_balans(self):
        return self.__balans


class SavingsAccount(Account):
    def __init__(self, balans, foiz):
        super().__init__(balans)
        self.foiz = foiz

    def add_interest(self):
        foiz_summasi = self.get_balans() * self.foiz / 100
        self.deposit(foiz_summasi)
        print(f"Foiz qo'shildi: {foiz_summasi}")



class CreditAccount(Account):
    def __init__(self, balans, kredit_limit):
        super().__init__(balans)
        self.kredit_limit = kredit_limit

    def withdraw(self, summa):
        if summa <= self.get_balans() + self.kredit_limit:

            new_balans = self.get_balans() - summa

            self.deposit(-summa)
            print(f"{summa} so'm kredit hisobdan yechildi.")
        else:
            print("Kredit limitdan oshib ketdi!")



# 2. UNIVERSITET TIZIMI


class Person:
    def __init__(self, ism, passport):
        self.ism = ism
        self.__passport = passport

    def get_passport(self):
        return self.__passport

    def info(self):
        return f"Ism: {self.ism}"


class Student(Person):
    def __init__(self, ism, passport, kurs):
        super().__init__(ism, passport)
        self.kurs = kurs
        self.__grades = [] 

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def info(self):
        return f"Student: {self.ism}, Kurs: {self.kurs}, O'rtacha: {self.get_average()}"


class Teacher(Person):
    def __init__(self, ism, passport, fan, salary):
        super().__init__(ism, passport)
        self.fan = fan
        self.salary = salary

    def info(self):
        return f"O'qituvchi: {self.ism}, Fan: {self.fan}, Maosh: {self.salary}"
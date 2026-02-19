
# Student degan yangi CLASS (model, qolip) yaratilyapti
# Bu - oddiy o'zgaruvchi emas, balki yangi turdagi obyekt
class Student:

    # __init__ - konstruktor (obyekt yaratilgan paytda avtomatik ishga tushadi)
    # Ya'ni Student(...) yozilgan zahoti shu funksiya ishlaydi
    def __init__(self, name, age, group, ball):

        # self - yaratilayotgan studentning o'zi
        # pastdagi qatorda biz studentning xususiyatlarini (atributlarini) berayapmiz

        self.name = name      # student ismi saqlanadi
        self.age = age        # student yoshi saqlanadi
        self.group = group    # student qaysi yo'nalishda o'qiyapti
        self.ball = ball      # student olgan bali (reytingi)

    # Bu - metod (class ichidagi funksiya)
    # Har bir student o'zi haqida ma'lumot qaytara oladi
    def get_info(self):

        # f-string orqali student haqidagi barcha ma'lumotlarni matn qilib qaytaryapti
        return f"Name: {self.name}\nAge: {self.age}\nGroup: {self.group}\nBall: {self.ball}"


# Bu yerda biz 4 ta student obyekt yaratdik
# Har biri alohida obyekt (real hayotda 4 ta odam)

students = [
    Student("Ivan", 19, "Python", 90),   # 1-student yaraldi
    Student("alix", 20, "Java", 78),     # 2-student yaraldi
    Student("vova", 21, "C++", 99),      # 3-student yaraldi
    Student("vali", 22, "C#", 87)        # 4-student yaraldi
]

# max() - ro'yxat ichidan eng kattasini topadi
# key=lambda x: x.ball -> solishtirishda studentning o'zini emas,
# balki uning ball qiymatini tekshiradi

top_student = max(students, key=lambda x: x.ball)

# Ya'ni Python ichida quyidagi jarayon bo'ladi:
# Ivan -> 90
# alix -> 78
# vova -> 99
# vali -> 87
# eng kattasi 99 -> vova tanlanadi


# get_info() metodi chaqirilib, tanlangan student haqida ma'lumot chiqariladi
print(top_student.get_info())



# Masala sharti:

# Car nomli klass yarating.

# Xususiyatlari:

# marka

# model

# yil

# rang

# narx

# Vazifa:

# 5 ta avtomobil obyektini yarating.

# Eng qimmat avtomobilni aniqlang.

# 2020-yildan keyingi avtomobillarni chiqaring.

class Cars:
  def __init__(self, marka, model, yil, rang, narx):
    self.marka = marka
    self.model = model
    self.yil = yil
    self.rang = rang
    self.narx = narx

  def format_price(self):
    if self.narx >= 1_000_000:
        qiymat = self.narx / 1_000_000
        if qiymat.is_integer():
            return f"{int(qiymat)}mln"
        return f"{qiymat:.1f}mln"

    elif self.narx >= 1_000:
        qiymat = self.narx / 1_000
        if qiymat.is_integer():
            return f"{int(qiymat)}k"
        return f"{qiymat:.1f}k"

    else:
        return str(self.narx)

  def get_info(self):
    return f"""Marka: {self.marka}
    Model: {self.model}
    Yil: {self.yil}
    Rang: {self.rang}
    Narx: {self.format_price()} so'm"""


cars = [
  Cars("Toyota", "Corolla", 2020, "Qora", 200000),
  Cars("Honda", "Civic", 2019, "Oq", 2500000),
  Cars("Ford", "Mustang", 2018, "Qizil", 3000000),
  Cars("BMW", "X5", 2021, "Sariq", 4000000),
  Cars("Tesla", "Model S", 2022, "Oq", 5000000)
]

top_Car = max(cars, key=lambda x: x.narx)

print(top_Car.get_info())


# 2️⃣ Kitob (Book) klassi Masala sharti:

# Book nomli klass yarating.

# Xususiyatlari:

# nomi

# muallif

# sahifa_soni

# narx

# janr

# Vazifa:

# 4 ta kitob obyektini yarating.

# Eng qimmat kitobni aniqlang.

# Sahifasi 300 dan ortiq kitoblarni chiqaring.


class Book :
  def __init__(self, nomi, muallif, sahifa_soni, narx, janr):
    self.nomi = nomi
    self.muallif = muallif
    self.sahifa_soni = sahifa_soni
    self.narx = narx
    self.janr = janr

  def format_price(self):
    if self.narx >= 1_000_000:
        qiymat = self.narx / 1_000_000
        if qiymat.is_integer():
            return f"{int(qiymat)}mln"
        return f"{qiymat:.1f}mln"

    elif self.narx >= 1_000:
        qiymat = self.narx / 1_000
        if qiymat.is_integer():
            return f"{int(qiymat)}k"
        return f"{qiymat:.1f}k"

    else:
        return str(self.narx)



  def get_info(self):
    return f"""Nomi: {self.nomi}
Muallif: {self.muallif}
Sahifa soni: {self.sahifa_soni}
Narx: {self.format_price()} so'm
Janr: {self.janr}"""


books = [
  Book("The Great Gatsby", "F. Scott Fitzgerald", 180, 1200000, "Romance"),
  Book("To Kill a Mockingbird", "Harper Lee", 281, 800000, "Fiction"),
  Book("1984", "George Orwell", 328, 500000, "Dystopian"),
  Book("Pride and Prejudice", "Jane Austen", 432, 900000, "Romance"),
]

print("=== Eng qimmat kitob ===\n")
qimmat = max(books, key=lambda b: b.narx).get_info()
print(qimmat)

print("\n=== Sahifasi 300 dan ortiq kitoblar ===\n")
for book in filter(lambda b: b.sahifa_soni > 300, books):
    print(book.get_info(), "\n----------------------")

# 4️⃣ Bank hisobi (BankAccount) klassi

# Masala sharti:

# BankAccount nomli klass yarating.

# Xususiyatlari:

# hisob_raqami

# egasi

# balans

# Vazifa:

# 3 ta hisob yarating.

# Eng katta balansli hisobni toping.

# Balansi 0 dan kichik bo‘lgan hisoblarni chiqaring.

class BankAccount:
  def __init__(self, hisob_raqami, egasi, balans):
    self.hisob_raqami = hisob_raqami
    self.egasi = egasi
    self.balans = balans

  def format_price(self):
    if self.balans >= 1_000_000:
        qiymat = self.balans / 1_000_000
        if qiymat.is_integer():
            return f"{int(qiymat)}mln"
        return f"{qiymat:.1f}mln"

    elif self.balans >= 1_000:
        qiymat = self.balans / 1_000
        if qiymat.is_integer():
            return f"{int(qiymat)}k"
        return f"{qiymat:.1f}k"

    else:
        return str(self.balans)

  def get_info(self):
    return f"""Hisob raqami: {self.hisob_raqami}
    Egasi: {self.egasi}
    Balans: {self.format_price()} so'm"""

accounts = [
  BankAccount(1, "Ivan", 1000000),
  BankAccount(2, "Alex", 5000000),
  BankAccount(2, "Alex", -500000),
  BankAccount(3, "Vova", -2000000),
  BankAccount(4, "Vali", 0),
]

print("=== Eng katta balansli hisob ===\n")
qimmat = max(accounts, key=lambda b: b.balans).get_info()
print(qimmat)

print("\n=== Balansi 0 dan kichik bo'lgan hisoblar ===\n")
for account in filter(lambda b: b.balans < 0, accounts):
    print(account.get_info(), "\n----------------------")


# Masala sharti:

# Phone nomli klass yarating.

# Xususiyatlari:

# brend

# model

# xotira

# narx

# rang

# Vazifa:

# 5 ta telefon obyektini yarating.

# Eng arzon telefonni toping.

# 128GB va undan yuqori xotirali telefonlarni chiqaring.

class Phone:
  def __init__(self, brend, model, xotira, narx, rang):
    self.brend = brend
    self.model = model
    self.xotira = xotira
    self.narx = narx
    self.rang = rang

  def format_price(self):
    if self.narx >= 1_000_000:
        qiymat = self.narx / 1_000_000
        if qiymat.is_integer():
            return f"{int(qiymat)}mln"
        return f"{qiymat:.1f}mln"

    elif self.narx >= 1_000:
        qiymat = self.narx / 1_000
        if qiymat.is_integer():
            return f"{int(qiymat)}k"
        return f"{qiymat:.1f}k"

    else:
        return str(self.narx)

  def get_info(self):
    return f"""Brend: {self.brend}
    Model: {self.model}
    Xotira: {self.xotira}
    Narx: {self.format_price()} so'm
    Rang: {self.rang}"""

phones = [
  Phone("Apple", "iPhone 13", 128, 1200000, "Qora"),
  Phone("Samsung", "Galaxy S21", 128, 800000, "Qora"),
  Phone("Xiaomi", "Mi 11", 128, 500000, "Qora"),
  Phone("Huawei", "Mate 30", 128, 900000, "Qora"),
  Phone("Nokia", "3310", 32, 200000, "Qora"),
]

print("=== Eng arzon telefon ===\n")
qimmat = min(phones, key=lambda b: b.narx).get_info()
print(qimmat)

print("\n=== 128GB va undan yuqori xotirali telefonlar ===\n")
for phone in filter(lambda b: b.xotira > 128, phones):
    print(phone.get_info(), "\n----------------------")


# Employee nomli klass yarating.

# Xususiyatlari:

# ism

# lavozim

# ish_staji (yil)

# oylik

# bo‘lim

# Vazifa:

# 5 ta xodim obyektini yarating.

# Eng katta oylik oladigan xodimni toping.

# Ish staji 5 yildan yuqori bo‘lgan xodimlarni chiqaring.



class Employee:
  def __init__(self, ism, lavozim, ish_staji, oylik, bolim):
    self.ism = ism
    self.lavozim = lavozim
    self.ish_staji = ish_staji
    self.oylik = oylik
    self.bolim = bolim

  def format_price(self):
    if self.oylik >= 1_000_000:
        return f"{self.oylik/1_000_000:.1f}mln".replace(".0","")
    elif self.oylik >= 1_000:
        return f"{self.oylik/1_000:.1f}k".replace(".0","")
    return str(self.oylik)

  def get_info(self):
    return f"""Ism: {self.ism}
Lavozim: {self.lavozim}
Ish staji: {self.ish_staji} yil
Oylik: {self.format_price()} so'm
Bo'lim: {self.bolim}"""


employees = [
  Employee("Ivan", "Dekan", 5, 5000000, "IT"),
  Employee("Alex", "Dekan", 6, 6000000, "IT"),
  Employee("Vova", "Dekan", 7, 7000000, "IT"),
  Employee("Vali", "Dekan", 8, 8000000, "IT"),
  Employee("Vasiliy", "Dekan", 9, 9000000, "IT"),
]

# Eng katta oylik
print("=== Eng katta oylik oladigan xodim ===\n")
print(max(employees, key=lambda b: b.oylik).get_info())

# 5 yildan ortiq staj
print("\n=== Ish staji 5 yildan yuqori bo'lgan xodimlar ===\n")
for e in filter(lambda b: b.ish_staji > 5, employees):
    print(e.get_info(), "\n----------------------")


# University nomli klass yarating.

# Xususiyatlari:

# nomi

# joylashuvi

# talabalar_soni

# fakultetlar_soni

# reyting

# Vazifa:

# 3 ta universitet obyektini yarating.

# Eng ko‘p talabaga ega universitetni toping.

# Reytingi 80 dan yuqori bo‘lgan universitetlarni chiqaring


class University:
  def __init__(self, nomi, joylashuvi, talabalar_soni, fakultetlar_soni, reyting):
    self.nomi = nomi
    self.joylashuvi = joylashuvi
    self.talabalar_soni = talabalar_soni
    self.fakultetlar_soni = fakultetlar_soni
    self.reyting = reyting

  def get_info(self):
    return f"""Nomi: {self.nomi}
Joylashuvi: {self.joylashuvi}
Talabalar soni: {self.talabalar_soni}
Fakultetlar soni: {self.fakultetlar_soni}
Reyting: {self.reyting}"""

universities = [
  University("O'zbekiston texnologiyali universiteti", "Toshkent", 10000, 5, 90),
  University("O'zbekiston texnologiyali universiteti", "Toshkent", 10000, 5, 80),
  University("O'zbekiston texnologiyali universiteti", "Toshkent", 10000, 5, 70),
  University("O'zbekiston texnologiyali universiteti", "Toshkent", 10000, 5, 60),
  University("O'zbekiston texnologiyali universiteti", "Toshkent", 10000, 5, 50),
]

print("=== Eng ko'p talabaga ega universitet ===\n")
print(max(universities, key=lambda b: b.talabalar_soni).get_info())

print("\n=== Reytingi 80 dan yuqori bo'lgan universitetlar ===\n")
for u in filter(lambda b: b.reyting > 80, universities):
    print(u.get_info(), "\n----------------------")
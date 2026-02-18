# # Student degan yangi CLASS (model, qolip) yaratilyapti
# # Bu - oddiy o'zgaruvchi emas, balki yangi turdagi obyekt
# class Student:

#     # __init__ - konstruktor (obyekt yaratilgan paytda avtomatik ishga tushadi)
#     # Ya'ni Student(...) yozilgan zahoti shu funksiya ishlaydi
#     def __init__(self, name, age, group, ball):

#         # self - yaratilayotgan studentning o'zi
#         # pastdagi qatorda biz studentning xususiyatlarini (atributlarini) berayapmiz

#         self.name = name      # student ismi saqlanadi
#         self.age = age        # student yoshi saqlanadi
#         self.group = group    # student qaysi yo'nalishda o'qiyapti
#         self.ball = ball      # student olgan bali (reytingi)

#     # Bu - metod (class ichidagi funksiya)
#     # Har bir student o'zi haqida ma'lumot qaytara oladi
#     def get_info(self):

#         # f-string orqali student haqidagi barcha ma'lumotlarni matn qilib qaytaryapti
#         return f"Name: {self.name}\nAge: {self.age}\nGroup: {self.group}\nBall: {self.ball}"


# # Bu yerda biz 4 ta student obyekt yaratdik
# # Har biri alohida obyekt (real hayotda 4 ta odam)

# students = [
#     Student("Ivan", 19, "Python", 90),   # 1-student yaraldi
#     Student("alix", 20, "Java", 78),     # 2-student yaraldi
#     Student("vova", 21, "C++", 99),      # 3-student yaraldi
#     Student("vali", 22, "C#", 87)        # 4-student yaraldi
# ]

# # max() - ro'yxat ichidan eng kattasini topadi
# # key=lambda x: x.ball -> solishtirishda studentning o'zini emas,
# # balki uning ball qiymatini tekshiradi

# top_student = max(students, key=lambda x: x.ball)

# # Ya'ni Python ichida quyidagi jarayon bo'ladi:
# # Ivan -> 90
# # alix -> 78
# # vova -> 99
# # vali -> 87
# # eng kattasi 99 -> vova tanlanadi


# # get_info() metodi chaqirilib, tanlangan student haqida ma'lumot chiqariladi
# print(top_student.get_info())



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

class Car:
  def __init__(self, marka, model, yil, rang, narx):
    self.marka = marka
    self.model = model
    self.yil = yil
    self.rang = rang
    self.narx = narx

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

# frontend🧑🏻‍💻👩‍💻, [18.02.2026 9:16]
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

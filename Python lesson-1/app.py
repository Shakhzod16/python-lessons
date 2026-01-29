# a = 5
# b = 6
# print(a + b)

# # 1️⃣ int — Butun sonlar
# age = 21
# year = 2026

# # 2️⃣ float — O‘nli sonlar
# price = 19.99
# height = 1.75

# # 3️⃣ complex — Kompleks sonlar
# z = 3 + 4j

# # 4️⃣ str — Matn (string)
# name = "Shahzod"
# message = 'Hello Python'

# # 5️⃣ bool — Mantiqiy qiymat
# is_active = True
# is_admin = False

# # 6️⃣ list — Ro‘yxat (o‘zgaruvchan)
# numbers = [1, 2, 3, 4]
# names = ["Ali", "Vali"]

# # 7️⃣ tuple — O‘zgarmas ro‘yxat
# colors = ("red", "green", "blue")

# # 8️⃣ set — Takrorlanmas elementlar
# unique_numbers = {1, 2, 3, 3}
# # Natija: {1, 2, 3}

# # 9️⃣ dict — Kalit-qiymat juftligi
# user = {
#     "name": "Shahzod",
#     "age": 21
# }

# # 🔟 NoneType — Bo‘sh qiymat
# result = None

# # 🔍 Ma’lumot turini bilish
# x = 10
# print(type(x))  # <class 'int'>

# Topshiriq
# 1 - masala

# ===================================================

# a = ['apple', 'banana', 'orange', 'grape','banana', 'mango']
# a[0]='limmon'
# a.append('limmon')
# a.remove('banana')
# del a[2]
# a.pop(3)
# a.insert(2,'limmon')


# print(a.index('banana'))
# print(a.count('banana'))
# a.reverse()
# a.sort(reverse=True)
# a.clear()
# b =sorted(a,reverse=True)
# a.sort()
# print(b)


# num = [5, 2, 9, 1, 5, 6]
# # print(sum(num))          # Output: 28
# print(min(num))          # Output: 1
# print(max(num))          # Output: 9

# fruits = ['apple', 'banana', 'cherry']
# print(len(fruits))  # Output: 3


# ==================================================================

# 1️⃣ List yaratish
# a = ['apple', 'banana', 'orange', 'grape', 'banana', 'mango']


# 👉 Bir nechta qiymatlarni bitta o‘zgaruvchida saqlash

# 2️⃣ Elementni o‘zgartirish
# a[0] = 'limmon'


# 📌 Vazifasi: Index bo‘yicha elementni almashtiradi
# ➡️ apple → limmon

# 3️⃣ append()
# a.append('limmon')


# 📌 Vazifasi: List oxiriga element qo‘shadi

# 4️⃣ remove()
# a.remove('banana')


# 📌 Vazifasi: Ko‘rsatilgan qiymatning birinchi uchraganini o‘chiradi

# 5️⃣ del
# del a[2]


# 📌 Vazifasi: Index bo‘yicha elementni o‘chiradi

# 6️⃣ pop()
# a.pop(3)


# 📌 Vazifasi: Index bo‘yicha elementni o‘chiradi va qaytaradi
# ⚠️ Agar index bermasang — oxirgisini o‘chiradi

# 7️⃣ insert()
# a.insert(2, 'limmon')


# 📌 Vazifasi: Ko‘rsatilgan indexga element qo‘shadi

# 8️⃣ index()
# a.index('banana')


# 📌 Vazifasi: Element qaysi indexda turganini qaytaradi
# ⚠️ Faqat birinchi uchraganini

# 9️⃣ count()
# a.count('banana')


# 📌 Vazifasi: Element listda necha marta borligini sanaydi

# 🔟 reverse()
# a.reverse()


# 📌 Vazifasi: Listni teskari aylantiradi
# ⚠️ Original list o‘zgaradi

# 1️⃣1️⃣ sort()
# a.sort()


# 📌 Vazifasi: Listni A → Z tartibda saralaydi

# a.sort(reverse=True)


# 📌 Vazifasi: Z → A tartibda saralaydi

# 1️⃣2️⃣ sorted()
# b = sorted(a, reverse=True)


# 📌 Vazifasi: Listni saralaydi lekin original listni o‘zgartirmaydi

# 1️⃣3️⃣ clear()
# a.clear()


# 📌 Vazifasi: List ichini butunlay tozalaydi

# 🔢 Sonlar bilan ishlash
# num = [5, 2, 9, 1, 5, 6]

# sum()
# sum(num)


# 📌 Vazifasi: Barcha sonlar yig‘indisi → 28

# min()
# min(num)


# 📌 Vazifasi: Eng kichik son → 1

# max()
# max(num)


# 📌 Vazifasi: Eng katta son → 9

# 📏 len()
# fruits = ['apple', 'banana', 'cherry']
# len(fruits)


# 📌 Vazifasi: List uzunligini (elementlar sonini) qaytaradi → 3

# Topshiriq
# 1 - masala

# fruits = ["apple","banana","oranga"]
# if len(fruits) == 0:
#   print("Ro'yhat bo'sh")
# else:
#   print(len(fruits))

# 2 - masala

# fruit = ["aplle",'banana',"oranga"]
# if 'banana' in fruit:
#   print("Banan mavjud")
# else:
#   print("banaan mavjud emas")

# 3 - masala

# numbers = [1,2,3,5,6,7,8,9,10,34,56]
# print(max(numbers))
# print(min(numbers))

# if max(numbers)  > 10:
#   print("Katta son bor")
# else:
#   print("Katta son yoq")

# 4 - masala

# test = ['wer',"aplle","qwerty","hello","world"]

# if len(test) >= 5:
#   test.insert(2, 'limmon')
# else:
#   test.append("limmon")
# print(test)

# 5 - masala

# fruit = ["banana","apple","banana","orange"]

# if fruit.count("banana") >= 2:
#   print("Ko'p banana")
# else:
#   print("Kam banana")

# 6 - masala

# numbers = [3, 1, 5, 2, 9]

# if len(numbers) == 0:
#     print("Saralash mumkin emas")
# else:
#     numbers.sort(reverse=True)
#     print(numbers)

# 7 - masala

# numbers = [3, 1, 5, 2, 9]

# if sum(numbers) % 2 == 0:
#     print("Yig'indi juft son")
# else:
#     print("Yig'indi toq son")

# 8 - masala

# numbers = [10, 20, 30, 40, 50]

# index = int(input("Indeks kiriting: "))

# if 0 <= index < len(numbers):
#     numbers.pop(index)
#     print(numbers)
# else:
#     print("Noto'g'ri indeks")

# 9 - masala

# fruits = ["apple","banan","orange","limone"]

# if "apple" in fruits:
#   fruits[fruits.index("apple")] = "green apple"
# else:
#   fruits.insert(0,"apple")
# print(fruits)
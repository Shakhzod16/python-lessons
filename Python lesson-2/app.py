# for — ketma-ketlikdagi (list, tuple, string, range) elementlarni birma-bir aylanib chiqish uchun ishlatiladi.

# 1️⃣ Eng oddiy misol (range)
# for i in range(5):
#     print(i)


# 👉 Natija:

# 0
# 1
# 2
# 3
# 4


# 📌 range(5) → 0 dan 4 gacha sonlar beradi.

# 2️⃣ List bilan for
# mevalar = ["olma", "banan", "anor"]

# for meva in mevalar:
#     print(meva)


# 👉 Natija:

# olma
# banan
# anor


# 📌 List ichidagi har bir element olinadi.

# 3️⃣ String (matn) bilan
# ism = "Shahzod"

# for harf in ism:
#     print(harf)


# 👉 Natija:

# S
# h
# a
# h
# z
# o
# d


# 📌 Matndagi har bir harf alohida chiqadi.

# 4️⃣ range(start, stop, step)
# for i in range(1, 10, 2):
#     print(i)


# 👉 Natija:

# 1
# 3
# 5
# 7
# 9


# 📌 step=2 → 2 qadam bilan oshadi.

# 5️⃣ Yig‘indi hisoblash (juda muhim)
# sonlar = [3, 5, 7]
# yigindi = 0

# for son in sonlar:
#     yigindi += son

# print(yigindi)


# 👉 Natija:

# 15

# 6️⃣ if bilan birga ishlatish
# sonlar = [1, 2, 3, 4, 5, 6]

# for son in sonlar:
#     if son % 2 == 0:
#         print(son, "juft")


# 👉 Natija:

# 2 juft
# 4 juft
# 6 juft

# 7️⃣ Indeks bilan ishlash (range + len)
# ismlar = ["Ali", "Vali", "Hasan"]

# for i in range(len(ismlar)):
#     print(i, ismlar[i])


# 👉 Natija:

# 0 Ali
# 1 Vali
# 2 Hasan

# 🔑 Qisqa xulosa

# for → aylanish uchun

# range() → sonlar ketma-ketligi

# List, string, tuple bilan ishlaydi

# Ko‘pincha if bilan birga ishlatiladi

# Topshiriqlar
# 1 - masala

# a = [3, -1, 0, 5, -7, 9, 2]

# count = 0
# for son in a:
#   if son > 0:
#     count +=1
# print(count)

# 2 - masala

# son = [1,2,0,4,6,87,90,123]
# maxNumber = son[0]
# minNumber = son[0]

# for son1 in son:
#   if son1 > maxNumber:
#     maxNumber = son1
#   if son1 < minNumber:
#     minNumber = son1
# print("eng katta son",maxNumber)
# print("eng kichik son",minNumber)

# 3 - masala

# text = "Python sikl operatorlari juda muhim"
# count = 0
# for boshjoy in text:
#   if boshjoy == " ":
#      count += 1
# print(count)

# 4 - masala

# a = [1, 4, 7, 10, 13, 18, 21]
# son = []
# for yangi in a:
#   if yangi % 2 == 0:
#    son.append(yangi)
# print(son)

# 5 - masala

# soz = "salom"
# teskari = ''
# for yangi in soz:
#   teskari = yangi + teskari
# print(teskari)

# 6 - masala

# lists = [1, 2, 3, 4, 2]
# for birxil in lists:
#   if lists.count(birxil) > 1:
#    print(birxil)

# 7 - masala

# a = ["ali","vali","dilbek","shoxjahon","miron"]
# engUzun = ''
# for yangi in a:
#   if len(yangi)>len(engUzun):
#     engUzun = yangi
# print(engUzun)

# 8 - masala

# a = [12, 105, 7, 999, 45, 1000, 321]
# uchxona = []
# for ynagi in a:
#   if 100 <= ynagi <= 999:
#     uchxona.append(ynagi)
# print(uchxona)

# 10 - masala

# words = ["alla", "olma", "ikki", "kiyik", "python"]

# palindrom = []

# for x in words:
#     if x == "".join(reversed(x)):
#         palindrom.append(x)

# print(palindrom)


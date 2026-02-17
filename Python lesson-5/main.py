# from adds import greeting
# from module import greeting
# from math import sin
# from . import adds

# greeting()



# a = open('text.txt','r')
# print(a)


# b = open('www.txt','a')

# with open('text.txt','a') as a:
#     # print(a.read())
#     # a.write('hello')
#     a.write('world')




# # Foydalanuvchidan matn olish
# matn = input("Matn kiriting: ")

# # Faylga yozish (fayl bo'lmasa yaratiladi)
# with open("matn.txt", "w", encoding="utf-8") as fayl:
#     fayl.write(matn)

# print("Matn faylga yozildi.")


# with open("matn.txt", "r", encoding="utf-8") as fayl:
#     matn = fayl.read()

# print("Fayldagi matn:")
# print(matn)



# with open("matn.txt", "r", encoding="utf-8") as fayl:
#     qatorlar = fayl.readlines()

# print("Qatorlar soni:", len(qatorlar))




# with open("matn.txt", "r", encoding="utf-8") as fayl:
#     matn = fayl.read()

# sozlar = matn.split()
# print("So'zlar soni:", len(sozlar))



# # 10 ta son yozish
# with open("sonlar.txt", "w") as fayl:
#     for i in range(10):
#         son = int(input(f"{i+1}-sonni kiriting: "))
#         fayl.write(str(son) + "\n")

# # Yig'indini hisoblash
# yigindi = 0
# with open("sonlar.txt", "r") as fayl:
#     for qator in fayl:
#         yigindi += int(qator.strip())

# print("Yig'indi:", yigindi)







# with open("sonlar.txt", "r") as fayl:
#     sonlar = [int(qator.strip()) for qator in fayl]

# eng_katta = max(sonlar)
# print("Eng katta son:", eng_katta)






# with open("matn.txt", "r", encoding="utf-8") as asl:
#     malumot = asl.read()

# with open("nusxa.txt", "w", encoding="utf-8") as nusxa:
#     nusxa.write(malumot)

# print("Fayl nusxasi yaratildi.")




# with open("sonlar.txt", "r") as fayl:
#     sonlar = [int(qator.strip()) for qator in fayl]

# with open("juft.txt", "w") as juft_fayl:
#     for son in sonlar:
#         if son % 2 == 0:
#             juft_fayl.write(str(son) + "\n")

# print("Juft sonlar juft.txt fayliga yozildi.")





# with open("talabalar.txt", "r", encoding="utf-8") as fayl:
#     talabalar = fayl.readlines()

# # Bo'sh joylarni olib tashlash
# talabalar = [talaba.strip() for talaba in talabalar]

# # Saralash
# talabalar.sort()

# with open("sorted.txt", "w", encoding="utf-8") as fayl:
#     for talaba in talabalar:
#         fayl.write(talaba + "\n")

# print("Talabalar alifbo tartibida sorted.txt fayliga yozildi.")





# with open("matn.txt", "r", encoding="utf-8") as fayl:
#     matn = fayl.read()

# sozlar = matn.split()
# eng_uzun = max(sozlar, key=len)

# print("Eng uzun so'z:", eng_uzun)
# print("Uzunligi:", len(eng_uzun))


# Masalalar

# 11-masala. Fayl oxiriga matn qo‘shish
# Shart:
# Foydalanuvchi kiritgan matnni matn.txt faylining oxiriga qo‘shadigan dastur tuzing.
# Talablar:
# Eski ma’lumotlar o‘chib ketmasligi kerak.
# Yangi matn yangi qatordan boshlansin.

# matn = input("Matn kiriting: ")
# with open("matn.txt", "a", encoding="utf-8") as fayl:
#     fayl.write("\n" + matn)

# print("Matn fayl oxiriga qo‘shildi.")



# 12-masala. Fayldagi belgilar sonini hisoblash
# Shart:
# matn.txt faylidagi barcha belgilar (probel bilan birga) sonini aniqlang.

# with open("matn.txt", "r", encoding="utf-8") as fayl:
#     matn = fayl.read()

# print("Belgilar soni:", len(matn))



# 13-masala. Fayldagi faqat katta harflarni chiqarish
# Shart:
# matn.txt faylidan faqat katta harflarni ajratib, ekranga chiqaring.
# Masalan:
# Salom Dunyo
# Natija: SD

# with open("matn.txt", "r", encoding="utf-8") as fayl:
#     matn = fayl.read()

# katta_harflar = ""

# for belgi in matn:
#     if belgi.isupper():
#         katta_harflar += belgi

# print("Natija:", katta_harflar)



# 14-masala. Fayldagi qatorlarni teskari tartibda chiqarish
# Shart:
# matn.txt faylidagi qatorlarni teskari tartibda ekranga chiqaring.

# with open("matn.txt", "r", encoding="utf-8") as fayl:
#     qatorlar = fayl.readlines()

# for qator in reversed(qatorlar):
#     print(qator.strip())



# 15-masala. Fayldagi sonlarning o‘rtacha qiymatini topish
# Shart:
# sonlar.txt faylida berilgan sonlarning o‘rtacha arifmetik qiymatini hisoblang.
# Formula:
# 𝑜
# ‘
# 𝑟
# 𝑡
# 𝑎
# 𝑐
# ℎ
# 𝑎
# =
# 𝑦
# 𝑖
# 𝑔
# ‘
# 𝑖
# 𝑛
# 𝑑
# 𝑖
# /
# 𝑠
# 𝑜
# 𝑛
# 𝑙
# 𝑎
# 𝑟
# _
# 𝑠
# 𝑜
# 𝑛
# 𝑖
# o‘rtacha=yig‘indi/sonlar_soni

# with open("sonlar.txt", "r") as fayl:
#     sonlar = fayl.read().split()

# sonlar = [float(son) for son in sonlar]

# orta = sum(sonlar) / len(sonlar)

# print("O‘rtacha qiymat:", orta)



# 16-masala. Fayldagi toq sonlarni yangi faylga yozish
# Shart:
# sonlar.txt faylidagi toq sonlarni toq.txt fayliga yozing.

# with open("sonlar.txt", "r") as fayl:
#     sonlar = fayl.read().split()

# with open("toq.txt", "w") as yangi_fayl:
#     for son in sonlar:
#         if int(son) % 2 != 0:
#             yangi_fayl.write(son + "\n")

# print("Toq sonlar toq.txt fayliga yozildi.")



# 17-masala. Fayldagi eng qisqa so‘zni topish
# Shart:
# matn.txt faylidagi eng qisqa so‘zni toping.


# with open("matn.txt", "r", encoding="utf-8") as fayl:
#     sozlar = fayl.read().split()

# eng_qisqa = min(sozlar, key=len)

# print("Eng qisqa so‘z:", eng_qisqa)




# 18-masala. Fayldagi har bir qator boshiga raqam qo‘shish
# Shart:
# matn.txt faylidagi har bir qator boshiga tartib raqamini qo‘shib, raqamli.txt fayliga yozing.
# Masalan:
# Ali
# Vali
# Sami
# Natija:
# 1. Ali
# 2. Vali
# 3. Sami

with open("matn.txt", "r", encoding="utf-8") as fayl:
    qatorlar = fayl.readlines()

with open("raqamli.txt", "w", encoding="utf-8") as yangi_fayl:
    for i, qator in enumerate(qatorlar, start=1):
        yangi_fayl.write(f"{i}. {qator}")

print("Raqamli fayl yaratildi.")



# 19-masala. Ikki faylni birlashtirish
# Shart:
# file1.txt va file2.txt fayllarini o‘qib, ularni result.txt fayliga birlashtiring.




# 20-masala. Faylda berilgan so‘zni qidirish
# Shart:
# Foydalanuvchi bir so‘z kiritsin. Shu so‘z matn.txt faylida necha marta uchrashini aniqlang.
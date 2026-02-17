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

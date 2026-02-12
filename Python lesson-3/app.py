# i=0
# while i<10:
#     print(i)
#     i += 1

# while True:
#     print("This will run forever.")


# while True:
#     a = input("Enter 'exit' to stop the loop: ")
#     if a=='exit':
#         break
#     elif a=='skip':
#         continue
#     else:
#         print("You entered:", a)

# Masalalar

# 1 - masala

# ismlar = [ "Ali", "Nodira", "Sardor", "Olim", "Muhammad"]

# uzun_ismlar = []

# for ism in ismlar:
#     if len(ism) > 5:
#         uzun_ismlar.append(ism)

# print(uzun_ismlar)

# 2 - masala

# Dict yani Object

# a = {
#     'name': 'Alice',
#     'age': 30,
#     'city': 'New York'
# }

# print(a.keys())
# print(a.values())
# print(a.items())

# a['balance'] = 1000
# print(a)

# print(a['namee'])  # Output: Alice
# print(a.get('agee'))  # Output: 30

a = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}



for b,c in a.items():
    print(f"{b}: {c}")

# Masalalar

# 1-masala: Onlayn do‘kon buyurtmalari
def hisobla(*args, **kwargs):
    jami = sum(args)

    chegirma = kwargs.get("chegirma", 0)
    yetkazib_berish = kwargs.get("yetkazib_berish", 0)
    soliq = kwargs.get("soliq", 0)

    # chegirma
    jami -= jami * chegirma / 100

    # soliq
    jami += jami * soliq / 100

    # yetkazib berish
    jami += yetkazib_berish

    return jami


# 🔹 Misol:

print(hisobla(100000, 50000, chegirma=10, soliq=12, yetkazib_berish=20000))

# 2-masala: Kino bron qilish tizimi
def bron_qilish(*args, **kwargs):
    narxlar = {
        "oddiy": 30000,
        "vip": 50000,
        "premium": 70000
    }

    soni = kwargs.get("soni", 1)
    popkorn = kwargs.get("popkorn", False)
    ichimlik = kwargs.get("ichimlik", False)

    jami = 0

    for chipta in args:
        jami += narxlar.get(chipta, 0) * soni

    if popkorn:
        jami += 15000

    if ichimlik:
        jami += 10000

    return jami


# 🔹 Misol:

print(bron_qilish("vip", "oddiy", soni=2, popkorn=True, ichimlik=True))

# 3-masala: Xodimlar baholash tizimi
def bahola(*args, **kwargs):
    ball = 100

    # bajarilgan ishlar
    ball += len(args) * 5

    kechikish = kwargs.get("kechikish", 0)
    jarima = kwargs.get("jarima", 0)

    ball -= kechikish * jarima

    return ball


# 🔹 Misol:

print(bahola("hisobot", "loyiha", "prezentatsiya", kechikish=2, jarima=5))

# 4-masala: O‘yin hisoblash tizimi
def oyin_hisobla(*args, **kwargs):
    jami = sum(args)

    bonus = kwargs.get("bonus", 0)
    level = kwargs.get("level", 1)

    if level >= 5:
        bonus *= 2

    return jami + bonus


# 🔹 Misol:

print(oyin_hisobla(50, 70, 100, bonus=20, level=5))

# 5-masala: Restoran buyurtmasi
def buyurtma(*args, **kwargs):
    taomlar = {
        "osh": 40000,
        "somsa": 10000,
        "shashlik": 25000,
        "manti": 30000
    }

    jami = 0
    for taom in args:
        jami += taomlar.get(taom, 0)

    xizmat_haqi = kwargs.get("xizmat_haqi", 0)
    choychaqa = kwargs.get("choychaqa", 0)

    jami += jami * xizmat_haqi / 100
    jami += choychaqa

    return jami


# 🔹 Misol:

print(buyurtma("osh", "somsa", "shashlik", xizmat_haqi=10, choychaqa=5000))

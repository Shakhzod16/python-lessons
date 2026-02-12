# 1️⃣ capitalize()
# a = 'Hello world '
# print(a.capitalize())


# 👉 Faqat birinchi harfni katta, qolganini kichik qiladi.
# Natija: "Hello world "

# 2️⃣ lower()
# print(a.lower())


# 👉 Barcha harflarni kichik qiladi.
# Natija: "hello world "

# 3️⃣ count('o')
# print(a.count('o'))


# 👉 Belgini necha marta qatnashganini sanaydi.
# Bu yerda "o" harfi 2 marta bor.

# 4️⃣ encode()
# print(a.encode())


# 👉 Matnni byte (kodlangan) ko‘rinishga o‘tkazadi.
# Natija: b'Hello world '

# Bu internet yoki fayl bilan ishlaganda kerak bo‘ladi.

# 5️⃣ endswith(' ')
# print(a.endswith(' '))


# 👉 Satr oxiri berilgan belgiga tengmi?
# Bu yerda oxiri bo‘sh joy bilan tugaydi → True

# 6️⃣ expandtabs()
# txt = "H\te\tl\tl\to"
# print(txt.expandtabs())


# 👉 \t (tab) ni oddiy bo‘sh joyga aylantiradi.

# 7️⃣ find("e")
# x = txt.find("e")


# 👉 Belgining birinchi indeksini qaytaradi.
# Agar topilmasa → -1

# 8️⃣ index("e",4,10)
# x = txt.index("e",4,10)


# 👉 find() kabi, lekin topilmasa xatolik beradi.
# Bu yerda 4–10 indeks oralig‘ida qidiradi.

# 9️⃣ isnumeric()
# txt = "565543"
# print(txt.isnumeric())


# 👉 Faqat raqamlardan iboratmi?
# Natija: True

# 🔟 join()
# myTuple = ("John", "Peter", "Vicky")
# x = ",".join(myTuple)


# 👉 Elementlarni birlashtiradi.
# Natija: "John,Peter,Vicky"

# 1️⃣1️⃣ rstrip()
# txt = "     banana     "
# print(txt.rstrip())


# 👉 O‘ng tomondagi bo‘sh joylarni o‘chiradi.

# 1️⃣2️⃣ maketrans() + translate()
# txt = "Hello Sam!S"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))


# 👉 Belgilarni almashtirish jadvali yaratadi.
# Bu yerda "S" → "P" ga almashadi.

# Natija: "Hello Pam!P"

# 1️⃣3️⃣ replace("bananas", "apples", 1)
# x = txt.replace("bananas", "apples",1)


# 👉 Faqat 1 marta almashtiradi.
# Natija: "I apples like bananas"

# 1️⃣4️⃣ rfind("casa")
# x = txt.rfind("casa")


# 👉 So‘zni oxiridan boshlab qidiradi.
# Oxirgi indeksni beradi.

# 1️⃣5️⃣ split(",")
# x = txt.split(",")


# 👉 Vergul bo‘yicha bo‘lib beradi.
# Natija: ['welcome', 'to', 'the', 'jungle']

# 1️⃣6️⃣ splitlines()
# txt = "Thank you...\nWelcome..."
# x = txt.splitlines()


# 👉 Yangi qatordan (\n) bo‘yicha ajratadi.

# 1️⃣7️⃣ title()
# print(txt.title())


# 👉 Har bir so‘zning birinchi harfini katta qiladi.

# 1️⃣8️⃣ translate(mydict)
# mydict = {83: 80}
# txt = "Hello Sam!"
# print(txt.translate(mydict))


# 👉 ASCII kodi bo‘yicha almashtiradi.
# 83 → "S"
# 80 → "P"

# 1️⃣9️⃣ zfill(6)
# txt = "50"
# print(txt.zfill(6))


# 👉 Chap tomondan 0 qo‘shadi.
# Natija: "000050"

# Bu ko‘pincha ID yoki hisob raqamlarida ishlatiladi.


# Masalalar


# 🟢 1-masala. Asosiy metodlar

matn = input("Satr kiriting: ")

print("Uzunligi:", len(matn))
print("Katta harflarda:", matn.upper())
print("Kichik harflarda:", matn.lower())

if len(matn) > 0:
    print("Birinchi belgi:", matn[0])
    print("Oxirgi belgi:", matn[-1])
else:
    print("Satr bo'sh")

# 🟢 2-masala. Bo‘sh joylar bilan ishlash

matn = input("Satr kiriting: ")

tozalangan = matn.strip()
yangi = " ".join(tozalangan.split())

print("Natija:", yangi)

# 🟢 3-masala. So‘zlarni sanash

matn = input("Satr kiriting: ")

sozlar = matn.split()
belgilar = matn.replace(" ", "")

print("So‘zlar soni:", len(sozlar))
print("Belgilar soni (bo'sh joysiz):", len(belgilar))

# 🟢 4-masala. Qidirish

matn = input("Satr kiriting: ")
soz = input("Qidiriladigan so‘z: ")

if soz in matn:
    print("Topildi")
else:
    print("Topilmadi")

# 🟢 5-masala. Almashtirish

matn = input("Satr kiriting: ")

yangi = matn.replace("a", "@")
print("Natija:", yangi)

# 🟡 6-masala. Satrni tekshirish\

matn = input("Satr kiriting: ")

print("Faqat harflar:", matn.isalpha())
print("Faqat raqamlar:", matn.isdigit())
print("Faqat katta harflar:", matn.isupper())

# 🟡 7-masala. Login tekshiruvi

login = input("Login kiriting: ")

if (
    len(login) >= 8
    and not login.isspace()
    and login.isalnum()
):
    print("Login qabul qilindi")
else:
    print("Login noto‘g‘ri")

# 🟡 8-masala. So‘zlarni teskari qilish

matn = input("Satr kiriting: ")

sozlar = matn.split()
teskari = [soz[::-1] for soz in sozlar]

natija = " ".join(teskari)
print("Natija:", natija)

# 🔵 9-masala. Palindrom

soz = input("So‘z kiriting: ")

if soz.lower() == soz.lower()[::-1]:
    print("Palindrom")
else:
    print("Palindrom emas")

# 🔵 10-masala. Murakkab tahlil

matn = input("Satr kiriting: ")

katta = 0
kichik = 0
raqam = 0
maxsus = 0

for belgi in matn:
    if belgi.isupper():
        katta += 1
    elif belgi.islower():
        kichik += 1
    elif belgi.isdigit():
        raqam += 1
    else:
        maxsus += 1

print("Katta harflar:", katta)
print("Kichik harflar:", kichik)
print("Raqamlar:", raqam)
print("Maxsus belgilar:", maxsus)

# 🔵 11-masala. Matnni formatlash

matn = input("Gap kiriting: ")

sozlar = matn.split()
yangi = [soz.capitalize() for soz in sozlar]

print(" ".join(yangi))

# 🔴 12-masala. Email tekshiruvi

email = input("Email kiriting: ")

if (
    "@" in email
    and "." in email
    and not email.isspace()
):
    print("Email to‘g‘ri")
else:
    print("Email noto‘g‘ri")

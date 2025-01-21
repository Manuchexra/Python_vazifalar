import math
#1-masala
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")

toliq_ism = ism + " " + familiya
print("To‘liq ism:", toliq_ism)

#2-masala
ism = input("Ismingizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")

print(f"Sizning ismingiz {ism}, yoshingiz {yosh}.")

#3-masala
matn = input("Matn kiriting: ")

print("Katta harflarda:", matn.upper())
print("Kichik harflarda:", matn.lower())
print("Sarlavha usulida:", matn.title())
print("Birinchi harfi katta qilib:", matn.capitalize())

#4-masala
matn = input("Boshliqlar bilan matn kiriting: ")

print("Bo'shliqlarsiz matn:", matn.strip())
print("Chap bo'shliqlarsiz matn:", matn.lstrip())
print("O'ng bo'shliqlarsiz matn:", matn.rstrip())

#5-masala
ism = input("Ismingizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")
rang = input("Sevimli rangingizni kiriting: ")
print(f"Salom, {ism}. Siz {yosh} yoshdasiz va sizning sevimli rangingiz {rang}.")

#6-masala
ism_kichik = input("Ismingizni kichik harflarda kiriting: ")
print("Katta harflarda:", ism_kichik.upper())
print("To'liq formatlangan:", ism_kichik.capitalize())

#7-masala
son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
print("Qo'shish:", son1 + son2)
print("Ayirish:", son1 - son2)
print("Ko'paytirish:", son1 * son2)
print("Bo'lish:", son1 / son2)
print("Darajaga ko'tarish:", son1 ** son2)

#8-masala
float1 = float(input("1-float sonni kiriting: "))
float2 = float(input("2-float sonni kiriting: "))
print("Bo'lish:", float1 / float2)
print("Darajaga kotarish:", float1 ** float2)

#9-masala
malumot = input("Biror ma'lumot kiriting: ")
print("Kiritilgan qiymat turi:", type(malumot))

#10-masala
son1 = input("1-sonni kiriting: ")
son2 = input("2-sonni kiriting: ")
string_qoshish = son1 + son2
print("String sifatida qo'shish:", string_qoshish)
integer_qoshish = int(son1) + int(son2)
print("Integer sifatida qo'shish:", integer_qoshish)

#11-masala
son = int(input("Biror son kiriting: "))
print("Son 10 dan katta:", son > 10)

#12-masala
son1 = int(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting (floatga o'tkaziladi): "))
natija = son1 + son2
print("Natija (float):", natija)
print("Natija (integer):", int(natija))

#13-masala
son = int(input("Biror son kiriting: "))
juft = son % 2 == 0
print("Son juft:", juft)
print("Son toq:", not juft)

#14-masala
uzunlik = float(input("To'rtburchakning uzunligini kiriting: "))
eni = float(input("To'rtburchakning enini kiriting: "))
perimetr = 2 * (uzunlik + eni)
yuza = uzunlik * eni
print("Perimetr:", perimetr)
print("Yuza:", yuza)

#15-masala
radius = float(input("Aylanani radiusini kiriting: "))
pi = 3.14
uzunlik = 2 * pi * radius
yuza = pi * radius**2
print("Aylanani uzunligi:", uzunlik)
print("Aylanani yuza:", yuza)

#16-masala
price1 = float(input("1-mahsulot narxini kiriting (float): "))
price2 = float(input("2-mahsulot narxini kiriting (float): "))
if price1 < price2:
    print("1-mahsulot arzonroq.")
elif price1 > price2:
    print("2-mahsulot arzonroq.")
else:
    print("Ikkala mahsulot narxi teng.")

#17-masala
num1 = float(input("1-sonni kiriting (float): "))
num2 = float(input("2-sonni kiriting (float): "))
num3 = float(input("3-sonni kiriting (float): "))
average = (num1 + num2 + num3) / 3
print(f"Uchta sonning o'rtacha qiymati: {average}")

#18-masala
number = float(input("Musbat son kiriting (float): "))
if number < 0:
    print("Iltimos, faqat musbat son kiriting!")
else:
    sqrt_result = math.sqrt(number)
    print(f"{number} sonining kvadrat ildizi: {sqrt_result}")
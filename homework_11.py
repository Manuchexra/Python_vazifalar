#1-masala
age = int(input("Yoshingizni kiriting: "))
if age >= 18:
    print("Voyaga yetgan")
else:
    print("Voyaga yetmagan")

#2-masala
grade = int(input("Olgan bahoyingizni kiriting (2-5): "))
if grade == 5:
    print("A'lo")
elif grade == 4:
    print("Yaxshi")
elif grade == 3:
    print("Qoniqarli")
elif grade == 2:
    print("Qoniqarsiz")
else:
    print("Noto'g'ri baho kiritildi")

#3-masala
month = int(input("Oy raqamini kiriting (1-12): "))
if month in [12, 1, 2]:
    print("Qish fasli")
elif month in [3, 4, 5]:
    print("Bahor fasli")
elif month in [6, 7, 8]:
    print("Yoz fasli")
elif month in [9, 10, 11]:
    print("Kuz fasli")
else:
    print("Noto'g'ri oy raqami kiritildi")

#4-masala
temperature = float(input("Havoning haroratini kiriting: "))
if temperature > 30:
    print("Havo issiq")
elif 20 <= temperature <= 30:
    print("Havo iliq")
elif temperature < 15:
    print("Havo sovuq")

#5-masala
days_expired = int(input("Hujjat amal qilish muddati (kun): "))
if days_expired > 5:
    print("Hujjat amal qilish muddati tugagan")
else:
    print("Hujjat amal qilish muddati hali tugamagan")

#6-masala
payment_method = input("To'lov usulini kiriting (naqd/karta): ").lower()
if payment_method == "naqd":
    amount = float(input("Summani kiriting: "))
    print(f"Naqd to'lov summasi: {amount}")
elif payment_method == "karta":
    password = input("Parolni kiriting: ")
    print("Karta to'lovi muvaffaqiyatli")
else:
    print("Noto'g'ri to'lov usuli kiritildi")

#7-masala
score = int(input("Baho kiriting: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

#8-masala
age = int(input("Yoshingizni kiriting: "))
if age >= 18:
    print("Kattalar")
else:
    print("Bolalar")

#9-masala
weather = input("Ob-havo haqida ma'lumot (yomg'ir/qor/yaxshi): ").lower()
if weather in ["yomg'ir", "qor"]:
    print("Ko'ylak kiyma")
else:
    print("Ob-havo yaxshi")

#10-masala
payment_type = input("To'lov turini tanlang (naqd/karta): ").lower()
if payment_type == "naqd":
    print("Naqd to'lov tanlandi")
elif payment_type == "karta":
    print("Karta to'lovi tanlandi")
else:
    print("Noto'g'ri to'lov turi")

#11-masala
score = int(input("Baho kiriting: "))
if score > 70:
    print("Sertifikat olishingiz mumkin")
else:
    print("Sertifikat olish uchun yetarli baho emas")

#12-masala
month = int(input("Oy raqamini kiriting (1-12): "))
if month in [12, 1, 2]:
    print("Qish")
elif month in [3, 4, 5]:
    print("Bahor")
elif month in [6, 7, 8]:
    print("Yoz")
elif month in [9, 10, 11]:
    print("Kuz")
else:
    print("Noto'g'ri oy raqami")

#13-masala
grades = list(map(int, input("3 ta bahoni kiriting (bo'sh joy bilan ajratib): ").split()))
average = sum(grades) / len(grades)
if average >= 70:
    print("Yaxshi")
elif 50 <= average < 70:
    print("O'rtacha")
else:
    print("Yomon")

#14-masala
food = input("Qaysi taomni xohlaysiz? ")
print("Tayyorlashga kirishamiz")

#15-masala
car_age = int(input("Avtomobil yoshi: "))
mileage = int(input("Avtomobil yurgan masofa (km): "))
if car_age > 10:
    print("Ehtiyot qismlarni tekshiring")
else:
    print("Avtomobil yaxshi holatda")

#16-masala
age = int(input("Yosh: "))
gender = input("Jins (erkak/ayol): ").lower()
if gender == "erkak":
    if age < 18:
        print("Futbolka tavsiya etiladi")
    else:
        print("Soat sovg'a qiling")
elif gender == "ayol":
    if age < 18:
        print("Sumka sovg'a qiling")
    else:
        print("Zargarlik buyumlari tavsiya etiladi")

#17-masala
points = int(input("Ball kiriting: "))
if points > 100:
    print("Reytingni yangilang")
else:
    print("Reyting saqlanmoqda")

#18-masala
time = int(input("Soatni kiriting (0-23): "))
if 0 <= time < 6:
    print("Xayrli tun")
elif 6 <= time < 18:
    print("Xayrli kun")
else:
    print("Xayrli kech")

#19-masala
password = input("Parolni kiriting: ")
if len(password) < 8:
    print("Parolni kuchaytiring")
else:
    print("Parol qabul qilindi")

#20-masala
income = int(input("Daromadingizni kiriting: "))
debt = int(input("Qarzingizni kiriting: "))
if income > debt:
    print("Kredit olish mumkin")
else:
    print("Kredit olish shartlari bajarilmagan")

#21-masala
age = int(input("Yoshingizni kiriting: "))
if age < 10:
    print("Suzish")
elif 10 <= age < 18:
    print("Futbol")
else:
    print("Yugurish")

#22-masala
weight = float(input("Vazningizni kiriting (kg): "))
height = float(input("Bo'yingizni kiriting (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Ozish")
elif 18.5 <= bmi < 24.9:
    print("Normal")
elif 25 <= bmi < 29.9:
    print("Ortiqcha vazn")
else:
    print("Semizlik")

#23-masala
plan = input("Yozgi ta'til uchun rejangiz bormi? (ha/yo'q): ").lower()
if plan == "ha":
    print("Yozda sayohatga chiqamiz")
else:
    print("Yozda dam olamiz")

#24-masala
tasks = int(input("Bajarilgan ishlar sonini kiriting: "))
if tasks > 5:
    print("Yaxshi natija")
else:
    print("Ko'proq ishlash kerak")

#25-masala
book = input("Kitob nomini kiriting: ").lower()
famous_books = ["harry potter", "hobbit", "ulysses", "war and peace"]
if book in famous_books:
    print("Buni o'qiganman")
else:
    print("Buni o'qish kerak")

#26-masala
team = input("Sevimli futbol jamoangizni kiriting: ")
winner_teams = ["Real Madrid", "Barcelona", "Bayern Munich"]
if team in winner_teams:
    print("Tabriklaymiz!")
else:
    print("Yaxshi jamoa")

#27-masala
income = int(input("Daromadni kiriting: "))
expenses = int(input("Xarajatlarni kiriting: "))
if income > expenses:
    print("Foyda")
else:
    print("Zarar")

#28-masala
experience = int(input("Ish tajribangiz (yillar): "))
if experience < 2:
    print("Yosh mutaxassis")
else:
    print("Tajribali mutaxassis")

#29-masala
result = int(input("Ish natijasini baholang (1-10): "))
if result > 8:
    print("Mukammal")
elif 5 <= result <= 8:
    print("Yaxshi")
else:
    print("Qoniqarli")

#30-masala
value = int(input("Mahsulot narxini kiriting ($): "))
if value > 100:
    print("Boj to'lashingiz kerak")
else:
    print("Boj to'lash shart emas")

#31-masala
age = int(input("Yoshingizni kiriting: "))
weight = int(input("Vazningizni kiriting (kg): "))
if age >= 18 and weight >= 50:
    print("Uchishingiz mumkin")
else:
    print("Uchish mumkin emas")

#32-masala
temperature = float(input("Haroratni kiriting: "))
if temperature < 0:
    print("Qishda qizish")
else:
    print("Harorat normal")

#33-masala
preparation = input("Maktabga tayyormisiz? (ha/yo'q): ").lower()
if preparation == "ha":
    print("Maktabga borishga tayyormiz")
else:
    print("Ko'proq o'qish kerak")

#34-masala
preparation = input("Maktabga tayyormisiz? (ha/yo'q): ").lower()
if preparation == "ha":
    print("Maktabga borishga tayyormiz")
else:
    print("Ko'proq o'qish kerak")

#35-masala
preparation = int(input("Dars tayyorgarligi darajasi (1-100): "))
if preparation >= 70:
    print("Tayyor")
else:
    print("Boshqa darslar oling")

#36-masala
friends = int(input("Do'stlaringiz sonini kiriting: "))
if friends < 5:
    print("Do'stlar orttirishingiz mumkin")
else:
    print("Yaxshi do'stlar soni")

#37-masala
number = int(input("Sonni kiriting: "))
if number > 0:
    print("Musbat son")
elif number < 0:
    print("Manfiy son")
else:
    print("Bu nol")

#38-masala
number = int(input("Sonni kiriting: "))
if number % 2 == 0:
    print("Juft son")
else:
    print("Toq son")

#39-masala
age = int(input("Yoshingizni kiriting: "))
if 0 <= age <= 12:
    print("Bolalar guruhiga kiradi")
elif 13 <= age <= 19:
    print("Yoshlar guruhiga kiradi")
else:
    print("Kattalar guruhiga kiradi")

#40-masala
grade = int(input("Baho kiriting: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

#41-masala
month = int(input("Oy raqamini kiriting (1-12): "))
if month in [12, 1, 2]:
    print("Qish")
elif month in [3, 4, 5]:
    print("Bahor")
elif month in [6, 7, 8]:
    print("Yoz")
elif month in [9, 10, 11]:
    print("Kuz")
else:
    print("Noto'g'ri oy raqami")

#42-masala
a, b = map(int, input("Ikki sonni kiriting (bo'sh joy bilan ajratib): ").split())
if a > b:
    print(f"{a} katta")
elif a < b:
    print(f"{b} katta")
else:
    print("Ikkala son teng")

#43-masala
password = input("Parolni kiriting: ")
correct_password = "12345"
if password == correct_password:
    print("Parol to'g'ri")
else:
    print("Parol noto'g'ri")

#44-masala
letter = input("Harfni kiriting: ")
if letter.isupper():
    print("Katta harf")
elif letter.islower():
    print("Kichik harf")
else:
    print("Bu harf emas")

#45-masala
temperature = float(input("Havoning haroratini kiriting: "))
if temperature > 35:
    print("Juda issiq")
elif 20 <= temperature <= 35:
    print("Iliq")
elif 0 <= temperature < 20:
    print("Sovuq")
else:
    print("Juda sovuq")

#46-masala
country = input("Mamlakatingizni kiriting: ").lower()
if country == "o'zbekiston":
    print("Siz O'zbekistondasiz")
else:
    print(f"Siz {country} mamlakatidasiz")

#47-masala
height = int(input("Balandlikni kiriting (sm): "))
if height < 150:
    print("Qisqa")
elif 150 <= height < 180:
    print("O'rtacha")
else:
    print("Baland")

#48-masala
price = int(input("Kitob narxini kiriting: "))
if price < 50:
    print("Arzon")
elif 50 <= price <= 100:
    print("O'rtacha")
else:
    print("Qimmat")

#49-masala
level = input("Sport darajasini kiriting (yangi, o'rta, tajribali): ").lower()
if level == "yangi":
    print("Siz boshlovchisiz")
elif level == "o'rta":
    print("Siz tajriba orttirgan sportchisiz")
elif level == "tajribali":
    print("Siz tajribali sportchisiz")
else:
    print("Noto'g'ri daraja")

#50-masala
symptoms = input("Sog'liq belgilarini kiriting (isitma, yo'tal, bosh og'rig'i): ").lower()
if "isitma" in symptoms or "yo'tal" in symptoms:
    print("Doktorga murojaat qiling")
else:
    print("Sog'ligingiz yaxshi")

#51-masala
credit_score = int(input("Kredit balini kiriting: "))
if credit_score >= 70:
    print("Kredit olish uchun mos")
else:
    print("Kredit olish uchun mos emas")

#52-masala
order = input("Buyurtmangizni tanlang (kofe, choy, sharbat): ").lower()
if order in ["kofe", "choy", "sharbat"]:
    print(f"{order.title()} buyurtmangiz tayyorlanmoqda")
else:
    print("Mavjud emas")

#53-masala
speed = int(input("Avtomobil tezligini kiriting: "))
if speed > 60:
    print("Tezlikni oshirdingiz")
else:
    print("Tezlik normal")

#54-masala
vacation_time = input("Ta'tilni kiriting (yoz/qish): ").lower()
if vacation_time == "yoz":
    print("Yozgi ta'til")
elif vacation_time == "qish":
    print("Qishki ta'til")
else:
    print("Noto'g'ri ta'til vaqti")

#55-masala
school_grade = int(input("Maktab bahosini kiriting: "))
if school_grade > 4:
    print("Yuqori baho")
elif school_grade == 3 or school_grade == 4:
    print("O'rtacha baho")
else:
    print("Past baho")

#56-masala
value = input("Qiymatni kiriting: ")
if value.isdigit():
    print("Bu raqam")
else:
    print("Bu raqam emas")
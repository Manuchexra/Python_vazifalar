import math
# 1-vazifa
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
print("Yig'indisi:", a + b)

# 2-masala
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
print("Ko'paytmasi:", a * b)

#3-masala
a = int(input("Sonni kiriting: "))
print("7ga bo'lgandagi qoldiq:", a % 7)

#4-masala
a = input("Ikki xonali sonni kiriting: ")
print("Teskari son:", a[::-1])

#5-masala
A = int(input("A uzunligini kiriting: "))
B = int(input("B uzunligini kiriting: "))
print("Kesma joylashish soni:", A // B)

#6-masala
name = input("Ismingizni kiriting: ")
print("Salom", name)

#7-masala
soz = input("So'zni kiriting: ")
print("Yangi so'z:", 'a' + soz + 'a')

#8-masala
soz = input("So'zni kiriting: ")
if soz == soz[::-1]:
    print("So'z takroriy (palindrom)")
else:
    print("So'z takroriy emas")

#9-masala
A = int(input("Binodagi qavatlar sonini kiriting: "))
B = int(input("Qavatdagi xonalar sonini kiriting: "))
C = int(input("Bitta xonadagi partalar sonini kiriting: "))
print("Umumiy partalar soni:", A * B * C)

#10-masala
a = int(input("Sonni kiriting: "))
print("Kvadrati:", a**2)

#11-masala
a = int(input("Kvadratning tomonini kiriting: "))
print("Perimetri:", 4 * a)
print("Yuzasi:", a * a)

#12-masala
R = float(input("Radiusni kiriting: "))
pi = 3.14159
print("Diametri:", 2 * R)
print("Yuzasi:", pi * R**2)
print("Uzunligi:", 2 * pi * R)

#13-masala
gradus = float(input("Gradusni kiriting: "))
pi = 3.14159
radian = gradus * (pi / 180)
print("Radian:", radian)

#14-masala
L = float(input("Metrlarda uzunlikni kiriting: "))
print("Santimetr:", L * 100)
print("Millimetr:", L * 1000)
print("Kilometr:", L / 1000)

#15-masala
son = input("Uch xonali sonni kiriting: ")
print("Teskari son:", son[::-1])

#16-masala
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
a, b = b, a
print("Almashtirilgan sonlar: a =", a, ", b =", b)

#17-masala
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))
a, b, c = b, c, a
print("Almashtirilgan sonlar: a =", a, ", b =", b, ", c =", c)

#18-masala
a = int(input(f"A = "))
b = int(input(f"B = "))
c = int(input(f"C = "))

print(f"AB nuqta uchun oraliq masofa: {abs(b-a)}")
print(f"AC nuqta uchun oraliq masofa: {abs(c-a)}")
print(f"BC nuqta uchun oraliq masofa: {abs(c-b)}")
#1-masala
L = int(input("Uzunlikni santimetrda kiriting: "))
meters = L // 100
print(f"To'liq metrlar soni: {meters}")

#2-masala
M = int(input("Og'irlikni kilogrammda kiriting: "))
tonnes = M // 1000
print(f"To'liq tonnalar soni: {tonnes}")

#3-masala
file_size = int(input("Fayl hajmini baytlarda kiriting: "))
kilobytes = file_size // 1024
print(f"To'liq kilobaytlar soni: {kilobytes}")

#4-masala
A = int(input())
B = int(input())
joylashishlar = A // B
print(joylashishlar)

#5-masala
A = int(input())
B = int(input())
joylashishlar = A // B
qoldiq = A % B
print(qoldiq)

#6-masala
number = int(input())
onlik = number // 10
birlik = number % 10
yigindi = onlik + birlik
print(yigindi)

#7-masala
number = int(input())
onlik = number // 10
birlik = number % 10
almashgan = birlik * 10 + onlik
print(almashgan)

#8-masala
number = int(input())
yuzlik = number // 100
print(yuzlik)

#9-masala
number = int(input())
yuzlik = number // 100
print(yuzlik)

#10-masala
number = int(input())
birlik = number % 10
onlik = (number // 10) % 10
yuzlik = number // 100
almashgan = birlik * 100 + yuzlik * 10 + onlik
print(almashgan)

#11-masala
number = int(input())
birlik = number % 10
onlik = (number // 10) % 10
yuzlik = number // 100
yigindi = birlik + onlik + yuzlik
print(yigindi)

#12-masala
number = int(input())
birlik = number % 10
onlik = (number // 10) % 10
yuzlik = number // 100
teskari = birlik * 100 + onlik * 10 + yuzlik
print(teskari)

#13-masala
number = int(input())
qoldiq = number % 100
yangisi = qoldiq * 10
print(yangisi)

#14-masala
number = int(input())
onlik = (number // 10) % 10
birlik = number % 10
yuzlik = number // 100
yangisi = onlik * 100 + birlik * 10 + yuzlik
print(yangisi)

#15-masala
number = int(input())
onlik = (number // 10) % 10
yuzlik = number // 100
birlik = number % 10
yangisi = yuzlik * 100 + birlik * 10 + onlik
print(yangisi)

#16-masala
number = int(input())
onlik = (number // 10) % 10
birlik = number % 10
yuzlik = number // 100
yangisi = onlik * 100 + birlik * 10 + yuzlik
print(yangisi)

#17-masala
number = int(input())
bir_marta_bolib = number // 1000
print(bir_marta_bolib)

#18-masala
number = int(input())
minglik = number // 1000
print(minglik)

#19-masala
N = int(input())
minutlar = N // 60
print(minutlar)

#20-masala
N = int(input())
soatlar = N // 3600
print(soatlar)

#21-masala
N = int(input())
minutlar = (N // 60) % 60
sekundlar = N % 60
print(minutlar, sekundlar)

#22-masala
N = int(input())
soatlar = N // 3600
sekundlar = N % 3600
print(soatlar, sekundlar)

#23-masala
N = int(input())
soatlar = N // 3600
qoldiq = N % 3600
minutlar = qoldiq // 60
sekundlar = qoldiq % 60
print(soatlar, minutlar, sekundlar)
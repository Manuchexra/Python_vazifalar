#1-masala
A = int(input("A sonini kiriting (A > B): "))
B = int(input("B sonini kiriting: "))
while A >= B:
    A -= B
print("Kesmadan ortib qolgan qism:", A)

#2-masala
A = int(input("A sonini kiriting (A > B): "))
B = int(input("B sonini kiriting: "))
count = 0
while A >= B:
    A -= B
    count += 1
print("Kesma B ga joylashgan marta:", count)

#3-masala
N = int(input("N sonini kiriting (N > 0): "))
K = int(input("K sonini kiriting (K > 0): "))
while N >= K:
    N -= K
print("Qoldiq:", N)

#4-masala
n = int(input("n sonini kiriting (n > 0): "))
power_of_three = 1
while power_of_three < n:
    power_of_three *= 3
if power_of_three == n:
    print("Bu 3 ning darajasi.")
else:
    print("Bu 3 ning darajasi emas.")

#5-masala
n = int(input("n sonini kiriting (n > 0): "))
k = 0
power = 1
while power < n:
    power *= 2
    k += 1
if power == n:
    print(f"n = 2^{k}")
else:
    print("n 2 ning darajasi emas.")

#6-masala
n = int(input("n sonini kiriting (n > 0): "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 2
print("n!! =", factorial)

#7-masala
n = int(input("n sonini kiriting (n > 0): "))
k = 0
while k ** 2 <= n:
    k += 1
print("Kvadratlari n dan katta bo'lmagan eng kichik k:", k)

#8-masala
n = int(input("n sonini kiriting (n > 0): "))
k = 0
while k ** 2 <= n:
    k += 1
print("Kvadratlari n dan katta bo'lgan eng katta k:", k - 1)

#9-masala
n = int(input("n sonini kiriting (n > 1): "))
k = 1
while 3 ** k < n:
    k += 1
print("Eng kichik k:", k)

#10-masala
n = int(input("n sonini kiriting (n > 1): "))
k = 1
while 3 ** k <= n:
    k += 1
print("Eng katta k:", k - 1)

#11-masala
n = int(input("n sonini kiriting (n > 1): "))
summa = 0
k = 0
while summa <= n:
    k += 1
    summa += k
print("Eng kichik k:", k)
print("Yig'indisi:", summa)

#12-masala
n = int(input("n sonini kiriting (n > 1): "))
summa = 0
k = 0
while summa + k + 1 <= n:
    k += 1
    summa += k
print("Eng katta k:", k)
print("Yig'indisi:", summa)

#13-masala
a = float(input("a sonini kiriting (a > 1): "))
summa = 0
k = 1
while summa <= a:
    summa += 1 / k
    k += 1
print("Eng kichik k:", k - 1)
print("Yig'indisi:", summa)

#14-masala
a = float(input("a sonini kiriting (a > 1): "))
summa = 0
k = 1
while summa + 1 / k <= a:
    summa += 1 / k
    k += 1
print("Eng katta k:", k - 1)
print("Yig'indisi:", summa)

#15-masala

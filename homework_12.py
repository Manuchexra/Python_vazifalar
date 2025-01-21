#1-masala
total = 0
while True:
    num = int(input("Raqam kiriting (0 tugatadi): "))
    if num == 0:
        break
    if num > 0:
        total += num
print("Yig'indi:", total)

#2-masala
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
if A > B:
    A, B = B, A  # A kichik bo'lishi uchun almashtiramiz
print("Yig'indi:", sum(range(A, B + 1)))

#3-masala
nums = []
while True:
    num = input("Raqam kiriting (stop uchun 'exit' yozing): ")
    if num.lower() == "exit":
        break
    nums.append(int(num))
print("Kiritilgan raqamlar:", nums)

#4-masala
x = [1, 2, 3, 14, 5, 6, 6, 7]
print("Eng katta element:", max(x))

#5-masala
x = [1, 2, 3, 14, 5, 6, 6, 7]
max_element = max(x)
print("Eng katta element indexi:", x.index(max_element))

#6-masala
num = int(input("Sonni kiriting: "))
print("Son xonasi:", len(str(abs(num))))

#7-masala
x = [1, 2, 0, 14, 5, -6]
print("Eng katta element:", max(x))
print("Eng kichik element:", min(x))

#8-masala
x = [-2, 31, 104, 51, 19, 7]
max_index = x.index(max(x))
min_index = x.index(min(x))
x[max_index], x[min_index] = x[min_index], x[max_index]
print("Elementlari almashtirilgan list:", x)

#9-masala
my_list = [10, 20, 30, 40, 50]
num = int(input("Sonni kiriting: "))
if num in my_list:
    print("Element bor")
else:
    print("Element yo'q")

#10-masala
a = int(input("A sonini kiriting: "))
b = int(input("B sonini kiriting: "))
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print("EKUB:", a)

#11-masala
a = int(input("A sonini kiriting: "))
b = int(input("B sonini kiriting: "))
original_a, original_b = a, b
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
ekub = a
ekuk = (original_a * original_b) // ekub
print("EKUK:", ekuk)
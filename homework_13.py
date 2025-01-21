#1-masala
print("1 dan 100 gacha yig'indisi:", sum(range(1, 101)))

#2-masala
odd_sum = sum(i for i in range(1, 51) if i % 2 != 0)
even_sum = sum(i for i in range(1, 51) if i % 2 == 0)
print("Toq sonlar yig'indisi:", odd_sum)
print("Juft sonlar yig'indisi:", even_sum)

#3-masala
count = sum(1 for i in range(-80, 81) if i % 7 == 0)
print("7 ga bo'linadigan sonlar soni:", count)

#4-masala
mevalar = ['olma', 'banan', 'apelsin', 'olma']
print("'Olma' so'zi soni:", mevalar.count('olma'))

#5-masala
A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))
if A > B:
    A, B = B, A  
odd_count = sum(1 for i in range(A, B + 1) if i % 2 != 0)
even_count = sum(1 for i in range(A, B + 1) if i % 2 == 0)
print("Toq sonlar soni:", odd_count)
print("Juft sonlar soni:", even_count)

#6-masala
x = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
divisible_by_2 = sum(1 for i in x if i % 2 == 0)
print("2 ga bo'linadiganlar soni:", divisible_by_2)

#7-masala
text = input("Matn kiriting: ")
capital_letters = sum(1 for char in text if char.isupper())
print("Katta harflar soni:", capital_letters)

#8-masala
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#9-masala
dyuymlar = [1, 2, 3, 4, 5]
santimetrlar = [round(d * 2.54, 2) for d in dyuymlar]
print("Santimetrlar:", santimetrlar)

#10-masala
sonlar = [5, 10, 15, 20, 25, 30]
juft_va_katta = [x for x in sonlar if x % 2 == 0 and x > 10]
print("Juft va 10 dan katta sonlar:", juft_va_katta)

# 11-masala
sonlar = [5, 10, 15, 20, 25, 30]
qoldiqlar = [x % 3 for x in sonlar]
print("3 ga bo'lgandagi qoldiqlar:", qoldiqlar)

#12-masala
x = ["olma", "banana", "olcha", "limon", "olxo'ri"]
boshlanadi_o = [item for item in x if item.startswith('o')]
print("'O' harfidan boshlangan elementlar:", boshlanadi_o)
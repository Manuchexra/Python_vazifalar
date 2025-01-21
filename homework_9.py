#1-masala
num = int(input())
if num > 0:
    num += 1
print(num)

#2-masala
a, b, c = map(int, input().split())
print(max(a, b, c))

#3-masala
a, b, c = map(int, input().split())
positive_count = sum(1 for x in (a, b, c) if x > 0)
print(positive_count)

#4-masala
num = int(input())
if num % 2 == 0:
    print("Juft")
else:
    print("Toq")
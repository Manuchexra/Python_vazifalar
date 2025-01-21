#1-masala
num = int(input())
if num > 0:
    num += 1
print(num)

#2-masala
num = int(input())
if num > 0:
    num += 1
else:
    num -= 2
print(num)

#3-masala
num = int(input())
if num > 0:
    num += 1
elif num < 0:
    num -= 2
else:
    num = 10
print(num)

#4-masala
a, b, c = map(int, input().split())
positive_count = sum(1 for x in (a, b, c) if x > 0)
print(positive_count)

#5-masala
a, b, c = map(int, input().split())
positive_count = sum(1 for x in (a, b, c) if x > 0)
negative_count = sum(1 for x in (a, b, c) if x < 0)
print("Musbat:", positive_count, "Manfiy:", negative_count)

#6-masala
a, b = map(int, input().split())
print(max(a, b))

#7-masala
a, b = map(int, input().split())
print(min(a, b))

#8-masala
a, b = map(int, input().split())
print(max(a, b), min(a, b))

#9-masala
a, b = map(int, input().split())
if a > b:
    a, b = b, a
print("A:", a, "B:", b)

#10-masala
a, b = map(int, input().split())
if a != b:
    a = b = a + b
else:
    a = b = 0
print("A:", a, "B:", b)

#11-masala
a, b = map(int, input().split())
if a != b:
    a = max(a, b)
    b = max(a, b)
else:
    a = b = 0
print("A:", a, "B:", b)

#12-masala
a, b, c = map(int, input().split())
print(min(a, b, c))

#13-masala
a, b, c = map(int, input().split())
print(sorted([a, b, c])[1])

#14-masala
# if14
a, b, c = map(int, input().split())
print(min(a, b, c), max(a, b, c))

#15-masala
a, b, c = map(int, input().split())
nums = [a, b, c]
nums.remove(max(nums))
print(sum(nums))

#16-masala
a, b, c = map(float, input().split())
if a < b < c:
    a, b, c = a * 2, b * 2, c * 2
else:
    a, b, c = -a, -b, -c
print(a, b, c)

#17-masala
a, b, c = map(float, input().split())
if a < b < c or a > b > c:
    a, b, c = a * 2, b * 2, c * 2
else:
    a, b, c = -a, -b, -c
print(a, b, c)

#18-masala
a, b, c = map(int, input().split())
if a == b:
    print(3)
elif a == c:
    print(2)
else:
    print(1)

#19-masala
a, b, c, d = map(int, input().split())
if a == b == c:
    print(4)
elif a == b == d:
    print(3)
elif a == c == d:
    print(2)
else:
    print(1)

#20-masala
a, b, c = map(int, input().split())
dist_b = abs(b - a)
dist_c = abs(c - a)
if dist_b < dist_c:
    print(b, dist_b)
else:
    print(c, dist_c)

#21-masala
x, y = map(int, input().split())
if x == 0 and y == 0:
    print(0)
elif x == 0:
    print(2)
elif y == 0:
    print(1)
else:
    print(3)

#22-masala
x, y = map(int, input().split())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

#23-masala
x1, y1, x2, y2 = map(int, input().split())
if x1 == x2:
    print(x1, y2)
elif y1 == y2:
    print(x2, y1)
else:
    print("Koordinatalar o'qlariga parallel emas")
#1-masala
A = int(input())
print(A > 0)

#2-masala
A = int(input())
print(A % 2 != 0)

#3-masala
A = int(input())
print(A % 2 == 0)

#4-masala
A, B = map(int, input().split())
print(A > 2 and B <= 3)

#5-masala
A, B = map(int, input().split())
print(A >= 0 or B < -2)

#6-masala
A, B, C = map(int, input().split())
print(A <= B <= C)

#7-masala
A, B, C = map(int, input().split())
print(A < B < C or C < B < A)

#8-masala
A, B = map(int, input().split())
print(A % 2 != 0 and B % 2 != 0)

#9-masala
A, B = map(int, input().split())
print(A % 2 != 0 or B % 2 != 0)

#10-masala
A, B = map(int, input().split())
print((A % 2 != 0) != (B % 2 != 0))

#11-masala
# Boolean11
A, B = map(int, input().split())
print((A % 2 == B % 2))

#12-masala
A, B, C = map(int, input().split())
print(A > 0 and B > 0 and C > 0)

#13-masala
A, B, C = map(int, input().split())
print(A > 0 or B > 0 or C > 0)

#14-masala
A, B, C = map(int, input().split())
print((A > 0) + (B > 0) + (C > 0) == 1)

#15-masala
A, B, C = map(int, input().split())
print((A > 0) + (B > 0) + (C > 0) == 2)

#16-masala
N = int(input())
print(10 <= N <= 99 and N % 2 == 0)

#17-masala
N = int(input())
print(100 <= N <= 999 and N % 2 != 0)

#18-masala
A, B, C = map(int, input().split())
print((A == B) + (B == C) + (A == C) >= 1)
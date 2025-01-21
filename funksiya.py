# FunSimple1
def PowerA3(A, B, C):
    D = A**3
    E = B**3
    F = C**3
    return D, E, F

# FunSimple2
def PowerA234(A, B, C):
    D = A**2
    E = B**3
    F = C**4
    return D, E, F

# FunSimple3
def MEAN(A, B, C, D):
    arithmetic_mean = (A + B) / 2
    geometric_mean = (C * D)**0.5
    return arithmetic_mean, geometric_mean

# FunSimple4
def Triangle(a):
    perimeter = 3 * a
    area = (a**2 * (3**0.5)) / 4
    return perimeter, area

# FunSimple5
def RectPS(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area

# FunSimple6
def DigitCountSum(n):
    digit_count = 0
    digit_sum = 0
    while n > 0:
        digit_count += 1
        digit_sum += n % 10
        n //= 10
    return digit_count, digit_sum

# FunSimple7
def InvertDigit(n):
    inverted = 0
    while n > 0:
        inverted = inverted * 10 + n % 10
        n //= 10
    return inverted

# FunSimple8
def AddRightDigit(n, r):
    return n * 10 + r

# FunSimple9
def AddLeftDigit(n, r):
    r_digits = len(str(r))
    return r * (10**len(str(n))) + n

# FunSimple10
def Swap(A, B):
    A, B = B, A
    return A, B

# FunSimple11
def Minmax(X, Y):
    if X > Y:
        return Y, X
    else:
        return X, Y

# FunSimple12
def SortInc3(A, B, C):
    lst = [A, B, C]
    lst.sort()
    return lst

# FunSimple13
def SortDec3(A, B, C):
    lst = [A, B, C]
    lst.sort(reverse=True)
    return lst

# FunSimple14
def ShiftRight3(A, B, C):
    return C, A, B

# FunSimple15
def ShiftLeft3(A, B, C):
    return B, C, A

# FunSimple16
def Sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

# FunSimple17
def QuadraticRoots(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return "Ildizlar mavjud emas"
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return root1, root2

# FunSimple18
import math
def CircleArea(r):
    return math.pi * r**2

# FunSimple19
def RingArea(R1, R2):
    return math.pi * (R1**2 - R2**2)

# FunSimple20
def TrianglePerimeter(A, B):
    hypotenuse = (A**2 + B**2)**0.5
    perimeter = A + B + hypotenuse
    return perimeter

# FunSimple21
def SumRange(A, B):
    if A > B:
        return 0
    return sum(range(A, B + 1))

# FunSimple22
def Calc(A, B, Op):
    if Op == 1:  # qo'shish
        return A + B
    elif Op == 2:  # ayirish
        return A - B
    elif Op == 3:  # ko'paytirish
        return A * B
    elif Op == 4:  # bo'lish
        if B != 0:
            return A / B
    return None

# FunSimple23
def Quarter(X, Y):
    if X > 0 and Y > 0:
        return 1  # Birinchi chorak
    elif X < 0 and Y > 0:
        return 2  # Ikkinchi chorak
    elif X < 0 and Y < 0:
        return 3  # Uchinchi chorak
    elif X > 0 and Y < 0:
        return 4  # To'rtinchi chorak
    return None

# FunSimple24
def Even(K):
    return K % 2 == 0

# FunSimple25
def IsSquare(K):
    root = K**0.5
    return root == int(root)

# FunSimple26
def IsPower5(K):
    while K > 1:
        if K % 5 != 0:
            return False
        K //= 5
    return K == 1

# FunSimple27
def IsPowerN(K, N):
    while K > 1:
        if K % N != 0:
            return False
        K //= N
    return K == 1

# FunSimple28
def IsPrime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

# FunSimple29
def DigitCount(K):
    return len(str(K))

# FunSimple30
def DigitN(K, N):
    digits = str(K)
    if 1 <= N <= len(digits):
        return int(digits[N - 1])
    return -1

import math

# Fun Simple31: 
def IsPalindrom(N):
    return str(N) == str(N)[::-1]

def count_palindromes(numbers):
    return sum(1 for num in numbers if IsPalindrom(num))

# Fun Simple32:
def DegToRad(D):
    return D * (math.pi / 180)

def convert_degrees_to_radians(degrees):
    return [DegToRad(d) for d in degrees]

# Fun Simple33:
def RadToDeg(R):
    return R * (180 / math.pi)

def convert_radians_to_degrees(radians):
    return [RadToDeg(r) for r in radians]

# Fun Simple34: 
def Fact(N):
    if N == 0 or N == 1:
        return 1
    result = 1
    for i in range(2, N + 1):
        result *= i
    return result

def calculate_factorials(numbers):
    return [Fact(n) for n in numbers]

# Fun Simple35: 
def Fact2(N):
    result = 1
    for i in range(N, 0, -2):
        result *= i
    return result

def calculate_double_factorials(numbers):
    return [Fact2(n) for n in numbers]

# Fun Simple36: 
def Fib(N):
    if N <= 0:
        return 0
    elif N == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, N + 1):
        a, b = b, a + b
    return b

def calculate_fibonacci_numbers(numbers):
    return [Fib(n) for n in numbers]

# Fun Simple37:
def Power1(A, B):
    return A ** B

def calculate_powers(numbers, B):
    return [Power1(A, B) for A in numbers]

# Fun Simple38:
def Power2(A, N):
    if N == 0:
        return 1
    elif N > 0:
        result = 1
        for _ in range(N):
            result *= A
        return result
    else:
        return 1 / Power2(A, -N)

def calculate_powers_with_exponents(A, exponents):
    return [Power2(A, N) for N in exponents]

# Fun Simple39: 
def Power3(A, N):
    if N % 1 != 0:
        return Power2(A, int(N))
    else:
        return Power1(A, N)

def calculate_powers_with_fractional_exponents(A, exponents):
    return [Power3(A, N) for N in exponents]

# Fun Simple40: 
def Exp1(x, ε):
    result = 1.0
    term = 1.0
    n = 1
    while True:
        term *= x / n
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

def calculate_exponentials(x_values, ε_values):
    return [Exp1(x, ε) for x, ε in zip(x_values, ε_values)]


import math

# FunSimple41: sin(x) ni hisoblash
def sin1(x, ε):
    result = 0.0
    n = 0
    while True:
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple42: cos(x) ni hisoblash
def cos1(x, ε):
    result = 0.0
    n = 0
    while True:
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple43: ln(1 + x) ni hisoblash
def Ln1(x, ε):
    if abs(x) >= 1:
        raise ValueError("|x| < 1 shartini qanoatlantirishi kerak")
    result = 0.0
    n = 1
    while True:
        term = ((-1) ** (n + 1)) * (x ** n) / n
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple44: arctg(x) ni hisoblash
def Arctg1(x, ε):
    if abs(x) >= 1:
        raise ValueError("|x| < 1 shartini qanoatlantirishi kerak")
    result = 0.0
    n = 0
    while True:
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple45: (1 + x)^a ni hisoblash
def Power4(x, a, ε):
    if abs(x) >= 1:
        raise ValueError("|x| < 1 shartini qanoatlantirishi kerak")
    result = 1.0
    n = 1
    while True:
        term = (a * (a - 1) * ... * (a - n + 1)) * (x ** n) / math.factorial(n)
        if abs(term) < ε:
            break
        result += term
        n += 1
    return result

# FunSimple46: 
def EKUB(A, B):
    while B:
        A, B = B, A % B
    return A

# FunSimple47: 
def Frac1(a, b, p, q):
    gcd = EKUB(a, b)
    p = a // gcd
    q = b // gcd
    return p, q

# FunSimple48:
def EKUK(A, B):
    return A * B // EKUB(A, B)

# FunSimple49: 
def EKUB3(A, B, C):
    return EKUB(EKUB(A, B), C)


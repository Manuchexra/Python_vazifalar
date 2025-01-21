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

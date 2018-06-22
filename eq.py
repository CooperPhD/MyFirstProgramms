def gcd(a, b, x):
    if a == 0 or b == 0:
        return max(a, b)
    elif a > b:
        return gcd(a - b, b, x + 1)
    else:
        return gcd(a, b - a, x + 1)
x = 0
a = int(input())
b = int(input())
print(gcd(a, b, x))
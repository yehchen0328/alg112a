a = int(input('Enter numbers : '))
b = int(input('Enter numbers : '))
c = int(input('Enter numbers : '))
d = int(input('Enter numbers : '))

#方法 1
def power2a(a):
    return 2**a
result = power2a(a)
print(result)

# 方法 2a：用遞迴

def power2b(b):
    if b < 0: raise ValueError("b cannot be negative")
    if b == 0: return 1
    if b == 1: return 2
    return power2b(b - 1) + power2b(b - 1)
result2 = power2b(b)
print(result2)


# 方法2b：用遞迴
def power2c(c):
    if c < 0: raise ValueError("c cannot be negative")
    if c == 0: return 1
    return 2*power2c(c-1)

result3 = power2c(c)
print(result3)

# 方法 3：用遞迴+查表
def power2d(d):
    pow2d = [None]*10000
    pow2d[0] = 1
    pow2d[1] = 2

    if d < 0:  raise ValueError("d cannot be negative")
    if not pow2d[d] is None: return pow2d[d]
    pow2d[d] = power2d(d-1)+power2d(d-1)
    return pow2d[d]

print(power2d(d))

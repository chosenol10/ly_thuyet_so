#  greatest common divisor: ước chung lớn nhất
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Least common multiple: bội chung nhỏ nhất
def lcm(a, b):
    return (a//(gcd(a, b)) * b)

# a = list(map(int, input().split()))
# res = 0
# ans = 1
# for i in a:
#     res = gcd(res, i)
#     ans = lcm(ans, i)
# print(res, ans)


# __________Đồng dư_________
# gặp cái bài toán có kq quá lớn
# in ra các kết quả đó chia dư cho cái số nào đó

# Công Thức:
#______________________________________________________#
#        (A + B) % C = (A % C + B % C) % C             #
#        (A - B) % C = (A % C - B % C) % C             #
#        (A * B) % C = ((A % C) * (B % C)) % C         #
#        (A ^ B) % C = (A % C) ^ (B % C)               #
#        (A / B) % C = ((A % C) * B^-1) % C            #
#______________________________________________________#

MAX_N = 10**6
MOD = 10**9 + 7

def powmod(a, b, c):
    res = 1
    # a %= c
    for i in range(1, b):
        res *= a
        res %= c
    return res % c

# print (powmod(1032, 1000001, 10))

def fib0(n):
    f= [0]*(n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        f[i] %= MOD
    return f[n] 


# __________LUỹ THỪA NHỊ PHÂN: BINARY EXPONENTIATION__________

# cach 1: (A ^ B)% C
def binpow(a, b):
    if b == 0:
        return 1
    x =binpow(a, b / 2)
    if b % 2 == 1:
        return x * x * a
    else:
        return X * x

# cach 2: Binary Pow
def binpow2(a, b):
    res = 1
    while b != 0:
        if b % 2 == 1:
            res *= a
        b //= 2
        a * a
    return res


# ______CSC, CSN______

# trong vở anh nhé!


#chỉnh hợp, tổ hợp , chrh hợp lập

def nCk(n, k):
    res = 1
    k = min(k, n - k)
    for i in range(k):
        res *= (n - i)
        res /= (i + 1)


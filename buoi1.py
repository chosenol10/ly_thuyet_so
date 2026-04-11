# #  greatest common divisor: ước chung lớn nhất
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# # Least common multiple: bội chung nhỏ nhất
# def lcm(a, b):
#     return (a//(gcd(a, b)) * b)

# # a = list(map(int, input().split()))
# # res = 0
# # ans = 1
# # for i in a:
# #     res = gcd(res, i)
# #     ans = lcm(ans, i)
# # print(res, ans)


# # __________Đồng dư_________
# # gặp cái bài toán có kq quá lớn
# # in ra các kết quả đó chia dư cho cái số nào đó

# # Công Thức:
# #______________________________________________________#
# #        (A + B) % C = (A % C + B % C) % C             #
# #        (A - B) % C = (A % C - B % C) % C             #
# #        (A * B) % C = ((A % C) * (B % C)) % C         #
# #        (A ^ B) % C = (A % C) ^ (B % C)               #
# #        (A / B) % C = ((A % C) * B^-1) % C            #
# #______________________________________________________#

# MAX_N = 10**6
# MOD = 10**9 + 7

# def powmod(a, b, c):
#     res = 1
#     # a %= c
#     for i in range(1, b):
#         res *= a
#         res %= c
#     return res % c

# # print (powmod(1032, 1000001, 10))

# def fib0(n):
#     f= [0]*(n + 1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n + 1):
#         f[i] = f[i - 1] + f[i - 2]
#         f[i] %= MOD
#     return f[n] 


# # __________LUỹ THỪA NHỊ PHÂN: BINARY EXPONENTIATION__________

# # cach 1: (A ^ B)% C
# def binpow(a, b):
#     if b == 0:
#         return 1
#     x = binpow(a, b / 2)
#     if b % 2 == 1:
#         return x * x * a
#     else:
#         return  x * x

# # cach 2: Binary Pow
# def binpow2(a, b):
#     res = 1
#     while b != 0:
#         if b % 2 == 1:
#             res *= a
#         b //= 2
#         a * a
#     return res


# # ______CSC, CSN______

# # trong vở anh nhé!


# #chỉnh hợp, tổ hợp , chrh hợp lập

# def nCk(n, k):
#     res = 1
#     k = min(k, n - k)
#     for i in range(k):
#         res *= (n - i)
#         res /= (i + 1)

# # tìm x sao cho N! chia hết cho K^x (K là số nguyên tố), x là số lớn nhẩt

# def  degree(n, k):
#     ans = 0
#     for i in range(k, n + 1, k):
#         m = i
#         while (m % k == 0):
#             ans  += 1
#             m //= k
#     return ans

# print(degree(20,3))

# def degree2(n, k):
#     ans = 0
#     while n:
#         n //= k
#         ans += n
#     return ans

# print(degree2(20,3))

def sang(n):
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) +1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    # return [i for i in range(2, n + 1) if is_prime[i]]
    return is_prime


def segment_sieve(L, R):
    limt = int(R ** 0.5 ) + 1
    primes = sang(limt)
    is_prime = [True] * (R - L + 1)
    for p in primes:
        start = max(p*p, ((L + p - 1)// p))
        for j in range(start, R + 1, p):
            is_prime[j-L] = False
    
    if L == 1:
        is_prime[0] = False

    for i in range(len(is_prime)):
        if is_prime[i]:
            print (i + L, end=" ")
    print()

MAX_N = 10**6 + 7

is_prime = sang(MAX_N)
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, int(n // 2) + 1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)

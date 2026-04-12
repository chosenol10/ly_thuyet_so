# # # # # #  greatest common divisor: ước chung lớn nhất
# # # # # def gcd(a, b):
# # # # #     if b == 0:
# # # # #         return a
# # # # #     return gcd(b, a % b)

# # # # # # Least common multiple: bội chung nhỏ nhất
# # # # # def lcm(a, b):
# # # # #     return (a//(gcd(a, b)) * b)

# # # # # # a = list(map(int, input().split()))
# # # # # # res = 0
# # # # # # ans = 1
# # # # # # for i in a:
# # # # # #     res = gcd(res, i)
# # # # # #     ans = lcm(ans, i)
# # # # # # print(res, ans)


# # # # # # __________Đồng dư_________
# # # # # # gặp cái bài toán có kq quá lớn
# # # # # # in ra các kết quả đó chia dư cho cái số nào đó

# # # # # # Công Thức:
# # # # # #______________________________________________________#
# # # # # #        (A + B) % C = (A % C + B % C) % C             #
# # # # # #        (A - B) % C = (A % C - B % C) % C             #
# # # # # #        (A * B) % C = ((A % C) * (B % C)) % C         #
# # # # # #        (A ^ B) % C = (A % C) ^ (B % C)               #
# # # # # #        (A / B) % C = ((A % C) * B^-1) % C            #
# # # # # #______________________________________________________#

# # # # # MAX_N = 10**6
# # # # # MOD = 10**9 + 7

# # # # # def powmod(a, b, c):
# # # # #     res = 1
# # # # #     # a %= c
# # # # #     for i in range(1, b):
# # # # #         res *= a
# # # # #         res %= c
# # # # #     return res % c

# # # # # # print (powmod(1032, 1000001, 10))

# # # # # def fib0(n):
# # # # #     f= [0]*(n + 1)
# # # # #     f[0] = 0
# # # # #     f[1] = 1
# # # # #     for i in range(2, n + 1):
# # # # #         f[i] = f[i - 1] + f[i - 2]
# # # # #         f[i] %= MOD
# # # # #     return f[n] 


# # # # # # __________LUỹ THỪA NHỊ PHÂN: BINARY EXPONENTIATION__________

# # # # # # cach 1: (A ^ B)% C
# # # # # def binpow(a, b):
# # # # #     if b == 0:
# # # # #         return 1
# # # # #     x = binpow(a, b / 2)
# # # # #     if b % 2 == 1:
# # # # #         return x * x * a
# # # # #     else:
# # # # #         return  x * x

# # # # # # cach 2: Binary Pow
# # # # # def binpow2(a, b):
# # # # #     res = 1
# # # # #     while b != 0:
# # # # #         if b % 2 == 1:
# # # # #             res *= a
# # # # #         b //= 2
# # # # #         a * a
# # # # #     return res


# # # # # # ______CSC, CSN______

# # # # # # trong vở anh nhé!


# # # # # #chỉnh hợp, tổ hợp , chrh hợp lập

# # # # # def nCk(n, k):
# # # # #     res = 1
# # # # #     k = min(k, n - k)
# # # # #     for i in range(k):
# # # # #         res *= (n - i)
# # # # #         res /= (i + 1)

# # # # # # tìm x sao cho N! chia hết cho K^x (K là số nguyên tố), x là số lớn nhẩt

# # # # # def  degree(n, k):
# # # # #     ans = 0
# # # # #     for i in range(k, n + 1, k):
# # # # #         m = i
# # # # #         while (m % k == 0):
# # # # #             ans  += 1
# # # # #             m //= k
# # # # #     return ans

# # # # # print(degree(20,3))

# # # # def degree2(n, k):   #trong 20! thi` co bao nhiu lan so 3 xuat hien (n! co ? k^ans)`
# # # #     ans = 0
# # # #     while n:
# # # #         n //= k
# # # #         ans += n
# # # #     return ans

# # # # print(degree2(20,3))

# # # # # def sang(n):
# # # # #     is_prime = [True]*(n+1)
# # # # #     is_prime[0] = is_prime[1] = False
# # # # #     for i in range(2, int(n ** 0.5) +1):
# # # # #         if is_prime[i]:
# # # # #             for j in range(i*i, n + 1, i):
# # # # #                 is_prime[j] = False

# # # # #     # return [i for i in range(2, n + 1) if is_prime[i]]
# # # # #     return is_prime


# # # # # def segment_sieve(L, R):
# # # # #     limt = int(R ** 0.5 ) + 1
# # # # #     primes = sang(limt)
# # # # #     is_prime = [True] * (R - L + 1)
# # # # #     for p in primes:
# # # # #         start = max(p*p, ((L + p - 1)// p))
# # # # #         for j in range(start, R + 1, p):
# # # # #             is_prime[j-L] = False
    
# # # # #     if L == 1:
# # # # #         is_prime[0] = False

# # # # #     for i in range(len(is_prime)):
# # # # #         if is_prime[i]:
# # # # #             print (i + L, end=" ")
# # # # #     print()

# # # # # MAX_N = 10**6 + 7

# # # # # is_prime = sang(MAX_N)
# # # # # t = int(input())
# # # # # for _ in range(t):
# # # # #     n = int(input())
# # # # #     for i in range(2, int(n // 2) + 1):
# # # # #         if is_prime[i] and is_prime[n - i]:
# # # # #             print(i, n - i)



# # # # # _______phan tich thua so nguyen to_________
 
# # # # # cho 1 so xong phan tich cac boi cua so do co phai la song nguyen to k neu co thi in ra

# # # # t = int(input())
# # # # for _ in range(t):
        
# # # #     n = int(input())
# # # #     ans = []
# # # #     d = [2, 3, 5, 7]
# # # #     for i in d:
# # # #         while n % i == 0:
# # # #             ans.append(i)
# # # #             n //= i
# # # #     if n != 1:
# # # #         ans.append(n)

# # # #     print(*ans, sep= " x ")


# # # # def degree(n, k):
# # # #     ans = 0
# # # #     while n:
# # # #         n //=k
# # # #         ans +=n
# # # #     return ans
# # # # print(degree(20,3))

# # # # t = int(input())
# # # # for _ in range(t):
# # # #     a,b = map(int, input().split())
# # # #     c1 = int(a ** 0.5) 
# # # #     c2 =  int(b ** 0.5) + 1
# # # #     if c1 * c1 != a:
# # # #         c1 += 1
# # # #     for i in range(c1, c2):
# # # #         print(i*i, end=" ")
# # # #     print()

# # # # t = int(input())
# # # # for _ in range(t):
# # # #     a,b = map(int, input().split())
# # # #     c1 = int(a ** 0.5) 
# # # #     c2 =  int(b ** 0.5) + 1
# # # #     cnt = 0
# # # #     if c1 * c1 != a:
# # # #         c1 += 1
# # # #     for i in range(c1, c2):
# # # #         cnt += 1
# # # #     print(cnt)


# # # # ________so hoan hao_________
# # # # tong cac uoc cua 1 so bang chi no la so hoan hao

# # # # def isHH(n):
# # # #     tong = 1
# # # #     for i in range(2, int(n ** 0.5) + 1):
# # # #         if n % i == 0:
# # # #             tong += i
# # # #             if i != n//i:
# # # #                 tong += n //i
# # # #     return tong == n

# # # # t =int(input())
# # # # for _ in range(t):
# # # #     n  = int(input())
# # # #     print(isHH(n))

# # # # toi uu so hoan hoa truong hop 10**18
# # # # def nt(n):
# # # #     for i in range(2, int (n ** 0.5) + 1):
# # # #         if n % i == 0:
# # # #             return False
# # # #     return n > 1

# # # # HH = [0] * 100
# # # # cnt = 0

# # # # def init():
# # # #     global cnt
# # # #     for p in range(2, 33):
# # # #         if nt(p):
# # # #             tmp = int(pow(2, p) - 1)
# # # #             if nt(tmp):
# # # #                 HH[cnt] = pow(2, p - 1)*tmp
# # # #                 cnt += 1

# # # # init()
# # # # t = int(input())
# # # # for _ in range(t):
# # # #     n = int(input())
# # # #     ok = False
# # # #     for i in range(0, cnt):
# # # #         if n == HH[i]:
# # # #             ok = True
# # # #             break
# # # #     if ok == True:
# # # #         print("YES")
# # # #     else:
# # # #         print("NO")


# # # # # init()
# # # # # for i in range(0, cnt):
# # # # #     print(HH[i])


# # # #                             ================================= #

# # # # def nt(n):
# # # #     for i in range(2, int(n ** 0.5) + 1):
# # # #         if n % i == 0:
# # # #             return False
# # # #     return n > 1

# # # # HH = [0] * 100
# # # # cnt = 0
# # # # def init():
# # # #     global cnt
# # # #     cnt = 0
# # # #     for p in range(2, 33):
# # # #         if nt(p):
# # # #             tmp = (1 << p) - 1
# # # #             if nt(tmp):
# # # #                 HH[cnt] = (1 << (p - 1)) * tmp
# # # #                 cnt += 1

# # # # init()

# # # # t = int(input())
# # # # for _ in range(t):
# # # #     n = int(input())
# # # #     flag = False
# # # #     for i in range(cnt):
# # # #         if n == HH[i]:
# # # #             flag = True
# # # #             break
# # # #     if flag:
# # # #         print("YES")
# # # #     else:
# # # #         print("NO")


# # # # --------fibonaci--------

# # # # fi = [0] * 100

# # # # def init():
# # # #     fi[0] = 0
# # # #     fi[1] = 1
# # # #     for i in range(2, 100):
# # # #         fi[i] = fi[i - 1] + fi[i - 2] 
# # # # init()

# # # # for i in range(0, 100):
# # # #     print(fi[i])
# # # # t = int(input())
# # # # for _ in  range(t):
# # # #     n = int(input())
# # # #     flag  = False
# # # #     for i in range(0, 92 + 1):
# # # #         print(fi[i])
# # # #         if n == fi[i]:
# # # #             flag = True
# # # #             break
# # # #     if flag:
# # # #         print("yes")
# # # #     else:
# # # #         print("NO")



# # # # ------------phi ham euler-----------

# # # # dem cac so la 2 so cung nhau (boi chung lon nhat la 1)
# # # # cong thuc :
# # #             # phi(n) = n. tich("uoc cua n") . (1 - 1 //i)
# # # # code:

# # # # def phi(n):
# # # #     res = n
# # # #     for i in range(2, int(n ** 0.5) + 1):
# # # #         if n % i == 0:
# # # #             while n % i == 0:
# # # #                 n //= i
# # # #             res -= res//i
# # # #     if n != 1:
# # # #         res -= res//n
# # # #     return res

# # # # print(phi(120))
    

# # # def phi(n):
# # #     res = n
# # #     for i in range(2, int(n ** 0.5) + 1):
# # #         if n % i== 0:
# # #             while n % i == 0:
# # #                 n //= i
# # #             res -= res//i
# # #     if n != 1:
# # #         res -= res//n
# # #     return res

# # # print(phi(120))



# # # tim bncc cua so co n chu so 


# # # x, y , z, n = map(int, input().split())
# # # for i in range(pow(10, n -1), pow(10, n)):
# # #     if i % x == 0 and i % y == 0 and i % z == 0:
# # #         print(i)
# # #     else:
# # #         print(int(-1))
# # #         break

# # # toi uu hon

# # def gcd(a,b):
# #     if b == 0:
# #         return a
# #     return gcd(b, a % b)

# # def lcm(a,b):
# #     return a // gcd(a,b) * b

# # x, y , z, n = map(int, input().split())
# # bcnn = lcm(x, lcm(y, z))
# # res = ((10**(n-1) + bcnn - 1)// bcnn)*bcnn
# # print(res) if res < 10**n else print(-1)


# def phi(n):
#     res = n
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             while (n % i == 0):
#                 n //= i
#             res  -= res//i
#     if n  != 1:
#         res -= res//n
#     return res

# n = 10
# for i in range(2, n + 1):
#     print(phi(i), end=" ")


phi = [0] * 100001

def sang():
    for i in range(1,100001):
        phi[i] = i

    for i in range(2,100001):
        if phi[i] == i:
            phi[i] = i - 1
            for j in range(i * 2, 100001, i):
                phi[j] -= phi[j] // i

sang()
n = int(input())
for i in range(1,n + 1):
    print(phi[i], end=" ")
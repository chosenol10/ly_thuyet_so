# # # # check so ngto 
# # # # def sieve(n):
# # # #     is_prime = [True] * (n + 1)
# # # #     is_prime[0] = is_prime[1] = False
# # # #     for i in range(2, int(n**0.5) + 1):
# # # #         if is_prime[i]:
# # # #             for j in range(i*i, n + 1, i):
# # # #                 is_prime[j] = False
# # # #     return is_prime

# # # # t = int(input())
# # # # arr = [int(input()) for _ in range(t)]
# # # # is_prime = sieve(max(arr))
# # # # for n in arr:
# # # #     print("YES" if is_prime[n] else "NO")        

# # # # ____________________________________________________
# # # # ktra so nguyen to va chu so cũng là số nguyên tố
# # # # viết chương trình đếm xem trong đoạn a,b  có bao nhiêu số là snt và tất cả các chữ số đều là số nguyên tố

# # # def sang(n):
# # #     is_prime = [True] * (n+1)
# # #     is_prime[0] = is_prime[1] = False
# # #     for i in range(2, int(n ** 0.5) + 1):
# # #         if is_prime[i]:
# # #             for j in range(i*i, n + 1, i):
# # #                 is_prime[j] = False
# # #     return is_prime
# # #     # return [i for i in range(2, n + 1) if is_prime[i]]

# # # # def segment_sieve(L, R):
# # # #     Limit = int(R ** 0.5) + 1
# # # #     primes = sang(Limit)
# # # #     is_prime = [True] * (R - L + 1)
# # # #     for p in primes:
# # # #         start = max(p*p, (( L + p - 1)//p)*p)
# # # #         for j in range(start, R + 1, p):
# # # #             is_prime[j - L] = False

# # # #     for i in range(len(is_prime)):
# # # #         if is_prime[i] and (i + L) >= 2:
# # # #             print(i + L, end=" ")

# # # # def digitPrime(n):
# # # #     while(n):
# # # #         r = n % 10
# # # #         if r not in [2,3,5,7]:
# # # #             return False
# # # #         n //= 10
# # # #     return True

# # # MAX_N = 10**6
# # # # # is_prime = sang(MAX_N)

# # # # t = int(input())
# # # # for _ in range(t):  
# # # #     cnt = 0
# # # #     nums = int(input())
# # # #     for n in range(2, nums + 1):
# # # #         if  is_prime[n] and digitPrime(n):
# # # #             cnt += 1
# # # #     print(cnt)

# # # ---------------------- ĐÉM TRONG ĐOẠN ĐÓ CÓ BAO NHIÊU SỐ NGUYÊN TỐ-----------------------

# # # def ssnt(n):
# # #     is_prime = [True]*(n+1)
# # #     is_prime[0] = is_prime[1] = False
# # #     for i in range(2, int(n**0.5)):
# # #         if is_prime[i]:
# # #             for j in range(i*i, n + 1, i ):
# # #                 is_prime[j] = False
# # #     return is_prime

# # # t = int(input())
# # # cnt = i = 0
# # # is_prime = ssnt(MAX_N)
# # # while cnt < t:
# # #     if is_prime[i]:
# # #         cnt += 1
# # #         print(i)
# # #     i += 1

# # # --------------------- CẶP SỐ NGUYÊN TỐ CÓ TỔNG BẰNG N---------------------------
# # # def sang(n):
# # #     is_prime = [True] * (n+1)
# # #     is_prime[0] = is_prime[1] = False
# # #     for i in range(2, int(n ** 0.5) + 1):
# # #         if is_prime[i]:
# # #             for j in range(i*i, n+1, i):
# # #                 is_prime[j] = False
# # #     return is_prime
    
# # # MAX_N = 10**6
# # # is_prime = sang(MAX_N)

# # # t = int(input())
# # # for _ in range(t):
# # #     n = int(input())
# # #     for i in range (2, int(n/2 + 1)):
# # #         if is_prime[i] and is_prime[n-i]:
# # #             print(i, n-i)

         
# # # ---------------------SỐ THUẦN NGUYÊN TỐ-----------------
# # #  xay dung ham check so nguyen to
# # #  ham tat ca cac chu so no la so nguyen to 
# # #   ham tong chu so cua no la so nguyen to

# # from math import sqrt

# # def sang(n):
# #     is_prime = [True] * (n+1)
# #     is_prime[0] = is_prime[1]  = False
# #     for i in range(2, int(sqrt(n)) + 1):
# #         if is_prime[i]:
# #             for j in range(i*i, n + 1, i):
# #                 is_prime[j] = False
# #     return is_prime 

# # def segment_sieve(L, R):
# #     LIMIT = int(sqrt(R)) + 1
# #     primes = [i for i in range(2, LIMIT + 1) if sang(LIMIT)[i]] 
# #     is_prime = [True]  * (R - L + 1)
# #     for p in primes:
# #         start = max(p*p, ((L + p - 1)//p)*p)
# #         for j in range(start, R + 1, p):
# #             is_prime[j - L] =False 

# #     if L == 1:
# #         is_prime = False
# #     return is_prime

# # def digitPrime(n):
# #     while n:
# #         r = n % 10
# #         if r not in [2, 3, 5, 7]:
# #             return False
# #         n //= 10
# #     return True 

# # def sumPrime(n):
# #     sum1 = 0
# #     while n:
# #         sum1 +=  n % 10
# #         n //= 10
# #     return sum1


# # is_prime = sang(1000)


# # t = int(input())
# # for _ in range(t):
# #     a = int(input())
# #     b = int(input())
# #     seg = segment_sieve(a,b)
# #     cnt = 0
# #     for i in range(len(seg)):
# #         num = i + a
# #         if digitPrime(num) and seg[i] and is_prime[sumPrime(num)]:
# #             cnt += 1

# #     print(cnt)
        


# # # ***LÀM LẠI ***
# # def sang(n):
# #     is_prime = [True]*(n+1)
# #     is_prime[0] = is_prime[1] = False
# #     for i in range(2, int(n ** 0.5)):
# #         if is_prime[i]:
# #             for j in range(i*i, n + 1, i):
# #                 is_prime[j] = False
# #     return is_prime


# # def segment_sieve(L, R):
# #     limit = int(R ** 0.5) + 1
# #     base = sang(limit)
# #     primes = [i for i in range(2, limit + 1) if base[i]]
# #     is_prime = [True] * (R - L + 1)
# #     for p in primes:
# #         start =  max(p*p, ((L + p - 1)//p)*p)
# #         for j in range(start, R+1, p):
# #             is_prime[j - L] =False
# #     if L == 1:
# #         is_prime[0] = False
# #     return is_prime

# # def digitPrime(n):
# #     while n:
# #         r = n % 10
# #         if r not in [2,3,5,7]:
# #             return False
# #         n//= 10
# #     return True

# # def sumdigit(n):
# #     s = 0
# #     while n:
# #         s += n%10
# #         n//= 10
# #     return s

# # MAX_N = 1000
# # is_prime = sang(MAX_N)

# # t = int(input())
# # for _ in range(t):
# #     a = int(input())
# #     b = int(input())
# #     seg = segment_sieve(a,b)
# #     cout = 0
# #     for i in range(len(seg)):
# #         num  = i + a
# #         if digitPrime(num) and seg[i] and is_prime[sumdigit(num)]:
# #             cout +=  1
# #     print(cout)


def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
for i in range(a, b):
    for j in range(i + 1, b + 1):
        if gcd(i, j) == 1:
            print([i,j])
    print()
    
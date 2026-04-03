# check so ngto 
# def sieve(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
#     for i in range(2, int(n**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i*i, n + 1, i):
#                 is_prime[j] = False
#     return is_prime

# t = int(input())
# arr = [int(input()) for _ in range(t)]
# is_prime = sieve(max(arr))
# for n in arr:
#     print("YES" if is_prime[n] else "NO")        

# ____________________________________________________
# ktra so nguyen to va chu so cũng là số nguyên tố
# viết chương trình đếm xem trong đoạn a,b  có bao nhiêu số là snt và tất cả các chữ số đều là số nguyên tố

def sang(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def segment_sieve(L, R):
    Limit = int(R ** 0.5) + 1
    primes = sang(Limit)
    is_prime = 
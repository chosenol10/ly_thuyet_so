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

a = list(map(int, input().split()))
res = 0
for i in a:
    res += i % 3
res= res % 3
print(res)
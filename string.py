# A - Z: 65 - 90
# a - z: 97 - 122
# 0 - 9: 48 - 57

# islower()
# isupper()
# isdigit()
# isalpha()
# lower()
# upper()

# string co the cong 2 chuoi lai voi nhau  vd "A" + "B"  = 

# s = input()
# seen = {}
# for i in s:
#     if i == " ":
#         continue
#     if i not in seen:
#         seen[i] = 1
#     else:
#         seen[i] += 1

# for k, v in seen.items():
#     print(k, v)

# res = 0
# ans = ""
# for i in seen:
#     if seen[i] > res:
#         res = seen[i]
#         ans = i

# print(ans, res)


# s = input()
# sum = 0
# for i in s:
#     sum += int(i)
# print(sum)


# s = input()
# seen = {}
# for i in s:
#     if i == " ":
#         continue
        
#     if i not in seen:
#         seen[i] = 1

#     else:
#         seen[i] += 1

# res = 0
# ans = ""
# for i in seen:
#     if res < seen[i]:
#         res= seen[i]
#         ans = i
# print(ans)


# s1 = input()
# s2 = s1.lower()
# print(s1)
# print(s2)
# print("YES") if s1 == s2 else print("NO")
    
# s1 = input().lower()
# res = set()
# for i in s1:
#     if "a" <= i <= "z":
#         res.add(i)

# print("YES" if len(res) == 26 else "NO")



# =========nhập 1 xâu phải thay đổi 1 kí tự để xâu đó đối xứng========
# s1 = input()
# count = 0

# for i in range(len(s1) // 2):
#     if s1[i] != s1[len(s1) - i - 1]:
#         count += 1

# if count == 1:
#     print("YES")
# else:
#     print("NO")


# s1 = input().split()
# print("\n".join(s1))

# def check(s):
#     for ch in s:
#         if not ch.isupper():
#             return False
#     return True

# t = int(input())
# for _ in range(t):

#     s = input().split()
#     for i in s:
#         if check(i):
#             print(i, end=" ")
#     print()

# def check (a, b):
#     if len(a) != len(b):
#         return len(a) < len(b)
#     return a < b

# s = input()

# a = "".join(sorted(s), check)
# print(a)


t = int(input())
for _ in range(t):
    name = input().split()
    fixName = []
    for i in name:
        # i = i.lower().capitalize()
        fixName.append(i.lower().capitalize())

    print(" ".join(fixName))
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

s = input()
a = [0] * 256   
for i in range(len(s)):
    a[s[i]] += 1
    print(a[s[i]])

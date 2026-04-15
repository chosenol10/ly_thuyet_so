# sinh nhi phan
# sinh to hop 
# sinh hoan vi
# sinh phan hoach

x = [0] * 100
n = int(input())
# k = int(input())
ok = True

# def check():
#     for i in range(1, n + 1):
#         if x[i] == 0:
#             return False 
#     return True
# check -> ok
    
# ok  = True
# def sinh():
#     global ok
#     i = n    # i la bit tu n vd 110  thi i = 0 111 thi i = 1
#     while (i >= 1 and x[i] == 1):
#         x[i] = 0
#         i -= 1  
#     if i == 0:
#         ok = False
#     else:
#         x[i] = 1


# while(ok):
#     for i in range(1, n + 1):
#         print(x[i], end= " ")
    
#     print()
#     sinh()
# for i in range(1, n + 1):
#     print(x[i], end=" ")

        
# def init():
#     global k
#     for i in range(1, n + 1):
#         x[i] = i
    
# def sinh():
#     global n, k, ok
#     i  =  k    #chon bit cuoi cung

#     while (i >= 1 and x[i] == n - k + i):
#         i -= 1
    
#     if i == 0:
#         ok = False   # ket thuc thuat toan
#     else:
#         x[i] += 1
#         for j in range(i + 1, k + 1):
#             x[j] = x[j - 1] + 1

# init()
# while(ok):
#     for i in range(1, k + 1):
#         print(x[i], end=" ")
#     print()
#     sinh()
    

# =========hoan vi==========
def init():
    for i  in range(1, n + 1):
        x[i] = i
    
def sinh():
    global n, ok
    i = n - 1
    while (i >= 1 and x[i] > x[i + 1]):
        i -= 1
    if i == 0:
        ok = False
    else:
        j = n
        while (x[i] > x[j]):
            j -= 1
        x[i], x[j] = x[j], x[i]
        x[i+1:n+1] = reversed(x[i+1:n+1])

init()
while(ok):
    for i in range(1, n + 1):
        print(x[i], end=" ")
    print()
    sinh()
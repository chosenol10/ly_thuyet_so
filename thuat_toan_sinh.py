# sinh nhi phan
# sinh to hop 
# sinh hoan vi
# sinh phan hoach

x = [0] * 100
n = int(input())

# def check():
#     for i in range(1, n + 1):
#         if x[i] == 0:
#             return False 
#     return True
# check -> ok
    
ok  = True
def sinh():
    global ok
    i = n    # i la bit tu n vd 110  thi i = 0 111 thi i = 1
    while (i >= 1 and x[i] == 1):
        x[i] = 0
        i -= 1  
    if i == 0:
        ok = False
    else:
        x[i] = 1


while(ok):
    for i in range(1, n + 1):
        print(x[i], end= " ")
    
    print()
    sinh()
# for i in range(1, n + 1):
#     print(x[i], end=" ")

        
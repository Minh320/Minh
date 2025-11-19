# Bài S4
n = int(input("Nhập n: "))
S4 = 0
for k in range(0, n+1):    
    S4 += k / (k + 2)      
print("S4 =", S4)
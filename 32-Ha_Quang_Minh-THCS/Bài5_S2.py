#Bài S2
n = int(input("Nhập số n : "))
S2 = 1  
for i in range(1, n):
    S2 *= i
print(f"S2 = {S2}")
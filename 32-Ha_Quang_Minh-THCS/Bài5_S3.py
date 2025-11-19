#Bài S3
n = int(input("Nhập n: "))
S3 = 0                    
for k in range(1, n+1):        
    i = ((-1) ** (k + 1)) / k  
    S3 += i                 
print("S3 =", S3)
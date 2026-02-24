# Tính các phép tính sau
# s1 = 1 + 2 + 3 + ... + n
# s2 = 1*2*3*4*...*n
# s3 = 1 - 1/2 - 1/3 - 1/4 + --- + ((-1)**n /n)
#s4 = sum(k / k+2) với k = 0

n = int(input("Nhập n: "))

s1 = 0
s2 = 1
s3 = 0
s4 = 0

for i in range(1, n + 1):
    s1 += i
    s2 *= i
    s3 += (-1)**(i + 1) / i
    s4 += i / (i + 2)

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")
print(f"s4 = {s4}")
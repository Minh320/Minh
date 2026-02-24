def so_nguyen_to(n):
    if n < 2:
        return False
    limit = int(n**0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True
print(so_nguyen_to(7))
ds = [x for x in range(100, 501) if so_nguyen_to(x)]
print(ds)

"""
Nhập vào một số nguyên dương n, viết hàm kiểm tra xem n có phải là số
nguyên tố hay không? Sau đó in ra các số nguyên tố trong khoảng [100, 500].
"""

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
    


n = int(input("nhập số nguyên dương n: "))

print("n là số nguyên nguyên tố" if kiem_tra_so_nguyen_to(n) else"n không phải là số nguyên tố")

for i in range(100, 501):
    if kiem_tra_so_nguyen_to(i):
        print(i)
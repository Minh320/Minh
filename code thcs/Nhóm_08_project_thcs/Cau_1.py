# Hàm kiểm tra số nguyên tố
def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# Hàm kiểm tra số Sophie Germain
def sophie_germain(n):
    if nguyen_to(n) and nguyen_to(2*n + 1):
        return True
    return False
# Chương trình chính
K = int(input("Nhập K: "))
tong = 0
print("Các số Sophie Germain ≤", K, ":")
for i in range(2, K + 1):
    if sophie_germain(i):
        print(i, end=" ")
        tong = tong + i
print("\nTổng =", tong)





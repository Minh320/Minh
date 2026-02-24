def la_so_du_thua(n):
    if n <= 1:
        return False
    
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    
    return tong > n


def tim_du_thua_max(K):
    for i in range(K, 1, -1):
        if la_so_du_thua(i):
            return i
    return None


# ===== CHƯƠNG TRÌNH CHÍNH =====
K = int(input("Nhập số nguyên dương K: "))

kq = tim_du_thua_max(K)
if kq:
    print("Số Dư Thừa lớn nhất ≤", K, "là:", kq)
else:
    print("Không có số Dư Thừa nào ≤", K)

def so_hoan_hao(n):
    if n <= 1:
        return False
    s = 1
    r = int(n**0.5)
    for i in range(2, r+1):
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
    return s == n

def tinh_tong_so_hoan_hao(a, b):
    a, b = int(a), int(b)
    if a > b:
        a, b = b, a
    total = 0
    for x in range(max(1, a), b+1):
        if so_hoan_hao(x):
            total += x
    return total
print(so_hoan_hao(6))              
print(so_hoan_hao(28))            
print(tinh_tong_so_hoan_hao(5, 30)) 




"""
Viết hàm tinh_tong_so_hoan_hao(a, b) nhận vào hai số nguyên dương a và b
(với a <= b). Hàm sẽ tính và trả về tổng của tất cả các số hoàn hảo trong khoảng từ a
đến b.
"""


def tinh_tong_so_hoan_hao(a,b):
    tong_perfect = 0
    tong_uoc = 1

    for x in range(a,b):
        if x < 2:
            continue

        tong_uoc = 1
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                tong_uoc += i
                if i != x // i:
                    tong_uoc += x // i

        if tong_uoc == x:
            tong_perfect += x

    return tong_perfect


a = int(input("nhập a: "))
b = int(input("nhập b: "))

check = tinh_tong_so_hoan_hao(a,b)

print(check)
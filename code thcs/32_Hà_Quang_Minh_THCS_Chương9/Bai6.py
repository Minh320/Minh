"""
Viết hàm la_so_nguyen_to(n) nhận vào một số nguyên n và trả về True nếu n
là số nguyên tố, ngược lại trả về False. Viết hàm in_so_nguyen_to_trong_khoang(a,
b) nhận vào hai số nguyên a và b. Sử dụng hàm la_so_nguyen_to để in ra tất cả các
số nguyên tố trong khoảng từ a đến b.
"""


def la_so_nguyen_to(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

n = int(input("nhập số nguyên dương n: "))
check = la_so_nguyen_to(n)
print(check)
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
ucln = 1
for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        ucln = i
print(f"UCLN là: {ucln}")
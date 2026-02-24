# Viết chương trình nhập vào 2 số bất kì, tìm ước chung lớn nhất của 2 số đó

a, b = map(int, input("Nhập hai số nguyên > 0, cách nhau bởi dấu cách: ").split())

while b != 0:
    a, b = b, a % b
print(f"Ước chung lớn nhất của hai số đã cho là: {a}")

a = int(input("Nhập số năm: "))
# Năm nhuận
b = (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
print(f"Năm {a} là năm nhuận: {b}")
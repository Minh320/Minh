# Nhập tử số và mẫu số
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
# Tìm UCLN bằng vòng lặp từ min(tu, mau) xuống 1
for i in range(min(tu, mau), 0, -1):  # bắt đầu từ min(tu, mau), giảm dần đến 1
    if tu % i == 0 and mau % i == 0:
        ucln = i
        break   # tìm được UCLN lớn nhất → dừng vòng lặp
# Chia tử số và mẫu số cho UCLN để tối giản
tu = tu // ucln
mau = mau // ucln
# In kết quả
print(f"Phân số tối giản: {tu}/{mau}")
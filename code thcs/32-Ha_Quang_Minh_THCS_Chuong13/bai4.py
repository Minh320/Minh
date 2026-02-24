# -*- coding: utf-8 -*-

# 1) Tạo file san_pham.txt
f = open("san_pham.txt", "w", encoding="utf-8")
f.write("ID, Tên sản phẩm, Giá\n")
f.write("1, Laptop, 1200\n")
f.write("2, Chuột máy tính, 25\n")
f.write("3, Bàn phím, 75\n")
f.close()

# 2) Nhập ID cần cập nhật
id_can_sua = input("Nhập ID cần cập nhật: ").strip()

# 3) Nhập giá mới
gia_moi = input("Nhập giá mới: ").strip()

# 4) Đọc file và cập nhật
f = open("san_pham.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

ds_moi = []
ds_moi.append(lines[0])  # giữ dòng tiêu đề

for i in range(1, len(lines)):
    parts = lines[i].strip().split(",")
    id_sp = parts[0].strip()
    ten_sp = parts[1].strip()
    gia_sp = parts[2].strip()

    if id_sp == id_can_sua:
        ds_moi.append(f"{id_sp}, {ten_sp}, {gia_moi}\n")
    else:
        ds_moi.append(lines[i])

# 5) Ghi đè lại file
f = open("san_pham.txt", "w", encoding="utf-8")
f.writelines(ds_moi)
f.close()

print("Xong!")
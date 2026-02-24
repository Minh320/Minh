# Bài 6: Tạo CSV + đọc bằng csv.DictReader + lọc lương > 50000

import csv

# 1,2) Tạo file nhan_vien.csv và ghi dữ liệu
with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Lương"])
    writer.writerow([1, "An", 45000])
    writer.writerow([2, "Bình", 52000])
    writer.writerow([3, "Chi", 80000])
    writer.writerow([4, "Dũng", 50000])

# 3,4) Đọc bằng DictReader và in nhân viên lương > 50000
with open("nhan_vien.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        luong = float(row["Lương"])
        if luong > 50000:
            print(f"ID: {row['ID']}, Tên: {row['Tên']}, Lương: {row['Lương']}")
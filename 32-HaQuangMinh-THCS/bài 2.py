a = int(input(" Nhập tổng số kẹo: " ))
b = int(input("Nhập số học sinh: "))
# Nhập số kẹo mỗi học sinh nhận được
keo_moi_hoc_sinh = a // b
# Nhập số kẹo còn thừa
so_keo_thua = a % b
# In kết quả
print(f"Mỗi học sinh nhận được: {keo_moi_hoc_sinh} viên kẹo")
print(f"Số kẹo còn thừa: {so_keo_thua}")
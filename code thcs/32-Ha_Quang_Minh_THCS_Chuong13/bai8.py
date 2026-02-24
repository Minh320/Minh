import os

# 1) Tạo thư mục temp_files
os.makedirs("temp_files", exist_ok=True)

# 2) Tạo file temp_files/file.txt
open("temp_files/file.txt", "w", encoding="utf-8").close()

# 3) Đổi tên file.txt -> new_file.txt (trong temp_files)
os.rename("temp_files/file.txt", "temp_files/new_file.txt")

# 4) Di chuyển new_file.txt ra thư mục hiện tại
os.rename("temp_files/new_file.txt", "new_file.txt")

# 5) Xóa thư mục temp_files (lúc này đã rỗng)
os.rmdir("temp_files")

print("Xong!")
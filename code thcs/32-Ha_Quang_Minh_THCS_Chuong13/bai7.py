# Bài 7: Tạo cấu trúc my_project và in ra danh sách file/thư mục

import os

root = "my_project"

# 1) Tạo thư mục
os.makedirs(os.path.join(root, "src"), exist_ok=True)
os.makedirs(os.path.join(root, "docs"), exist_ok=True)
os.makedirs(os.path.join(root, "data"), exist_ok=True)

# 2) Tạo file rỗng
open(os.path.join(root, "src", "main.py"), "w", encoding="utf-8").close()
open(os.path.join(root, "docs", "README.md"), "w", encoding="utf-8").close()
open(os.path.join(root, "data", "input.txt"), "w", encoding="utf-8").close()

# 3) In cấu trúc (dùng os.listdir)
print(root + "/")
for folder in os.listdir(root):
    path_folder = os.path.join(root, folder)
    if os.path.isdir(path_folder):
        print("  " + folder + "/")
        for item in os.listdir(path_folder):
            print("    " + item)
'''
tich = 1
ds = range(1, 10)
for i in ds:
    tich = tich * i
print(tich)
'''

'''
name_age = "Hà Quang Minh"
print(name_age.lower())
print(name_age.upper())
print(name_age.strip())
print(name_age.replace("Hà","Nguyễn"))
print(name_age.split())
print(name_age.count("n"))
'''

'''
x = "abc123"
print(x.isdigit())
print(x.isalpha())
print(x.isupper())
print(x.islower())

x = "123"
print(x.isdigit())
print(x.isalpha())
print(x.isupper())
print(x.islower())
'''

'''
#Nối chuỗi
str1 = "nva"
str2 = "18tuoi"
x = str1 + str2
print(x)
y = " ".join([str1,str2])
print(y)
'''

'''
#ma trận
matrix = [[1, 2, 4, 5], [3, 5, 5, 6]]
print(matrix)
'''
'''
Bài tập: Tạo một module để tính toán các phép toán cơ bản:
Tạo file phep_toan.py và định nghĩa 4 hàm:
cong(a, b): Trả về tổng của hai số.
tru(a, b): Trả về hiệu của hai số.
nhan(a, b): Trả về tích của hai số.
chia(a, b): Trả về thương của hai số.
Tạo một file khác, main.py, trong cùng thư mục.
Trong main.py, sử dụng cú pháp import phep_toan để nhập module.
Gọi các hàm từ module đã nhập để thực hiện các phép tính và in kết quả ra màn hình.


Bài tập: Xây dựng một package để quản lý các module chuyển đổi đơn vị:
Tạo một thư mục chuyen_doi làm package.
Trong thư mục chuyen_doi, tạo file __init__.py.
Tạo module khoi_luong.py với một hàm kg_sang_gam(kg) để chuyển đổi kilogram sang gram.
Tạo module do_dai.py với một hàm met_sang_cm(m) để chuyển đổi mét sang centimet.
Tạo file tinh_toan.py bên ngoài package chuyen_doi.
Trong tinh_toan.py, sử dụng cú pháp from ... import ... để nhập các hàm từ package đã tạo và gọi các hàm này để kiểm tra kết quả.

Bài tập: Import một module từ một thư mục khác:
Tạo hai thư mục: du_an và thu_muc_ngoai.
Trong thư mục thu_muc_ngoai, tạo file tien_ich.py với một hàm in_thong_tin(ho_ten, tuoi).
Trong thư mục du_an, tạo file chuong_trinh_chinh.py.
Trong chuong_trinh_chinh.py, sử dụng sys.path.append() để thêm đường dẫn của thư mục thu_muc_ngoai vào danh sách tìm kiếm của Python.
Sử dụng cú pháp import tien_ich và gọi hàm in_thong_tin() từ module đã nhập.

https://docs.python.org/3/library/index.html
'''

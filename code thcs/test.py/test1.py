'''
Bài 1: Cho hai biến x = 15 và y = 20. Kiểm tra xem x có nhỏ hơn y hay không.
Bài 2: Cho hai biến a = 5 và b = 5. Kiểm tra xem a có bằng b hay không.
Bài 3: Cho hai chuỗi chuoi1 = "Python" và chuoi2 = "python". Kiểm tra xem hai chuỗi này có bằng nhau không. (Lưu ý: Python phân biệt chữ hoa và chữ thường).
'''

'''
# bài 1
x =15
y = 20
print(x < y)
# bài 2
a =5 
b =5
print(a == b)
# bài 3
chuoi1 = "Python"
chuoi2 = "python"
print(chuoi1 == chuoi2)
'''

'''
Bài 1: Cho x = 10 và y = 20. Kiểm tra xem x có lớn hơn 5 và y có nhỏ hơn 25 không.
Bài 2: Một học sinh được xếp loại giỏi nếu điểm trung bình lớn hơn hoặc bằng 8.0 và không có môn nào dưới 6.5. Cho diem_trung_binh = 8.2 và diem_mon_thap_nhat = 6.0. Kiểm tra học sinh đó có được xếp loại giỏi không.
'''

'''
# bài 1
x = 10
y = 20
print(x > 5 and y < 25)
# bài 2 
diemtrungbinh = 8.0
diemmonthapnhat = 6.0
gioi = (diemtrungbinh >= 8.0) and (diemmonthapnhat > 6.5)
print(gioi)
'''
'''
toán tử ddihj danh
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b) # True: a và b có giá trị bằng nhau và bằng [1, 2, 3]
print(a is b) # Fale: a và b có cùng trở đến 1 vị trí trong ô nhớ hay không --> Không
print(a is c) # True: a và b có cùng trở đến 1 vị trí trong ô nhớ hay không --> Có

C += [25]  # thêm một giá mới 25 vào trong tập hợp 
'''


'''
i = int(input("Nhập i : "))
if i % 2 == 0 :
    print("là số chẵn") #TRUE
else: 
    print("không là số chẵn")
'''

'''
i = int(input("Nhập i : "))
if i % 2 == 0 : 
    i = i + 2     
else:
    i = i + 1
print(f"Giá trị i là: {i}")
'''

'''
i = int(input("Nhập i: "))
if i % 2 == 0 :
    i = i + 2 #TRUE
    if i % 3 == 0 :
        print("i là số cần tìm")
    elif i % 3 != 0 :
        print(f"Giá trị của i là: {i}")
else:
    i = i + 1
print(f"Giá trị i là: {i}")
'''
'''
print(list(range(5)))

print(list(range(0, 5, 1))
'''
'''
i = 3
while (i + 1) % 3 == 0:
     i = i + 2
print(i)
'''

'''
for i in range(5,31):
    if(i % 5 == 0):
        print(i)
'''
'''
i =  5 
while i <= 30:
    if i % 5 == 0:
        print(i)
    i += 1
'''


'''
def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang/chieu_cao**2
    return bmi
# sử dụng vòng lặp for để nhập DL cho 5 người từ ban phím
for i in range(0, 5):
    heigh = float(input("Nhập chiều cao (m): "))
    weight = float(input("Nhập cân nặng (kg): "))
    bmi = tinh_bmi(heigh, weight)

    print(f"Chỉ số bmi {i+1} là: {bmi}")
'''




'''
def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang/chieu_cao**2
    return bmi
# sử dụng vòng lặp for để nhập DL cho 5 người từ ban phím
i = 0
while i < 5:
    heigh = float(input("Nhập chiều cao (m): "))
    weight = float(input("Nhập cân nặng (kg): "))
    bmi = tinh_bmi(heigh, weight)

    print(f"Chỉ số bmi số {i+1} là: {bmi}")
    i += 1
'''



'''
def thay_doi_phan_tu(lst):    
	lst[0] = 20
	print(f"Bên trong hàm: {lst}")
danh_sach = [10, 20, 30]
print(f"Trước khi gọi: {danh_sach}")
thay_doi_phan_tu(danh_sach)
print(f"Sau khi gọi: {danh_sach}")
'''

'''
#hàm tính tổng của 2 số
def tinh_tong(x, y):
    return x+y

kqua = tinh_tong(3, 6)
print(kqua)
'''

'''
def gioi_thieu(ten, tuoi, thanh_pho):  	
	return f"{ten}, {tuoi} tuổi, sống tại {thanh_pho}"

x = gioi_thieu("Minh", 18, "Hà Nội")
print(x)
'''

'''
#hàm tính tổng của 2 số
def tinh_tong(x="hi"):
    return x

a = tinh_tong()
print(a)
'''
'''
# trường hợp: tham số bb + tham số mặc định
def tinh_tong(a, b, x="hi", y="hello"):
    return a + b

c = tinh_tong("Hello", "Minh")
print(c)
'''
'''
# hãy cho biết những số chẵn nằm trong khoảng từ 1 đến 8
for i in range l(1, 9):
    if i % 2 == 0:
     print(i)
'''


'''
#BT: hãy tính bình phương của các số: 2,4,6,8,10 sử dụng hàm map()
#    Trong đó, có thể khai báo danh sách các số trên theo kiểu: [2,4,6,8,10] 
#        hoặc sử dụng hàm range(...)
def binh_phuong(x):
    return x**2
result = list(map(binh_phuong, [2,4,6,8,10]))
print(result)
'''



'''
def la_so_chan(x):
    return x%2==0
ds = range(1, 9)
kqua = filter(la_so_chan, ds)
print(list(kqua))
'''



'''
def loc_diem(x):
    return x >= 7.5
ds = [8.5, 4.0, 7.5, 9.0, 3.5, 6.0]
kqua = filter(loc_diem, ds)
print(list(kqua))
'''
'''
from functools import reduce
ds = range(1, 10)

def tinh_tich(x, y):
    return x*y

kqua = reduce(tinh_tich, ds)
print(kqua)
'''


'''
Các bước quá trình của reduce:
+) B1: hàm tinh_tich sẽ lấy 2 phâng tử đầu tiên của ds --> 1 và 2
       sau đó hàm tinh_tich sẽ thực hiện nhân 2 số: 1*2=2 ==> tả về kết quả là 2
       tại đây, giá trị 2 sẽ được thay thế vị trí cho số 1 và 2 trong ds
+) B2: ds khi này sẽ được cập nhật lại thnhad [2,3,4,...,9]
       reduce sẽ gọi hàm tinh_tich, hàm tinh_tich sẽ lấy 2 phần tử đầu tiên của ds --> 2 và 3
       sau đó hàm tinh_tich 
'''
'''
# sử dụng vong lặp for để giải quyết bài toán trên
tich = 1
ds = range(1, 10)
for i in ds:
    tich = tich * i
print(tich)
'''

'''
# Bt: viết 1 hàm ẩn (sử dụnglambda) đơn giản để thực hiện tính tổng của 3 só
tinh_tong = lambda x,y,z: x+y+z
print(tinh_tong(1,2,3))

# lambda có thế đucợ sử dụng kết hợp với các hàm khác nhau như map, filter, reduce
# kết hợp lambda với map:
# cú pháp của map" map(function, sequence)
# tạo hàm trả về bình thường của các số tương ứng trong khoản 1 đến 5
a = map(lambda x: x**2, range(1,6))
print(list(a))

# kết hợp lambda vs filter:
#cú pháp của filter: filter(finction, sequence)
# tạo hàm trả về số lẻ trong khoảng 1 đến 5 
b = filter(lambda x: x%2!=0, range(1,6))
print(list(b))


#kết hợp lambda vs reduce
#cú pháp của reduce: reduce(function, sequence)
#tinh tích cyae các phần tử nằm trong khoảng 1 đến 5
from functools import reduce
c = reduce(lambda x,y: x*y, range(1,6))
print(c)
'''



# Hàm kiểm tra số nguyên tố
def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# Hàm kiểm tra số Sophie Germain
def sophie_germain(n):
    if nguyen_to(n) and nguyen_to(2*n + 1):
        return True
    return False
# Chương trình chính
K = int(input("Nhập K: "))
tong = 0
print("Các số Sophie Germain ≤", K, ":")
for i in range(2, K + 1):
    if sophie_germain(i):
        print(i, end=" ")
        tong = tong + i
print("\nTổng =", tong)





import csv
import os

FILE = "files/ds_benhnhan.csv"

def khoi_tao_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Ma", "Ten", "LoaiPhong", "SoNgay", "TongVienPhi"])

def nhap_benh_nhan():
    ma = input("Mã bệnh nhân: ")
    ten = input("Tên bệnh nhân: ")
    loai = int(input("Loại phòng (1-Dịch vụ, 2-Thường): "))
    ngay = int(input("Số ngày nằm viện: "))

    return {
        "Ma": ma,
        "Ten": ten,
        "LoaiPhong": loai,
        "SoNgay": ngay,
        "TongVienPhi": 0
    }

def tinh_vien_phi(bn):
    if bn["LoaiPhong"] == 1:
        gia = 1000000
    else:
        gia = 200000

    tong = bn["SoNgay"] * gia

    if bn["SoNgay"] >= 10:
        tong = tong * 0.9

    bn["TongVienPhi"] = int(tong)
    return bn

def luu_file(ds):
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for bn in ds:
            writer.writerow([
                bn["Ma"],
                bn["Ten"],
                bn["LoaiPhong"],
                bn["SoNgay"],
                bn["TongVienPhi"]
            ])

def sap_xep(ds):
    ds.sort(key=lambda x: x["TongVienPhi"], reverse=True)


def hien_thi(ds):
    for bn in ds:
        print(bn)

from libs.vienphi import *

ds = []
khoi_tao_file()

while True:
    print("\n1. Nhập")
    print("2. Tính viện phí")
    print("3. Lưu file")
    print("4. Sắp xếp & Hiển thị")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        bn = nhap_benh_nhan()
        ds.append(bn)

    elif chon == "2":
        for i in range(len(ds)):
            ds[i] = tinh_vien_phi(ds[i])

    elif chon == "3":
        luu_file(ds)

    elif chon == "4":
        sap_xep(ds)
        hien_thi(ds)

    elif chon == "0":
        break


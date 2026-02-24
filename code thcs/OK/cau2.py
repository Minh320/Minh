
from libs.thuvien_kho import *

ds_hang_hoa = []
Khoi_tao_file()

while True:
    print("1. Nhập")
    print("2. Tính tiền")
    print("3. Lưu")
    print("4. Sắp xếp & Hiển thị")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        ds_hang_hoa=nhap_hang_hoa()

    elif chon == "2":
        tinh_thanh_tien(ds_hang_hoa)
        print("Đã tính xong thành tiền")

    elif chon == "3":
        luu_file(ds_hang_hoa)
        print("Đã lưu vào file")

    elif chon == "4":
        sap_xep_giam_dan(ds_hang_hoa)
        hien_thi(ds_hang_hoa)

    elif chon == "0":
        print("Thoát khỏi chương trình")
        break

    else:
        print("Chọn sai chức năng")

'''
from libs.thuvien_kho import *

ds_hang = []
khoi_tao_file()

while True:
    print("\n===== MENU =====")
    print("1. Nhập thông tin hàng hóa")
    print("2. Tính thành tiền")
    print("3. Lưu vào file")
    print("4. Sắp xếp & Hiển thị")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        ds_hang = nhap_hang()

    elif chon == "2":
        tinh_thanh_tien(ds_hang)
        print("Đã tính xong thành tiền.")

    elif chon == "3":
        luu_file(ds_hang)
        print("Đã lưu vào file.")

    elif chon == "4":
        sap_xep_giam_dan(ds_hang)
        hien_thi(ds_hang)

    elif chon == "0":
        print("Kết thúc chương trình.")
        break

    else:
        print("Chọn sai chức năng!")
'''
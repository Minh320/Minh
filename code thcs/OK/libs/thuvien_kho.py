
import os
import csv

FILE = "files/ds_hang.csv"

def Khoi_tao_file():
    if not os.path.exists("files"):
        os.makedirs("files")


    if not os.path.exists("files"):
        with open(FILE, "w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["MaHang","TenHang","SoLuong","DonGia"])

def nhap_hang_hoa():
    ds = []
    n = int(input("Nhập số lượng hàng: "))

    for i in range(n):
        print(f"\nHàng thứ {i +1}")
        ma = input("Mã hàng: ")
        ten = input("Tên hàng: ")
        soluong = int(input("Số lượng: "))
        gia = float(input("Đơn Giá: "))

        hang ={
            "MaHang":ma,
            "TenHang":ten,
            "SoLuong":soluong,
            "DonGia":gia
        }
        ds.append(hang)

    return ds

def tinh_thanh_tien(ds):
    for hang in ds:
        thanh_tien = hang["SoLuong"] * hang["DonGia"]
        if hang["SoLuong"] >= 50:
            thanh_tien *= 0.9
        hang["ThanhTien"] = thanh_tien

def luu_file(ds):
    with open(FILE, "a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        for hang in ds:
            writer.writerow([
                hang["MaHang"],
                hang["TenHang"],
                hang["SoLuong"],
                hang["DonGia"],
                hang["ThanhTien"]
            ])

def sap_xep_giam_dan(ds):
    ds.sort(key=lambda x: x["ThanhTien"], reverse = True)

def hien_thi(ds):
    print("\nDANH SÁCH HÀNG HÓA")
    for hang in ds:
        print(hang)


'''
import csv
import os

FILE = "files/ds_hang.csv"


# 1. Khởi tạo file
def khoi_tao_file():
    if not os.path.exists("files"):
        os.makedirs("files")

    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["MaHang", "TenHang", "SoLuong", "DonGia", "ThanhTien"])


# 2. Nhập thông tin hàng hóa
def nhap_hang():
    ds = []
    n = int(input("Nhập số lượng hàng: "))

    for i in range(n):
        print(f"\nHàng thứ {i+1}")
        ma = input("Mã hàng: ")
        ten = input("Tên hàng: ")
        sl = int(input("Số lượng: "))
        dg = float(input("Đơn giá: "))

        hang = {
            "MaHang": ma,
            "TenHang": ten,
            "SoLuong": sl,
            "DonGia": dg
        }
        ds.append(hang)

    return ds


# 3. Tính thành tiền
def tinh_thanh_tien(ds):
    for hang in ds:
        thanh_tien = hang["SoLuong"] * hang["DonGia"]
        if hang["SoLuong"] >= 50:
            thanh_tien *= 0.9
        hang["ThanhTien"] = thanh_tien


# 4. Lưu danh sách vào file
def luu_file(ds):
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for hang in ds:
            writer.writerow([
                hang["MaHang"],
                hang["TenHang"],
                hang["SoLuong"],
                hang["DonGia"],
                hang["ThanhTien"]
            ])


# 5. Sắp xếp giảm dần theo Thành tiền
def sap_xep_giam_dan(ds):
    ds.sort(key=lambda x: x["ThanhTien"], reverse=True)


# 6. Hiển thị danh sách
def hien_thi(ds):
    print("\nDANH SÁCH HÀNG HÓA")
    for hang in ds:
        print(hang)
'''
import csv
import os

FILE = "files/ds_benhnhan.csv"

def khoi_tao_file():
    """Khởi tạo file CSV nếu chưa tồn tại"""
    if not os.path.exists("files"):
        os.makedirs("files")
    
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Ma", "Ten", "LoaiPhong", "SoNgay", "TongVienPhi"])
        print(f"Đã khởi tạo file {FILE}")
    else:
        print(f"File {FILE} đã tồn tại")

def nhap_danh_sach_benh_nhan():
    """Nhập danh sách bệnh nhân từ bàn phím"""
    ds = []
    print("\n" + "="*50)
    print("NHẬP DANH SÁCH BỆNH NHÂN")
    print("="*50)
    
    while True:
        print(f"\n--- Bệnh nhân thứ {len(ds) + 1} ---")
        ma = input("Mã bệnh nhân (nhập '0' để kết thúc): ").strip()
        
        if ma == "0":
            break
            
        ten = input("Tên bệnh nhân: ").strip()
        
        while True:
            try:
                loai = int(input("Loại phòng (1-Dịch vụ, 2-Thường): "))
                if loai in [1, 2]:
                    break
                else:
                    print("Vui lòng nhập 1 hoặc 2!")
            except ValueError:
                print("Vui lòng nhập số!")
        
        while True:
            try:
                ngay = int(input("Số ngày nằm viện: "))
                if ngay > 0:
                    break
                else:
                    print("Số ngày phải lớn hơn 0!")
            except ValueError:
                print("Vui lòng nhập số!")

        benh_nhan = {
            "Ma": ma,
            "Ten": ten,
            "LoaiPhong": loai,
            "SoNgay": ngay,
            "TongVienPhi": 0
        }
        ds.append(benh_nhan)
        print(f"Đã thêm bệnh nhân {ma} - {ten}")
    
    print(f"\nĐã nhập xong {len(ds)} bệnh nhân")
    return ds

def tinh_vien_phi_cho_danh_sach(ds):
    """Tính tổng viện phí cho toàn bộ danh sách bệnh nhân"""
    print("\n" + "="*50)
    print("TÍNH VIỆN PHÍ CHO BỆNH NHÂN")
    print("="*50)
    
    if not ds:
        print("Danh sách trống! Không có bệnh nhân để tính.")
        return ds
    
    for i, bn in enumerate(ds, 1):#hãm tích hợp để đếm và lặp qua một tập hợp
        # Tính giá phòng
        if bn["LoaiPhong"] == 1:
            gia = 1000000
            loai_phong_text = "Dịch vụ"
        else:
            gia = 200000
            loai_phong_text = "Thường"
        
        # Tính tổng
        tong = bn["SoNgay"] * gia
        
        # Giảm 10% nếu số ngày >= 10
        if bn["SoNgay"] >= 10:
            giam_gia = tong * 0.1
            tong = tong * 0.9
            bn["TongVienPhi"] = int(tong)
            print(f"{i}. {bn['Ma']} - {bn['Ten']}: {bn['SoNgay']} ngày × {gia:,} VNĐ/ngày = {bn['SoNgay'] * gia:,} VNĐ")
            print(f"   (Giảm 10%: -{int(giam_gia):,} VNĐ) → Tổng: {bn['TongVienPhi']:,} VNĐ")
        else:
            bn["TongVienPhi"] = int(tong)
            print(f"{i}. {bn['Ma']} - {bn['Ten']}: {bn['SoNgay']} ngày × {gia:,} VNĐ/ngày = {bn['TongVienPhi']:,} VNĐ")
    
    print(f"\nĐã tính viện phí cho {len(ds)} bệnh nhân")
    return ds

def luu_danh_sach_vao_file(ds):
    """Lưu danh sách bệnh nhân vào file CSV"""
    print("\n" + "="*50)
    print("LƯU DANH SÁCH VÀO FILE")
    print("="*50)
    
    if not ds:
        print("Danh sách trống! Không có dữ liệu để lưu.")
        return
    
    try:
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Ghi header
            writer.writerow(["Ma", "Ten", "LoaiPhong", "SoNgay", "TongVienPhi"])
            # Ghi dữ liệu
            for bn in ds:
                writer.writerow([
                    bn["Ma"],
                    bn["Ten"],
                    bn["LoaiPhong"],
                    bn["SoNgay"],
                    bn["TongVienPhi"]
                ])
        
        print(f"Đã lưu {len(ds)} bệnh nhân vào file: {FILE}")
        
        # Hiển thị thông tin file
        print("\nThông tin file:")
        print(f"- Vị trí: {os.path.abspath(FILE)}")
        print(f"- Dung lượng: {os.path.getsize(FILE)} bytes")
        
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def sap_xep_va_hien_thi(ds):
    """Sắp xếp và hiển thị danh sách bệnh nhân"""
    print("\n" + "="*50)
    print("SẮP XẾP VÀ HIỂN THỊ DANH SÁCH")
    print("="*50)
    
    if not ds:
        print("Danh sách trống! Không có dữ liệu để hiển thị.")
        return
    
    # Sắp xếp giảm dần theo tổng viện phí
    ds_sorted = sorted(ds, key=lambda x: x["TongVienPhi"], reverse=True)
    
    print("\nDANH SÁCH BỆNH NHÂN (Sắp xếp giảm dần theo viện phí):")
    print("-"*80)
    print(f"{'STT':<5} {'Mã BN':<10} {'Tên bệnh nhân':<20} {'Loại phòng':<12} {'Số ngày':<8} {'Tổng viện phí':<15}")
    print("-"*80)
    
    tong_doanh_thu = 0
    for i, bn in enumerate(ds_sorted, 1):
        loai_phong = "Dịch vụ" if bn["LoaiPhong"] == 1 else "Thường"
        tong_vienphi = f"{bn['TongVienPhi']:,} VNĐ"
        tong_doanh_thu += bn['TongVienPhi']
        
        print(f"{i:<5} {bn['Ma']:<10} {bn['Ten']:<20} {loai_phong:<12} {bn['SoNgay']:<8} {tong_vienphi:<15}")
    
    print("-"*80)
    
    # Thống kê
    print("\nTHỐNG KÊ:")
    print(f"Tổng số bệnh nhân: {len(ds_sorted)}")
    print(f"Tổng doanh thu: {tong_doanh_thu:,} VNĐ")
    
    # Phân loại bệnh nhân
    bn_dich_vu = [bn for bn in ds_sorted if bn["LoaiPhong"] == 1]
    bn_thuong = [bn for bn in ds_sorted if bn["LoaiPhong"] == 2]
    
    print(f"- Bệnh nhân phòng dịch vụ: {len(bn_dich_vu)}")
    print(f"- Bệnh nhân phòng thường: {len(bn_thuong)}")
    
    return ds_sorted
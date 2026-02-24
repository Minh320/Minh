# Import module từ thư mục libs
import sys
sys.path.append('libs')
from thuvien_vienphi import *

def main():
    """Chương trình chính chạy tuần tự các bước"""
    print("="*60)
    print("CHƯƠNG TRÌNH QUẢN LÝ VIỆN PHÍ BỆNH NHÂN")
    print("="*60)
    
    # Bước 1: Khởi tạo file
    print("\nBƯỚC 1: KHỞI TẠO FILE DỮ LIỆU")
    khoi_tao_file()
    
    # Bước 2: Nhập danh sách bệnh nhân
    danh_sach = nhap_danh_sach_benh_nhan()
    
    if not danh_sach:
        print("Không có bệnh nhân nào được nhập. Kết thúc chương trình.")
        return
    
    # Bước 3: Tính viện phí
    danh_sach = tinh_vien_phi_cho_danh_sach(danh_sach)
    
    # Bước 4: Lưu vào file
    luu_danh_sach_vao_file(danh_sach)
    
    # Bước 5: Sắp xếp và hiển thị
    danh_sach = sap_xep_va_hien_thi(danh_sach)
    
    print("\n" + "="*60)
    print("CHƯƠNG TRÌNH KẾT THÚC")
    print("="*60)

if __name__ == "__main__":
    main()
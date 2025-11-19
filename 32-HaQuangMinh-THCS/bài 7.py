a = input("Nhập tên đăng nhập: ")
b = input("Nhập mật khẩu: ")
#Kiểm tra quyền truy cập
ten_dang_nhap = "admin" 
mat_khau = "password123"
print("Kết quả : " , a == ten_dang_nhap and b == mat_khau)
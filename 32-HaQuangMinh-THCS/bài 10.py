a = float(input("Nhập mức lương cơ bản trong tháng: "))
b = int(input("Nhập số ngày công trong tháng: "))
#lương một ngày
luong_mot_ngay = a/22
#lương thưởng và lương phạt
tien_thuong = b > 22
tien_phat = b < 22 
#tổng lương tháng
luong_thang = luong_mot_ngay * b
tong_luong_thang = luong_thang + (luong_thang * 0.1 * tien_thuong) - (luong_thang * 0.05 * tien_phat)
print(f"Tổng lương tháng là: {tong_luong_thang} VNĐ")
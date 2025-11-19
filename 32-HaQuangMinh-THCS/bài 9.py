a = float(input("Nhập số kWh điện đã tiêu thụ: "))
#Tính số điện
bac_1 = a > 0 and a <= 100
bac_2 = a > 101 and a <= 200
bac_3 = a > 201 and a <= 300
gia_bac_1 = a * 1.678 
gia_bac_2 = a * 1.734
gia_bac_3 = a * 2.014
tong_tien = (bac_1 * gia_bac_1) + (bac_2 * gia_bac_2) + (bac_3 * gia_bac_3)
print(f"Tổng tiền điện phải trả là : {tong_tien} VNĐ")
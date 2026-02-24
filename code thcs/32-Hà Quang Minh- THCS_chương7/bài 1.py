a = float(input("Nhập giá sản phẩm: "))
b = int(input("Nhập số lượng mua: "))
# Tính tổng chi phí ban đầu
tong_chi_phi_ban_dau = a * b
# Tính thuế
thue = tong_chi_phi_ban_dau * 0.10
# Tính tổng tiền phải trả (bao gồm thuế)
tong_tien_tra = tong_chi_phi_ban_dau + thue
# In kết quả, làm tròn đến 2 chữ số thập phân
print(f"Tổng tiền phải trả là: {tong_tien_tra:.2f}")
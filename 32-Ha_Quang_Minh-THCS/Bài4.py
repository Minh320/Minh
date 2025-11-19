# Nhập số n từ người dùng
n = int(input("Nhập số nguyên n: "))
print(f"Các số nguyên tố nhỏ hơn {n} là:")
# Kiểm tra nếu n nhỏ hơn hoặc bằng 2, vì không có số nguyên tố nào nhỏ hơn
if n <= 2:
    print("Không có số nguyên tố nào thoả mãn.")
else:
    # Vòng lặp ngoài duyệt qua các số từ 2 đến n-1
    for so in range(2, n):
        a = True
        for i in range(2, int(so**0.5) + 1):
            # Nếu so chia hết cho bất kỳ số nào ngoài 1 và chính nó
            if (so % i) == 0:
                a = False 
                break # Thoát khỏi vòng lặp trong ngay lập tức
        if a:
            print(so)
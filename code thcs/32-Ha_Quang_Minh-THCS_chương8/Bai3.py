#Viết chương trình nhập vào mẫu số và tử số của một phân số, trả về kết quả phân số đã tối giản

tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số (khác 0): "))


while mau_so != 0:
    a, b = mau_so, tu_so
    while b != 0:
        a, b = b, a % b
    ucln = a
    mau_so //= ucln
    tu_so //= ucln
    break

if mau_so == tu_so:
    print("Phân số tối giản là: 1")

print(f"Phân số tối giản là: {tu_so}/{mau_so}")
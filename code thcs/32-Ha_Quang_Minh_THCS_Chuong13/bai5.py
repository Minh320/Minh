# Bài 5: Sao chép file (đọc/ghi nhị phân theo từng khối)

nguon = input("Nhập đường dẫn file nguồn: ").strip()
dich  = input("Nhập đường dẫn file đích: ").strip()

kich_thuoc_khoi = 1024  # 1024 byte

with open(nguon, "rb") as f_in, open(dich, "wb") as f_out:
    while True:
        data = f_in.read(kich_thuoc_khoi)
        if data == b"":   # hết file
            break
        f_out.write(data)

print("Đã sao chép xong!")
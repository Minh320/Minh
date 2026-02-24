# Viết hàm chuyen_doi_nhiet_do(do_c) nhận vào nhiệt độ tính bằng độ C và trả về nhiệt độ tương ứng bằng độ F.


def chuyen_doi_nhiet_do(do_c):
    do_f = (do_c * 1.8) + 32
    return do_f


do_c = float(input("nhập nhiệt độ (C): "))
do_f = chuyen_doi_nhiet_do(do_c)
print(F"độ F tương ứng là: {do_f} F")
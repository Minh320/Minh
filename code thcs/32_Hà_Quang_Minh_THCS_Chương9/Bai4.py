def tinh_trung_binh_cong(a, b, c):
    return (a + b + c) / 3
print(tinh_trung_binh_cong(3, 4, 5))  



"""
Viết hàm tinh_trung_binh_cong(a, b, c) nhận vào ba số. Hàm sẽ tính và trả về
giá trị trung bình cộng của chúng.
"""


def tinh_trung_binh_cong(a,b,c):
    average = (a + b + c) / 3
    return average

a, b, c = map(float, input("nhập a b c (cách nhau khoảng trắng): ").split())

average = tinh_trung_binh_cong(a,b,c)
print(f"trung bình của của {a, b, c} là: {average}")
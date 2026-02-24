""" Viết hàm giai_phuong_trinh_bac_nhat(a, b) nhận vào hai hệ số a và b của phương trình ax+b=0. 
Hàm sẽ in ra nghiệm của phương trình hoặc thông báo vô nghiệm/vô số nghiệm. """

def giai_phuong_trinh_bac_nhat(a,b):
    if a != 0:
        x = -b / a
        return f"nghiệm của phương trình là: {x}"
    else:
        if b == 0:
            return "phương trình vô số nghiệm"
        else:
            return "phương trình vô nghiệm"
        
a = float(input(" nhập hệ số a: "))
b = float(input("nhập hệ số b: "))

x = giai_phuong_trinh_bac_nhat(a,b)
print(x)
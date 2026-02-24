s = input("Nhập chuỗi: ")
ket_qua = ""
da_gap_chu = False      # đã gặp ký tự chữ/số chưa
truoc_la_space = False # ký tự trước có phải dấu cách không
for ch in s:
    if ch != " ":                 # gặp chữ hoặc ký tự khác
        ket_qua += ch
        da_gap_chu = True
        truoc_la_space = False
    else:                          # gặp dấu cách
        if da_gap_chu and not truoc_la_space:
            ket_qua += ch          # chỉ thêm 1 dấu cách
            truoc_la_space = True
print(f"Chuỗi sau khi xử lý: {ket_qua}")

"""
Viết chương trình xóa tất cả các khoảng trắng thừa trong một chuỗi (chỉ giữ
lại 1 khoảng trắng giữa các từ)
"""

def is_space(ch):
    return ch == ' ' or ch == '\t' or ch == '\n' or ch == '\r'

s = input("Nhập chuỗi: ")

res = ""
i = 0

while i < len(s) and is_space(s[i]):
    i += 1

in_space = False
while i < len(s):
    ch = s[i]
    if is_space(ch):
        in_space = True
    else:
        if in_space and len(res) > 0:
            res += ' '
        res += ch
        in_space = False
    i += 1

print("Kết quả:", res)
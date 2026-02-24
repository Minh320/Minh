def nhom_sinh_vien_theo_diem(d):
    ket_qua = {}
    for ten in d:
        diem = d[ten]
        if diem in ket_qua:
            ket_qua[diem].append(ten)
        else:
            ket_qua[diem] = [ten]
    return ket_qua
ds = {"duc":9,
      "vinh":8,
      "hiep":8,
      "manh":7,
      "lam":7}
ket_qua = nhom_sinh_vien_theo_diem(ds)
print("Dictionary ban đầu:", ds)
print("Dictionary sau khi nhóm theo điểm:", ket_qua)

'''
Bài 19: Viết chương trình nhóm các sinh viên theo điểm số từ một dictionary có dạng
{'tên': điểm} thành {'điểm': [danh sách tên]}.
'''

n = int(input("Số sinh viên: "))
scores = {}
i = 0
while i < n:
    name = input("Tên: ")
    score = int(input("Điểm: "))
    scores[name] = score
    i += 1

grouped = {}
for name in scores:
    sc = scores[name]
    if sc in grouped:
        grouped[sc].append(name)
    else:
        grouped[sc] = [name]

print("Nhóm theo điểm:")
for sc in grouped:
    print(sc, ":", grouped[sc])
def tim_key_gia_tri_lon_nhat(d):
    max_key = None
    max_value = None
    for k in d:
        if max_value is None or d[k] > max_value:
            max_value = d[k]
            max_key = k
    return max_key

n = int(input("Nhập số cặp key-value: "))

d = {}
for i in range(n):
    key = int(input("Nhập key: "))
    value = int(input("Nhập value: "))
    d[key] = value

ket_qua = tim_key_gia_tri_lon_nhat(d)

print("Dictionary:", d)
print("Key có giá trị lớn nhất là:", ket_qua)

'''
Bài 17: Viết chương trình tìm key có giá trị lớn nhất trong một dictionary chứa các
cặp key-value là số.
'''

n = int(input("Số cặp key-value: "))
d = {}
i = 0
while i < n:
    key = input("Key: ")
    val = int(input("Value: "))
    d[key] = val
    i += 1

best_key = None
best_val = None

for k in d:
    v = d[k]
    if best_val is None or v > best_val:
        best_val = v
        best_key = k

if best_key is None:
    print("Dictionary rỗng.")
else:
    print("Key có value lớn nhất:", best_key)
    print("Value:", best_val)

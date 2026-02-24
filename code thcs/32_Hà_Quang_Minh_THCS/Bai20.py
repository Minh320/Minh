def loc_dictionary(d):
    ket_qua = {}
    for k in d:
        if d[k] > 50:
            ket_qua[k] = d[k]
    return ket_qua

ds = {"A": 63,
      "B": 23,
      "C": 60,
      "D": 55,
      "E": 95}
ket_qua = loc_dictionary(ds)

print("Dictionary ban đầu:", ds)
print("Các cặp key-value có value > 50:", ket_qua)

'''
Bài 20: Viết chương trình lọc ra các cặp key-value từ dictionary thỏa mãn một điều
kiện cho trước (ví dụ: giá trị lớn hơn 50).
'''

n = int(input("Số cặp key-value: "))
d = {}
i = 0
while i < n:
    key = input("Key: ")
    val = int(input("Value: "))
    d[key] = val
    i += 1

threshold = int(input("Giữ các cặp có value > : "))

res = {}
for k in d:
    if d[k] > threshold:
        res[k] = d[k]

print("Các cặp thỏa điều kiện:")
for k in res:
    print(k, ":", res[k])
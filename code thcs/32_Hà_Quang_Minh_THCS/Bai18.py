def dao_nguoc_dictionary(d):
    d_nguoc = {}
    for k in d:
        v = d[k]
        d_nguoc[v] = k
    return d_nguoc
ds = {1 : 10,
      2 : 20,
      3 : 30}
ket_qua = dao_nguoc_dictionary(ds)
print("Dictionary ban đầu:", ds)
print("Dictionary sau khi đảo:", ket_qua)

'''
Bài 18: Viết chương trình đảo ngược dictionary (key thành value và ngược lại), giả
sử các value là duy nhất.
'''


n = int(input("Số cặp key-value: "))
d = {}
i = 0
while i < n:
    key = input("Key: ")
    val = input("Value (duy nhất): ")
    d[key] = val
    i += 1

inv = {}
for k in d:
    inv[d[k]] = k

print("Dictionary đảo:")
for k in inv:
    print(k, ":", inv[k])
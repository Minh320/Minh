a = [1, 4, 2, 3, 1, 4, 2]
ket_qua = []
for x in a:
    co = False
    for y in ket_qua:
        if x == y:
            co = True
            break
    if not co:
        ket_qua.append(x)
print(f"Danh sách ban đầu: {a}")
print(f"Danh sách sau khi loại trùng: {ket_qua}")


'''
Bài 5: Viết chương trình loại bỏ tất cả các phần tử trùng lặp trong một danh sách và
giữ nguyên thứ tự xuất hiện.
'''
n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

seen = {}
res = []

i = 0
while i < len(a):
    x = a[i]
    if x not in seen:
        seen[x] = 1
        res.append(x)
    i += 1

print("Danh sách sau khi loại trùng:", res)
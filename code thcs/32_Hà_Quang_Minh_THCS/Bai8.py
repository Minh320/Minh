a = [1, 2, 3, 4, 5]
k = int(input("Nhập k: "))
n = len(a)
k = k % n
i = 0
while i < k:
    cuoi = a[n - 1]    
    j = n - 1
    while j > 0:
        a[j] = a[j - 1]
        j = j - 1
    a[0] = cuoi         
    i = i + 1
print(f"Danh sách sau khi dịch: {a}")

'''
Bài 8: Viết chương trình dịch chuyển các phần tử của list sang phải k vị trí (k do
người dùng nhập).
'''

n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

k = int(input("Nhập k: "))

if n == 0:
    print("List rỗng.")
else:
    k = k % n
    res = [0] * n

    i = 0
    while i < n:
        new_pos = i + k
        if new_pos >= n:
            new_pos -= n
        res[new_pos] = a[i]
        i += 1

    print("Kết quả:", res)
def tong_duong_cheo_phu(a):
    n = len(a)
    tong = 0
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                tong = tong + a[i][j]
    return tong
ma_tran = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tong = tong_duong_cheo_phu(ma_tran)
print(f"Tổng đường chéo phụ: {tong}")

'''
Bài 9: Viết chương trình tính tổng các phần tử trên đường chéo phụ của ma trận
vuông.
'''

n = int(input("Nhập n (ma trận n x n): "))
mat = []
i = 0
while i < n:
    row = []
    j = 0
    while j < n:
        row.append(int(input(f"mat[{i}][{j}] = ")))
        j += 1
    mat.append(row)
    i += 1

s = 0
i = 0
while i < n:
    s += mat[i][n - 1 - i]
    i += 1

print("Tổng đường chéo phụ:", s)
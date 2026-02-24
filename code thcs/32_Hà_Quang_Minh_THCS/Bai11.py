def kiem_tra_doi_xung(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False
    return True
ma_tran = [[1,2,3], [2,4,5], [3,5,6]]
if kiem_tra_doi_xung(ma_tran):
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận KHÔNG phải là ma trận đối xứng")

'''
Bài 11: Viết chương trình kiểm tra xem một ma trận có phải là ma trận đối xứng hay
không.
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

ok = True
i = 0
while i < n:
    j = i + 1
    while j < n:
        if mat[i][j] != mat[j][i]:
            ok = False
            break
        j += 1
    if not ok:
        break
    i += 1

print("Đối xứng." if ok else "Không đối xứng.")
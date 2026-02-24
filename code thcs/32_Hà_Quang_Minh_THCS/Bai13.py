def la_ma_tran_don_vi(a):
    n = len(a)
    # Kiểm tra ma trận vuông
    for i in range(n):
        if len(a[i]) != n:
            return False
    # Kiểm tra ma trận đơn vị
    for i in range(n):
        for j in range(n):
            if i == j:
                if a[i][j] != 1:
                    return False
            else:
                if a[i][j] != 0:
                    return False
    return True
ma_tran = [[1,0,0], [0,1,0], [0,0,1]]
if la_ma_tran_don_vi(ma_tran):
    print("Ma trận là ma trận đơn vị")
else:
    print("Ma trận KHÔNG phải là ma trận đơn vị")

'''
Bài 13: Viết chương trình kiểm tra xem một ma trận vuông có phải ma trận đơn vị
không (phải kiểm tra ma trận nhập vào có phải ma trận vuông không)
'''


r = int(input("Nhập số hàng: "))
c = int(input("Nhập số cột: "))

mat = []
i = 0
while i < r:
    row = []
    j = 0
    while j < c:
        row.append(int(input(f"mat[{i}][{j}] = ")))
        j += 1
    mat.append(row)
    i += 1

if r != c:
    print("Không phải ma trận đơn vị (không phải ma trận vuông).")
else:
    n = r
    ok = True
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i == j:
                if mat[i][j] != 1:
                    ok = False
                    break
            else:
                if mat[i][j] != 0:
                    ok = False
                    break
            j += 1
        if not ok:
            break
        i += 1
    print("Là ma trận đơn vị." if ok else "Không phải ma trận đơn vị.")
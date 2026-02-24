def nhan_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    C = []
    for i in range(m): # Tạo ma trận kết quả C toàn số 0
        hang = []
        for j in range(p):
            hang.append(0)
        C.append(hang)
    for i in range(m): # Nhân ma trận
        for j in range(p):
            tong = 0
            for k in range(n):
                tong = tong + A[i][k] * B[k][j]
            C[i][j] = tong

    return C
A = [[1,2,3], [3,4,1], [2,5,3]]
B = [[2,4,3], [6,4,3], [2,4,5]]
C = nhan_ma_tran(A, B)
print(f"Ma trận kết quả C: {C}")

'''
Bài 12: Viết chương trình nhân hai ma trận với nhau (nếu phép nhân khả thi).
'''


r1 = int(input("A - số hàng: "))
c1 = int(input("A - số cột: "))
A = []
i = 0
while i < r1:
    row = []
    j = 0
    while j < c1:
        row.append(int(input(f"A[{i}][{j}] = ")))
        j += 1
    A.append(row)
    i += 1

r2 = int(input("B - số hàng: "))
c2 = int(input("B - số cột: "))
B = []
i = 0
while i < r2:
    row = []
    j = 0
    while j < c2:
        row.append(int(input(f"B[{i}][{j}] = ")))
        j += 1
    B.append(row)
    i += 1

if c1 != r2:
    print("Không nhân được (số cột A phải bằng số hàng B).")
else:
    C = []
    i = 0
    while i < r1:
        row = []
        j = 0
        while j < c2:
            val = 0
            k = 0
            while k < c1:
                val += A[i][k] * B[k][j]
                k += 1
            row.append(val)
            j += 1
        C.append(row)
        i += 1

    print("Ma trận C:")
    i = 0
    while i < r1:
        print(C[i])
        i += 1

def xu_ly_hai_set(A, B):
    A_khong_B = set()
    B_khong_A = set()
    giao = set()
    hop = set()
    # A nhưng không thuộc B
    for x in A:
        if x not in B:
            A_khong_B.add(x)
    # B nhưng không thuộc A
    for x in B:
        if x not in A:
            B_khong_A.add(x)
    # Giao của A và B
    for x in A:
        if x in B:
            giao.add(x)
    # Hợp của A và B
    for x in A:
        hop.add(x)
    for x in B:
        hop.add(x)
    return A_khong_B, B_khong_A, giao, hop
A = (1,2,3,4,5,6,7,8)
B = (1,2,3,4,6,7,9,10)
A_khong_B, B_khong_A, giao, hop = xu_ly_hai_set(A, B)
print("A nhưng không thuộc B:", A_khong_B)
print("B nhưng không thuộc A:", B_khong_A)
print("Giao của A và B:", giao)
print("Hợp của A và B:", hop)


'''
Bài 14: Cho hai set A và B, viết chương trình tìm ra các phần tử thuộc A nhưng không
thuộc B, các phần tử thuộc B nhưng không thuộc A, và các phần tử có trong cả hai
set (giao, hiệu, hợp của hai set).
'''


na = int(input("Số phần tử A: "))
A = []
i = 0
while i < na:
    x = int(input(f"A[{i}] = "))
    # đảm bảo không trùng trong A
    exist = False
    j = 0
    while j < len(A):
        if A[j] == x:
            exist = True
            break
        j += 1
    if not exist:
        A.append(x)
    i += 1

nb = int(input("Số phần tử B: "))
B = []
i = 0
while i < nb:
    x = int(input(f"B[{i}] = "))
    exist = False
    j = 0
    while j < len(B):
        if B[j] == x:
            exist = True
            break
        j += 1
    if not exist:
        B.append(x)
    i += 1

A_minus_B = []
i = 0
while i < len(A):
    x = A[i]
    inB = False
    j = 0
    while j < len(B):
        if B[j] == x:
            inB = True
            break
        j += 1
    if not inB:
        A_minus_B.append(x)
    i += 1

B_minus_A = []
i = 0
while i < len(B):
    x = B[i]
    inA = False
    j = 0
    while j < len(A):
        if A[j] == x:
            inA = True
            break
        j += 1
    if not inA:
        B_minus_A.append(x)
    i += 1

inter = []
i = 0
while i < len(A):
    x = A[i]
    inB = False
    j = 0
    while j < len(B):
        if B[j] == x:
            inB = True
            break
        j += 1
    if inB:
        inter.append(x)
    i += 1

uni = []
i = 0
while i < len(A):
    uni.append(A[i])
    i += 1
i = 0
while i < len(B):
    x = B[i]
    exist = False
    j = 0
    while j < len(uni):
        if uni[j] == x:
            exist = True
            break
        j += 1
    if not exist:
        uni.append(x)
    i += 1

print("A \\ B:", A_minus_B)
print("B \\ A:", B_minus_A)
print("A ∩ B:", inter)
print("A ∪ B:", uni)
x = int(input("Nhập số: "))
flag = False  
for i in range(0, x + 1):
    if i * i == x:
        flag = True
        break
if flag:
    print(f"{x} là số chính phương")
else:
    print(f"{x} không phải là số chính phương")
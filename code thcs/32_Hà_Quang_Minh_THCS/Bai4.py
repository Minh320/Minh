a = [1, 7, 14, 9, 32, 18]
max1 = a[0]
max2 = None
for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x != max1 and x > max2:
        max2 = x
print(f"Giá trị lớn thứ hai là: {max2}")

"""
Viết chương trình tìm giá trị lớn thứ hai trong một danh sách các số nguyên.
"""

n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

if n < 2:
    print("Cần ít nhất 2 phần tử.")
else:
    largest = a[0]
    second = None

    i = 1
    while i < n:
        x = a[i]
        if x > largest:
            second = largest
            largest = x
        else:
            if x != largest:
                if second is None or x > second:
                    second = x
        i += 1

    if second is None:
        print("Không có giá trị lớn thứ hai (các phần tử có thể bằng nhau hết).")
    else:
        print("Giá trị lớn thứ hai:", second)
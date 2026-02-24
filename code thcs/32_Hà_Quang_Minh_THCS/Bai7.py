a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 8 #tổng 
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == k:
            print(f"Cặp số: {a[i], a[j]}")


'''
Bài 7: Viết chương trình tìm ra tất cả các cặp số trong danh sách có tổng bằng một
giá trị cho trước.
'''

n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

target = int(input("Nhập tổng cần tìm: "))

found = False
i = 0
while i < n:
    j = i + 1
    while j < n:
        if a[i] + a[j] == target:
            print(f"({a[i]}, {a[j]})")
            found = True
        j += 1
    i += 1

if not found:
    print("(Không có cặp nào)")
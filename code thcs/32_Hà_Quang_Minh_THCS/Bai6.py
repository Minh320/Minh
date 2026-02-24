a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tong_chan = 0
tong_le = 0
for x in a:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x
print(f"Tổng số chẵn: {tong_chan}")
print(f"Tổng số lẻ: {tong_le}")

'''
Bài 6: Viết chương trình tính tổng các số chẵn và tổng các số lẻ trong một danh sách.
'''

n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

sum_even = 0
sum_odd = 0

i = 0
while i < len(a):
    if a[i] % 2 == 0:
        sum_even += a[i]
    else:
        sum_odd += a[i]
    i += 1

print("Tổng chẵn:", sum_even)
print("Tổng lẻ  :", sum_odd)
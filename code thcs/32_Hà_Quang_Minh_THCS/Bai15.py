def tach_chan_le_va_tinh_tong(t):
    chan = ()
    le = ()
    tong_chan = 0
    tong_le = 0
    for x in t:
        if x % 2 == 0:
            chan = chan + (x,)
            tong_chan = tong_chan + x
        else:
            le = le + (x,)
            tong_le = tong_le + x

    return chan, le, tong_chan, tong_le

a = [1,2,3,4,5,6]

chan, le, tong_chan, tong_le = tach_chan_le_va_tinh_tong(a)

print("Tuple ban đầu:", a)
print("Tuple chẵn:", chan)
print("Tổng các số chẵn:", tong_chan)
print("Tuple lẻ:", le)
print("Tổng các số lẻ:", tong_le)


'''
Bài 15: Viết chương trình nhận vào một tuple chứa các số nguyên, sau đó tạo ra hai
tuple mới: một tuple chứa các số chẵn và một tuple chứa các số lẻ từ tuple ban đầu,
đồng thời tính tổng các phần tử trong mỗi tuple mới.
'''

n = int(input("Số phần tử tuple: "))
temp = []
i = 0
while i < n:
    temp.append(int(input(f"t[{i}] = ")))
    i += 1

t = tuple(temp)

evens = []
odds = []
sum_e = 0
sum_o = 0

i = 0
while i < len(t):
    x = t[i]
    if x % 2 == 0:
        evens.append(x)
        sum_e += x
    else:
        odds.append(x)
        sum_o += x
    i += 1

print("Tuple chẵn:", tuple(evens))
print("Tuple lẻ  :", tuple(odds))
print("Tổng chẵn:", sum_e)
print("Tổng lẻ  :", sum_o)
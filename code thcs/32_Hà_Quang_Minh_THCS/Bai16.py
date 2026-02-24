def dem_tan_suat_ky_tu(s):
    tan_suat = {}
    for i in s:
        if i in tan_suat:
            tan_suat[i] = tan_suat[i] + 1
        else:
            tan_suat[i] = 1
    return tan_suat

ds = input("Nhập chuỗi: ")
ket_qua = dem_tan_suat_ky_tu(ds)
print("Tần suất xuất hiện của các ký tự:", ket_qua)

'''
Bài 16: Viết chương trình đếm tần suất xuất hiện của mỗi ký tự trong một chuỗi và
lưu vào dictionary.
'''


s = input("Nhập chuỗi: ")

freq = {}
i = 0
while i < len(s):
    ch = s[i]
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
    i += 1

print("Tần suất ký tự:")
for k in freq:
    print(repr(k), ":", freq[k])
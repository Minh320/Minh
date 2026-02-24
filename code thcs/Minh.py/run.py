'''
# cách 1: mở đóng file thủ công
f = open("text.txt", 'r') # encoding = 'utc-8' cho phép chương trình đọc ký hiệu đặc biệt ( có dấu)
f.close()    # đóng lại file sau khi đã tương tác


# cách 2: mở - đóng file tự động
with open("text.txt",'w') as f:
    # đoc file,...
    pass
'''
'''
f = open("text.txt", 'w')
f.write("Day la noi dung dau tien")
f.close()
'''


import csv

ds = [["ten", "tuoi", "thanh phố"]
      ["nva", 18, "HN"]
      ["nvb", 19, "HP"]
      ["nvc", 20, "HCM"]]
# tạo fole moi csv
with open("test.csv", 'w') as f:
    writer  = csv.writer(f)
    writer.writerows(ds)
    # Hoac
    #for row in ds:
    #    weiter.writerow(row)
    print("da tao file csv thanh cong")

with open("test.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
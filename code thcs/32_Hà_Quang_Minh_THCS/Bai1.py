x = input("Nhập chuỗi: ")
chu_cai = 0
chu_so = 0
dac_biet = 0
for i in x:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        chu_cai += 1
    elif '0' <= i <= '9':
        chu_so += 1
    else:
        dac_biet += 1
print(f"Số chữ cái: {chu_cai}")
print(f"Số chữ số: {chu_so}")
print(f"Số ký tự đặc biệt: {dac_biet}")

"""
Viết chương trình nhập vào một chuỗi và đếm số lượng ký tự chữ cái, chữ số
và ký tự đặc biệt trong chuỗi đó
"""

def count_characters(input_string):
    letters = sum(c.isalpha() for c in input_string)
    digits = sum(c.isdigit() for c in input_string)
    special_characters = sum(not c.isalnum() for c in input_string)
    
    return letters, digits, special_characters

text = input("Nhập vào một chuỗi: ")
letters, digits, special_characters = count_characters(text)
print(f"Số lượng chữ cái: {letters}")
print(f"Số lượng chữ số: {digits}")
print(f"Số lượng ký tự đặc biệt: {special_characters}")
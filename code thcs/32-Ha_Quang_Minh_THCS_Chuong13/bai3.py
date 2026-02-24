list_int = [2, 4, 5, 6]

with open(r"C:\Users\Administrator\Desktop\code thcs\32-Ha_Quang_Minh_THCS_Chuong13\so_nguyen.txt", "w") as file:
    for i in list_int:
        file.write(f"{i} \n")


with open(r"C:\Users\Administrator\Desktop\code thcs\32-Ha_Quang_Minh_THCS_Chuong13\so_nguyen.txt", "r", encoding='utf-8') as file:
    content = file.read()

print(content)
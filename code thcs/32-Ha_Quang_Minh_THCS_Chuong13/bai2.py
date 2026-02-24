with open(r"C:\Users\Administrator\Desktop\code thcs\32-Ha_Quang_Minh_THCS_Chuong13\vanban.txt", "r", encoding='utf-8') as file:
    content = file.read()

print(content)

dict_content = {}

list_word = content.split()

for i in list_word:
    if i in dict_content:
        dict_content[i] += 1
    else:
        dict_content[i] = 1

print(dict_content)
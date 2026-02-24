file = open("test_bai1.txt", "r", encoding='utf-8')
content = file.read()
print(content)

list_word = content.split()
print("tổng số từ trong tập tin: ", len(list_word))
file.close()
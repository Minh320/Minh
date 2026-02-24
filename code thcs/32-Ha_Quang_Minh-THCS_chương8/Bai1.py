# Viết chương trình nhập vào một số kiểm tra xem số đó có phải số chính phương hay không?
# số chính phương là số có căn bậc hai là một số nguyên

n = int(input("Nhập một số nguyên: "))

for i in range(1, n + 1):
    if i * i == n:
        print(f"{n} là số chính phương của {i}.")
        break
else:
    print(f"{n} không phải là số chính phương.")
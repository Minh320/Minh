# Viết chương trình nhập vào n, tìm tất cả các số nguyên tố nhỏ hơn n
# số nguyên tố là số chia heet cho 1 và chính nó

n = int(input("Nhập một số nguyên dương n: "))

print(f"Các số nguyên tố nhỏ hơn {n} là: ", end="")

for num in range(2, n):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
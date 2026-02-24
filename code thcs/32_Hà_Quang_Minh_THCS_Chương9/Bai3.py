""" Viết hàm kiem_tra_so_armstrong(n) nhận vào một số nguyên dương n. Hàm này sẽ trả về 
 True nếu n là số Armstrong (tổng các lũy thừa bậc 3 của các chữ số của nó bằng chính nó, ví dụ: 153) và False nếu không. """


def kiem_tra_so_armstrong(n):
    n_goc = n
    sum = 0
    while n > 0:
        number_i = n % 10
        sum += number_i **3
        n = n // 10
    return sum == n_goc

n = int(input("nhập số nguyên dương n: "))
check_n = kiem_tra_so_armstrong(n)
print(check_n)
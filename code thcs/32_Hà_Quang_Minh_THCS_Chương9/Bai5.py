def kiem_tra_so_doi_xung(n):
    s = str(n)
    dao = ""
    for i in s:
        dao += i
    return s == dao
print(kiem_tra_so_doi_xung(121))  
print(kiem_tra_so_doi_xung(353))  
print(kiem_tra_so_doi_xung(123))  



"""
Viết hàm kiem_tra_so_doi_xung(n) nhận vào một số nguyên dương n. Hàm sẽ
trả về True nếu n là số đối xứng (khi đọc xuôi hay ngược đều giống nhau, ví dụ: 121,
353) và False nếu không.
"""

def kiem_tra_so_doi_xung(n):
    n_goc = n
    n_doixung = 0
    while n > 0:
        number_i = n % 10
        n_doixung = n_doixung*10 + number_i
        n = n // 10
    
    return n_goc == n_doixung

n = int(input("nhập số nguyên dương n: "))
check_n = kiem_tra_so_doi_xung(n)
print(check_n)
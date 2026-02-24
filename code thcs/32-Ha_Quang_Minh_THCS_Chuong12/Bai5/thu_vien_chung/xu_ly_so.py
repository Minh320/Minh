def kiem_tra_so_nguyen_to(so):
    # so nguyen to la so lon hon 1 va chia hết cho 1 và chính nó
    if so <= 1:
        return "không phải là số nguyên tố"
    
    if so == 2:
        return "la so nguyên tố"
    
    for i in range(2, int(so**0.5)+1):
        if so % i == 0:
            return "không phải là số nguyên tố"
    
    return "là số nguyên tố"
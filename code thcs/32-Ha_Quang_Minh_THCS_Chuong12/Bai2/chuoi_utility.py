def dao_nguoc_chuoi(chuoi):
    chuoi_nguoc = chuoi[::-1]
    return chuoi_nguoc


def dem_so_tu(chuoi):
    list_word = chuoi.split()
    n_word = len(list_word)
    return n_word
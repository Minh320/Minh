tinh_tich = lambda x,y,z : x*y*z
print(tinh_tich(1,2,3))


"""
Viết một hàm lambda để tính tích của ba số bất kỳ.
"""

tich_a_b_c = lambda a, b, c: a*b*c

a, b, c = map(float, input("nhập 3 số a b c: ").split())

print(tich_a_b_c(a,b,c))
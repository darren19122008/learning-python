print("-"*40)
print("RUMUS KERUCUT")
print("-"*40)

PHI = 3,14
r = int(input('Masukkan jari-jari:  '))
s = float(input('Masukkan sisi kerucut:  '))
t = float(input('Masukkan tinggi kerucut:  '))

ls = PHI * r * s 
lp = print("-"*40)
print("RUMUS KERUCUT")
print("-"*40)

PHI = 3,14
r = int(input('Masukkan jari-jari:  '))
s = float(input('Masukkan sisi kerucut:  '))
t = float(input('Masukkan tinggi kerucut:  '))

ls = PHI * r * s 
lp = (PHI * r * s) + (PHI * r ** 2)
v = 1/3 * PHI * r ** 2 * t

print('Luas selimut \t:  ',ls, ' cm')
print('Luas permukaan \t:  ',lp)
print('Volume \t:  ',round(v,2))
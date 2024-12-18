print("="*40)
print("RUMUS KERUCUT")
print("="*40)

PHI = 3.14
r = int(input('Masukkan jari-jari: '))
s = float(input('Masukkan sisi kerucut: '))
t = float(input('Masukkan tinggi kerucut: '))

Ls = PHI * r * s
Lp = (PHI * r * s) + (PHI * r ** 2)
v = 1/3 * PHI   * r ** 2 * t

print('luas selimut \t: ',Ls, ' cm')
print('Luas permukaan \t: ', Lp)
print('volume \t: ', round(v,2))
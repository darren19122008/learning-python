bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
bulan.append('Muharram')

for a,b in enumerate(bulan):
    print(f'bulan ke-{a+1} yaitu {b}')

#soal 2
print(bulan[2])
print(bulan[9])

#soal 3
bulan[7] = 'August'
print(bulan[7])

#soal 4
bulan[0] = 'january'
print(bulan[0])
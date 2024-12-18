nama1 = 'Didah'
nama2 = 'Toni'
nama3 = 'Yanti'

nama = ['Didah','Toni','Yanti']
nama[0] = 'Didah Ah Ah'

print(nama[0])
print(nama[1])
print(nama[2])

nama.append('Deni')

for i,x in enumerate(nama):
    print(i+1,'. ',x)
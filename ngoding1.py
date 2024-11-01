x = 1
y = 2
z = 3

x = int(input('Masukkan nilai x\t:  '))
y = int(input('Masukkan nilai y\t:  '))
z = int(input('Masukkan nilai z\t:  '))

x,y,z = y,z,x 

print(f"Setelah Ditukar:({x},{y},{z})")
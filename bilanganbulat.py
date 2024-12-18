print("="*20)
print("bilangan bulat")
print("="*20)

a = 1 
b = 2
c = 3

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b

a = int(input('Masukkan nilai a\t:  '))
b = int(input('Masukkan nilai b\t:  '))
c = int(input('Masukkan nilai c\t:  '))

print(f"bilangan yang terurut:{a},{b},{c}")
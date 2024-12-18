detik_ke_menit = 60
detik_ke_jam = 60 * 60
detik_ke_hari = 60 * 60 * 24

detik = int(input("Masukkan detik\t:  "))

hari = detik / detik_ke_hari
detik = detik % detik_ke_hari
jam = detik / detik_ke_jam
detik = detik % detik_ke_jam
menit = detik / detik_ke_menit
detik = detik / detik_ke_menit

print("Hasilnya adalah\t:" ,hari, "hari" ,jam, "jam" ,menit, "menit" ,detik, "detik" )
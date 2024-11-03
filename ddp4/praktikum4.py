#program menentukan bilangan ganjil dan genap
print ('## 1. Progam bilangan ganjil dan genap')
print('=======================================')

#bilangan
bilangan = int(input('Masukan bilangan: '))

if bilangan % 2 == 0:
    print(bilangan, 'Merupakan bilangan genap')
    
else:
    print(bilangan, 'Merupakan bilangan ganjil')
    
#program menentukan nilai ujian
print ('## 2. Progam menentukan nilai ujian')
print('=======================================')

#Input nilai
nilai_ujian = int(input('Masukkan nilai: '))

#Proses
if nilai_ujian >= 75:
    print('anda lulus')
else:
    print('anda tidak lulus')
    
#program menentukan usia dan status
print ('## 3. Progam menentukan usia dan status')
print('=======================================')

#input usia
usia = int(input('Masukan usia anda: '))

#Proses dan output
if usia >= 18: 
    print('Anda sudah dewasa')
elif usia >=13 and usia <=17:
    print('Anda remaja')
else:
    print('Anda anak-anak')
    
#program cek keanggotaan
print ('## 4. Progam cek keanggotaan')
print('=======================================')
print()

#input status
status_anggota = input('''Daftar keanggotaan dibawah ini
1. gold
2. silver
3. bronze
Masukkan pilihan anda: ''')
#Proses dan Output
if status_anggota=='gold' or status_anggota=='silver':
    print('Selamat Anda Mendapatkan Diskon')
elif status_anggota == 'bronze':
    print('Maaf Anda tidak mendapatkan diskon')
else:
    print('Masukan kata dengan benar')
    
#program pembelian diskon
print ('## 5. Progam pembelian diskon')
print('=======================================')
print()

#input pembelian
hrg_minyak = 25000
hrg_indomie= 5000
hrg_beras= 75000
hrg_gula= 25000
hrg_kopi= 20000
hrg_teh= 10000

minyak= int(input("Masukkan Jumlah Minyak:" ))
byr_minyak= minyak * hrg_minyak
indomie= int(input("Masukkan Jumlah Indomie: "))
byr_indomie= indomie * hrg_indomie
beras= int(input("Masukkan Jumlah Beras: "))
byr_beras= beras*hrg_beras
gula= int(input("Masukkan Jumlah Gula: "))
byr_gula= gula*hrg_gula
kopi= int(input("Masukkan Jumlah Kopi: "))
byr_kopi= kopi*hrg_kopi
teh= int(input("Masukkan Jumlah Teh: "))
byr_teh= teh*hrg_teh

jml_beli = minyak + indomie + beras + gula + kopi + teh
total= byr_minyak + byr_indomie + byr_beras + byr_gula + byr_kopi + byr_teh

#output
if jml_beli>=100:
    diskon = total * 10/100
    harga_akhir= total - diskon
    print("Harga total pembelian anda adalah" +str(harga_akhir))
else:
    harga_akhir = total
    print("Harga total pembelian anda adalah" +str(harga_akhir))
    
print("Terimakasih Sudah Belanja Disini:)")
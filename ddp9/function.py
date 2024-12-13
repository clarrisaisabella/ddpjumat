# deklarasi fungsi
def hai():
        print('Hello selamat datang di NF')
        print()
        
#panggil fungsi
hai()
hai()
hai()

#contoh2
def cetak(kata):
    print(kata)
cetak('Hello World')
cetak('Selamat Datang di NF')

def biodata(nama, alamat, umur):
    cetak('nama saya adalah' +nama)
    cetak('alamat saya di' +alamat)
    cetak('umur saya adalah' +str(umur))
biodata(' Clarrisa', ' Cibinong', ' 18')

def perkalian(angka1, angka2):
    cetak(angka1*angka2)
    
perkalian(3, 4) #12
perkalian (10, 10)

        
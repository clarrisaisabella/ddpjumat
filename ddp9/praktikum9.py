#No1  Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. 
# Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0




def celcius_ke_farenheit(celcius):
    hasil_konversi = (celcius * 9/5) +32
    return hasil_konversi

print(celcius_ke_farenheit(0))
print(celcius_ke_farenheit(100))



#No2  Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. 
# Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))  # Output: True
#print(is_genap(7))  # Output: False

def is_genap(angka):
    return angka %2 == 0

print(is_genap(4))
print(is_genap(7))
    


#No3    Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai(60) #gagal

def keterangan(nilai):
    print()
    if nilai >=80:
        return('Lulus')
    else :
        return('gagal')
print(keterangan(80))
print(keterangan(60))



#No4    Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,5,7,9,11,13,15,17,19
def bilangan_ganjil(angka):
    for i in range(1, angka+1, 2):
        print (i, end=" ")
bilangan_ganjil(20)

kendaraan=['beat karbu', 'motor', 200, 'pink', 3]
print(kendaraan)

kendaraan.append('10jt')
print(kendaraan)

kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2,'honda')
print(kendaraan)


angka_pilihan=int(input("""Masukkan Pilihan:
                        1. Menghitung Luas Persegi
                        2. Menghitung Luas Lingkaran
                        3. Menghitung Luas Segitiga
                        """))

match angka_pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        sisi= int(input("Masukkan Sisi: "))
        luas_persegi= sisi **2
        print(f"Luas Persegi dengan sisi{sisi} cm, adalah{luas_persegi} cm^2 ")
    case 2:
        print("Menghitung Luas Lingkaran")
        phi=22/7
        r= int(input("Masukkan Jari-jari: "))
        luas_lingkaran= phi*r*r
        print(f"Luas lingkaran dengan jari-jari{r} cm, adalah {luas_lingkaran} cm^2 ")
    case 3:
        print("menghitung luas segitiga")
        1/2
        a=int(input("Masukkan alas: "))
        t=int(input("Masukkan tinggi: "))
        luas_segitiga= 1/2*a*t
        print(f"Luas segitiga dengan alas{a} cm dan tinggi {t} cm, adalah {luas_segitiga} cm^2 ")
    case _:
        print("Input tidak valid")
berat_badan= int(input("Masukkan berat badan: "))
tinggi_badan= int(input("Masukkan tinggi badan: "))
bbideal = (tinggi_badan-100) - ((tinggi_badan-100)*0.15)
print("Berat badan ideal dengan tinggi badan", tinggi_badan, "adalah", bbideal, "kg")
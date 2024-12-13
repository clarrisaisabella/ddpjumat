nama=str(input("Masukkan Nama Pembeli: "))
no_hp=int(input("Masukkan No HP Pembeli: "))
menu=int(input("""Pesan Menu Apa?:
               1. Makanan
               2. Minuman"""))

match menu:
    case 1:
        print("Makanan")
        print("Masukan Pesanan: ")
        hrg_nasi_goreng=15000
        hrg_mie_goreng=12000
        hrg_ayam_geprek=18000
        
        nasi_goreng= int(input("jumlah nasi goreng:"))
        byr_nasi_goreng= hrg_nasi_goreng*nasi_goreng
        mie_goreng= int(input("jumlah mie goreng:"))
        byr_mie_goreng= hrg_mie_goreng*mie_goreng
        ayam_geprek= int(input("jumlah ayam geprek:"))
        byr_ayam_geprek= hrg_ayam_geprek*ayam_geprek
        
        jml_pesanan= nasi_goreng + mie_goreng + ayam_geprek
        print("pesanan anda adalah" +str(jml_pesanan))
        harga_byr= byr_nasi_goreng + byr_mie_goreng + byr_ayam_geprek
        print("Harga yang harus anda bayar adalah:" +str(harga_byr))
        
    case 2:
        print("Minuman ")
        print("Masukkan Pesanan:")
        hrg_aneka_jus=15000
        hrg_soft_drink=10000
        hrg_sweet_ice_tea=5000
        
        aneka_jus= int(input("jumlah aneka jus: "))
        byr_aneka_jus= hrg_aneka_jus*aneka_jus
        soft_drink= int(input("jumlah soft drink: "))
        byr_soft_drink=hrg_soft_drink*soft_drink
        sweet_ice_tea= int(input("jumlah sweet ice tea: "))
        byr_sweet_ice_tea=hrg_sweet_ice_tea*hrg_sweet_ice_tea
        
        
        jumlah_pesanan= aneka_jus + soft_drink + sweet_ice_tea
        print("pesanan anda adalah" +str(jumlah_pesanan))
        harga_bayar= byr_aneka_jus + byr_soft_drink + byr_sweet_ice_tea
        print("Harga yang harus anda bayar adalah:" +str(harga_bayar))
        
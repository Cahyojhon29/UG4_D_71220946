def cari_kata_terpanjang(kalimat):
    
    daftar_kata = kalimat.split()  
    kata_terpanjang = max(daftar_kata, key=len)
    return kata_terpanjang

kalimat = input("Masukkan sebuah kalimat: ")
kata_terpanjang = cari_kata_terpanjang(kalimat)

print("Kata terpanjang dalam kalimat tersebut adalah:", kata_terpanjang)

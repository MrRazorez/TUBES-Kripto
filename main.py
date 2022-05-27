import keystream
import cbc
import lsb

def cobaEnkripsi(plain) :
    try :
        kunci = keystream.keystream()

        temp = cbc.enkripsi(plain, kunci.lfsr, kunci.IV)
        masuk = input("Nama file input gambar (dengan ekstensi) : ")
        masuk = "tempat_gambar/"+masuk
        lsb.sisip(temp, masuk)

        f = open("tempat_gambar/kunci.txt", "w")
        f.write(kunci.lfsr+"\n"+kunci.IV)
        print("PESAN TELAH TERENKRIPSI!!")
    except :
        print("GAGAL ENKRIPSI")

def cobaDekripsi(chiper) :
    try :
        f = open("tempat_gambar/kunci.txt", "r")
        kunci = f.readlines()
        kunci[0] = kunci[0][:len(kunci[0])-1]

        gambar = "tempat_gambar/"+chiper
        tmp = lsb.ekstraksi(gambar)
        temp = cbc.dekripsi(tmp, kunci[0], kunci[1])

        print("PESAN : ")
        print(cbc.plainASCII(temp))
        
    except :
        print("TIDAK ADA KUNCI PEMBUKA")

if __name__ == "__main__" :
    print("PILIHAN MENU")
    print("============")

    print("1. Enkripsi")
    print("2. Dekripsi")

    pilih = input("=> ")
    pilih = int(pilih)

    if pilih == 1 :
        masuk = input("Ketik Pesan\n=> ")
        cobaEnkripsi(masuk)
    elif pilih == 2 :
        masuk = input("Ketik Nama File Gambar Chiper\n=> ")
        cobaDekripsi(masuk)

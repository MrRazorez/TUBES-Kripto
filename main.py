import cbc
import lsb

if __name__ == "__main__" :
    teks = "hello, world!!"
    print(teks)
    coba = cbc.enkripsi(teks, cbc.ambilKey.lfsr, cbc.ambilKey.IV)
    print(coba)
    hasil = cbc.dekripsi(coba, cbc.ambilKey.lfsr, cbc.ambilKey.IV)
    print(cbc.plainASCII(hasil))

    lsb.sisip(coba, "./7i5j2icd69c31.png")
    masuk = input("Gambar => ")
    coba2 = lsb.ekstraksi(masuk)
    hasil2 = cbc.dekripsi(coba2, cbc.ambilKey.lfsr, cbc.ambilKey.IV)
    print(cbc.plainASCII(hasil2))
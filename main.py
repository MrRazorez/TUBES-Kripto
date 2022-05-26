import gen_bin
import cbc

def ngeTEST(teks) :
    i = 1
    temp = ""

    while i < len(teks) :
        tmp = teks[i-1] + teks[i]
        tmp = gen_bin.hek_conv(tmp)
        temp += chr(tmp)
        i += 2

    return temp

if __name__ == "__main__" :
    teks = "hello"
    print(teks)
    coba = cbc.enkripsi(teks, cbc.ambilKey.lfsr, cbc.ambilKey.IV)
    hasil = cbc.dekripsi(coba, cbc.ambilKey.lfsr, cbc.ambilKey.IV)
    print(cbc.plainASCII(hasil))
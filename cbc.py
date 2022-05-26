import gen_bin
import keystream

ambilKey = keystream.keystream()

def __plainHex(teks) :
    temp = ""
    for i in teks :
        temp += gen_bin.hek_conv(ord(i))

    return temp

def plainASCII(teks) :
    i = 1
    temp = ""

    while i < len(teks) :
        tmp = teks[i-1] + teks[i]
        tmp = gen_bin.hek_conv(tmp)
        temp += chr(tmp)
        i += 2

    return temp

def __wrap_left(karakter) :
    tmp = gen_bin.bin_conv(gen_bin.hek_conv(karakter))
    if len(tmp) < 4 :
        tp = ""
        for i in range(4-len(tmp)) :
            tp += "0"

        tmp = tp+tmp

    tmp = tmp[1:]+tmp[0]

    return gen_bin.hek_conv(gen_bin.bin_conv(tmp))

def __wrap_right(karakter) :
    tmp = gen_bin.bin_conv(gen_bin.hek_conv(karakter))
    if len(tmp) < 4 :
        tp = ""
        for i in range(4-len(tmp)) :
            tp += "0"

        tmp = tp+tmp

    tmp = tmp[len(tmp)-1]+tmp[:len(tmp)-1]
    
    return gen_bin.hek_conv(gen_bin.bin_conv(tmp))

def enkripsi(plain, K, IV) :
    plain_hex = __plainHex(plain)
    print(plain_hex)
    temp = ""

    i = 0
    for j in plain_hex :
        tmp = gen_bin.hek_conv(gen_bin.hek_conv(j) ^ gen_bin.hek_conv(IV))
        tmp = __wrap_left(gen_bin.hek_conv(gen_bin.hek_conv(tmp) ^ gen_bin.hek_conv(K[i])))
        temp += tmp
        IV = tmp

        i += 1
        if i == len(K) :
            i %= len(K)
    print(temp)

    return temp

def dekripsi(chiper, K, IV) :
    print(chiper)
    temp = ""

    i = 0
    for j in chiper :
        tmp = gen_bin.hek_conv(gen_bin.hek_conv(__wrap_right(j)) ^ gen_bin.hek_conv(K[i]))
        tmp = gen_bin.hek_conv(gen_bin.hek_conv(tmp) ^ gen_bin.hek_conv(IV))
        temp += tmp
        IV = j

        i += 1
        if i == len(K) :
            i %= len(K)
    print(temp)

    return temp
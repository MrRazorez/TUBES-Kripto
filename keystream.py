import gen_bin
from random import randint

class keystream :
    def __init__(self) -> None :
        self.U = self.__key_gen()
        self.lfsr = self.__lfsr_sys(self.U)

    def __key_gen(self) :
        temp = randint(1, 255)
        temp += randint(1, 255)
        temp = gen_bin.bin_conv(temp)

        if len(temp) < 16 :
            tmp = ""
            for i in range(16-len(temp)) :
                tmp += "0"

            temp = tmp+temp

        return temp

    def __gen_lfsr(self, kunci) :
        sway = int(kunci[len(kunci)-1]) ^ int(kunci[0])
        kunci = str(sway)+kunci[:len(kunci)-1]

        return kunci

    def __pecah(self, kata) :
        temp = ""
        i = 0
        j = 4
        
        while j <= len(kata) :
            temp += gen_bin.hek_conv(gen_bin.bin_conv(kata[i:j]))
            i += 4
            j += 4

        return temp
            

    def __lfsr_sys(self, kunci) :
        temp = ""
        temp += kunci[len(kunci)-1]
        kunci = self.__gen_lfsr(kunci)
        pegang = kunci
        i = 0
        while kunci != pegang or i == 0 :
            temp += kunci[len(kunci)-1]
            kunci = self.__gen_lfsr(kunci)
            i += 1
        
        return self.__pecah(temp)
import gen_bin
from random import randint

class keystream :
    def __init__(self) -> None :
        self.key_lfsr = self.__key_gen()
        self.lfsr = self.__lfsr_sys(self.key_lfsr)

    def __key_gen(self) :
        temp = randint(1, 15)
        temp = gen_bin.bin_conv(temp)

        if len(temp) < 4 :
            tmp = ""
            for i in range(4-len(temp)) :
                tmp += "0"

            temp = tmp+temp

        return temp

    def __gen_lfsr(self, kunci) :
        sway = int(kunci[len(kunci)-1]) ^ int(kunci[0])
        kunci = str(sway)+kunci[:len(kunci)-1]

        return kunci

    def __lfsr_sys(self, kunci) :
        temp = ""
        pegang = kunci
        i = 0
        while kunci != pegang or i == 0 :
            temp += kunci[len(kunci)-1]
            kunci = self.__gen_lfsr(kunci)
            i += 1

        return temp
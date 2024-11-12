def TCKontrol(TC):
    result = True
    if len(TC) != 11 or TC[0] == "0" or not TC.isnumeric():
        result = False
    else:
        s1 = int(TC[0])
        s2 = int(TC[1])
        s3 = int(TC[2])
        s4 = int(TC[3])
        s5 = int(TC[4])
        s6 = int(TC[5])
        s7 = int(TC[6])
        s8 = int(TC[7])
        s9 = int(TC[8])
        s10 = int(TC[9])
        s11 = int(TC[10])

        toplamTekler = s1 + s3 + s5 + s7 + s9
        toplamCiftler = s2 + s4 + s6 + s8

        if (7 * toplamTekler - toplamCiftler) % 10 != s10:
            result = False

        toplam10 = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10

        if toplam10 % 10 != s11:
            result = False

    return result

TC = input("TC kimlik numarası giriniz: ")
result = TCKontrol(TC)
print(result)

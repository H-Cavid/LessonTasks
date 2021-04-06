#kvadratin sahesini ve perimetrini hesablayin
en = int(input("Kvadratin enini daxil edin:"))
uzunluq = int(input("kvadratin uzunlugunu daxil edin:"))


def sahe():
    s=en*uzunluq
    return s

def perimetr():
    p=en+uzunluq
    return p

print("kvadratin sahesi:",sahe())
print("kvadratin perimetri",perimetr())
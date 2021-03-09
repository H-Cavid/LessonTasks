#kvadratin sahesini ve perimetrini hesablayin
en = int(input("Kvadratin enini daxil edin:"))
uzunluq = int(input("kvadratin uzunlugunu daxil edin:"))

@classmethod
def sahe():
    s=en*uzunluq
    return s
@classmethod
def perimetr():
    p=en+uzunluq
    return p

print("kvadratin sahesi:",sahe)
print("kvadratin perimetri",perimetr)
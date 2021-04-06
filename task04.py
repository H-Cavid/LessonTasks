# # Ucbucagin sahesini hesablayan proqrami yazin.Funksiyadan istifade ederek
import math
a=int(input("Ucbucagin terefini daxil edin:"))
b=int(input("Ucbucagin 2-ci terefini daxil edin:"))
c=int(input("Ucbucagin 3-cu terefini daxil edin:"))

def sahe():
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S

print("Ucbucagin sahesi:" ,int(sahe()))
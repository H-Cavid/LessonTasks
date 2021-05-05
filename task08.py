import numpy as np 
import random 
def Hesab():
    try:
        setir = int(input("Setirlerin sayini daxil edin : ")) 
        sutun = int(input("Sutunlarin sayini daxil edin : ")) 
        araliq= int(input("Araligi daxil edin : "))
        A = np.random.randint(araliq, size=(setir,sutun)) 
        print(A)
    except:
        print("Daxil edilen parametler yanlisdir")

Hesab()
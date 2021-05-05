def Number():
    try:
        num = int(input("Eded daxil edin: "))
        if (num % 2) == 0:
            print("{0} cutdur".format(num))
        else:
            print("{0} tekdir".format(num))
    except:
        print("SEHVDI")

Number()
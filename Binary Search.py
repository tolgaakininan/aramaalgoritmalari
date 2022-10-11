def binarySearch(dizi,hedef):
    kucuk=0
    buyuk=len(dizi)
    while kucuk<=buyuk:
        orta=(buyuk+kucuk)//2
        if dizi[orta]==hedef:
            return orta
        elif dizi[orta]>hedef:
            buyuk=orta-1
        else:
            kucuk=orta+1
    return -1;
dizi=([13,22,33,44,55,66])
indis=binarySearch(dizi,33)
if indis==-1:
    print("Aradığınız element dizide yok")
else:
    print("Aradığınız element dizinin "+str(indis)+". indisinde")

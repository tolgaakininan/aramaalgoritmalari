def lineerSearch(dizi,hedef):
    count=0
    for i in dizi:
        
        if i==hedef:
            return count
        count=+1    
    return -1
dizi=([13.,22,9,8,14])
indis=lineerSearch(dizi,22)
if indis==-1:
    print("Aradığınız element dizide yok")
else:
    print("Aradığınız element "+str(indis)+". indiste")

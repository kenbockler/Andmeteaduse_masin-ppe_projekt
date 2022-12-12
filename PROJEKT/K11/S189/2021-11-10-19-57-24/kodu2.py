def transponeeriK(maatriks):
    järjend_kokku = []
    for i in range((len(maatriks[0])-1),-1,-1):
        järjend = []
        for j in range((len(maatriks)-1),-1,-1):
            arv = maatriks[j][i]
            järjend.append(arv)
        järjend_kokku.append(järjend)
    return(järjend_kokku)
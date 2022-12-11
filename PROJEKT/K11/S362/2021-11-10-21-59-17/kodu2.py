def transponeeriK(maatriks):
    maatriksT=[]
    if maatriks==[[]]:
        return maatriks
    else:
        a=len(maatriks[0])-1
        while a>-1:
            maatriksT_rida=[]
            for i in range((len(maatriks)-1),-1,-1):
                maatriksT_rida+=[maatriks[i][a]]
            maatriksT+=[maatriksT_rida]
            a=a-1
        return maatriksT
maatriks=[[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
maatriksT=transponeeriK(maatriks)
print(maatriks)
print(maatriksT)
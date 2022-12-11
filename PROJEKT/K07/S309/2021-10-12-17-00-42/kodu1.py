def poisse_ja_tüdrukuid(datalist):
    malecount = 0
    femalecount = 0
    for item in datalist:
        if(str(item[-1]) == "P"):
            malecount += 1
        elif(str(item[-1]) == "T"):
            femalecount += 1
    return (malecount, femalecount)
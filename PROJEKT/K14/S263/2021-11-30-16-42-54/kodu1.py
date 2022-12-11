def rek_abs(järjend):   
    if järjend == []:
        return []   
    else:
        uus_järjend = []
        for element in järjend:
            if isinstance(element,list)==False:
                uus_järjend.append(abs(element))    
            elif isinstance(element,list)==True:
                uus_järjend.append(rek_abs(element)) 
        return uus_järjend
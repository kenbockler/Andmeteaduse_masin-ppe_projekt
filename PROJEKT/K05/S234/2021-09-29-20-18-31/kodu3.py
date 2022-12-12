def moos(suur,vaike,kogus):
    if suur*5+vaike<kogus:
        return(-1)
    else:
        suuri=kogus//5
        väikeseid=kogus-suuri*5
        if suuri<=suur and väikeseid<=vaike:
            return(suuri+väikeseid)
        else:
            if väikeseid<=vaike:
                väikeseid=kogus-suur*5 
                return(suur+väikeseid)
            else:
                return(-1)
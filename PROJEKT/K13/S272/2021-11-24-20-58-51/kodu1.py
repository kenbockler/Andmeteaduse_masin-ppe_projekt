def auto_hind(price,years):
    if years == 0:
        return price
    return round(auto_hind(price*0.8,years-1),2)
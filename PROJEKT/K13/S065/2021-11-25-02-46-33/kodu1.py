def auto_hind(hind, aasta):
    if aasta == 0:
        return round(hind, 2)
    else:
        return auto_hind(hind*0.8, aasta-1)
print(auto_hind(8000.0, 5))
def auto_hind(hind, aasta):
    if aasta == 0:
        return hind
    return auto_hind(round((hind * 0.8),2), aasta-1)
print(auto_hind(10000.0, 5))
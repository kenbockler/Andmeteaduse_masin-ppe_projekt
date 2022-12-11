'''-- Kodutöö nr. 13 - 1. Kasutatud auto hind rekursiivselt --'''
def auto_hind(hind, aastad):
    if aastad == 0:
        return float(hind)
    else:
        return round(auto_hind(0.8*float(hind), aastad-1), 2)
print(auto_hind(8000.0, 5))
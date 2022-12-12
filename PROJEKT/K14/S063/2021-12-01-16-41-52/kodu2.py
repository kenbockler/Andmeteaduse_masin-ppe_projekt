'''-- Kodutöö nr. 14 - 2. Väljasta liin --'''
def väljasta_liin(eellane, järglane, sugupuu):
    if eellane == järglane:
        print(järglane)
        return True
    elif järglane not in sugupuu:
        return False
    else:
        (isa, ema) = (el for el in sugupuu[järglane])
        if väljasta_liin(eellane, isa, sugupuu) or väljasta_liin(eellane, ema, sugupuu):
            print(järglane)
            return True
        else:
            return False
sõnastik = {'Kalle': ('Teet', 'Maris'),
            'Maris': ('Konstantin', 'Mari'),
            'Rita': ('Teet', 'Maris'),
            'Siim': ('Teet', 'Maris'),
            'Mari': ('Karl', 'Leeni'),
            'Teet': ('Joosep', 'Adele'),
            'Adele': ('Johannes', 'Leida'),
            'Konstantin': ('Viktor', 'Jelena'),
            'Joosep': ('August', 'Emma'),
            'Viktor': ('Nikolai', 'Maria')}
print("Kas liin leidub?", väljasta_liin('Leida', 'Kalle', sõnastik))
print("Kas liin leidub?", väljasta_liin('Mari', 'Adele', sõnastik))

sugupuu={'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}
def v�ljasta_liin(eel, j�rg, sugupuu):
    if j�rg not in sugupuu:
        return False
    else:
        for j�rg in sugupuu.keys():
            if j�rg[0] == eel:
                print(eel)
                print(j�rg)
                return True
            elif j�rg[1] == eel:
                print(eel)
                print(j�rg)
                return True
            else:
                v�ljasta_liin(eel[0], j�rg, sugupuu)
                v�ljasta_liin(eel[1], j�rg, sugupuu)
print("Kas liin leidub?", v�ljasta_liin('Leida', 'Kalle', sugupuu))
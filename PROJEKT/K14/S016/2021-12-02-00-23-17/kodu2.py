s�nastik = {
  'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')}
def v�ljasta_liin(eellane, j�rglane, s�nastik):
    if eellane == j�rglane:
        print(eellane)
        return True
    if j�rglane in s�nastik.keys():
        for vanem in s�nastik[j�rglane]:
            if v�ljasta_liin(eellane, vanem, s�nastik) == True:
                print(j�rglane)
                return True
        return False
    return False
print("Kas liin leidub?", v�ljasta_liin('Leida', 'Kalle', s�nastik))
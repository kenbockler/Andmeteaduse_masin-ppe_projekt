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
            print(j�rglane)
            return True
        elif True:
            for laps in s�nastik:
                if eellane in s�nastik[laps]:
                    print(eellane)
                    eellane = laps
                    return v�ljasta_liin(eellane, j�rglane, s�nastik)
        else:
            return False
v�ljasta_liin('Leida', 'Kalle', s�nastik)
    
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
  'Viktor': ('Nikolai', 'Maria')
}
def v�ljasta_liin(eellane, j�rglane, s�nastik):
    vanemad = list(s�nastik.values())
    j�rglased = list(s�nastik.keys())
    v�imalik_eellane = []
    if eellane in v�imalik_eellane:
        return v�imalik_eellane
    else:
        for i in range(2):
            v�imalik_eellane.append(s�nastik[j�rglane][i])
            uus_eellane = v�imalik_eellane
            j�rglane = eellane
            eellane = uus_eellane
            v�ljasta_liin(eellane, j�rglane, s�nastik)
        print()
print(v�ljasta_liin('Leida', 'Kalle', s�nastik))
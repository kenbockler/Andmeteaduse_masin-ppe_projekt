def v�ljasta_liin(enimi, jnimi, s):
    if enimi == jnimi:
        print(enimi)
        return True
    for i in (0, 1):
        try:
            if v�ljasta_liin(enimi, s[jnimi][i], s):
                print(jnimi)
                return True
        except: pass
    return False
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
print("Kas liin leidub?", v�ljasta_liin('Leida', 'Kalle', s�nastik))
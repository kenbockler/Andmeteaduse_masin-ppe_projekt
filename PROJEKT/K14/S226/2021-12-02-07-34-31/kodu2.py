s = {
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
def väljasta_liin(eellase_nimi, jarglase_nimi, sugupuu):
   for key in sugupuu:
        if eellase_nimi in sugupuu[key]:
            print(key)
            if key == jarglase_nimi:
                break
            väljasta_liin(key, jarglase_nimi, sugupuu)
print(väljasta_liin('Mari', 'Adele', s))
    
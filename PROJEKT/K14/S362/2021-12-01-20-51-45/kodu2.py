def väljasta_liin(eellase_nimi, järglase_nimi,sugupuu_sõnastik):
   for el in sugupuu_sõnastik:
       if eellase_nimi in sugupuu_sõnastik[el]:
            print(eellase_nimi)
            väljasta_liin(el, järglase_nimi,sugupuu_sõnastik)
            if el==järglase_nimi:
                print(järglase_nimi)
                break
            return True
   return False
sõnastik={
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
print("Kas liin leidub?", väljasta_liin('Jürgen', 'Kaja',sõnastik))

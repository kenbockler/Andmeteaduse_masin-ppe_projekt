s�nastik ={
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
def v�ljasta_liin(nimi1, nimi2 , s�nastik):
    if nimi2 in s�nastik:
        kiri = s�nastik[nimi2]
        if kiri[0] == nimi1:
            print(kiri[0])
            return True
        if kiri[1] == nimi1:
            print(kiri[1])
            return True
        if v�ljasta_liin(nimi1, kiri[0] , s�nastik) is True:
            print(kiri[0])
            if kiri[0] != nimi2:
                print(nimi2)
            return True
        if v�ljasta_liin(nimi1, kiri[1] , s�nastik) is True:
            print(kiri[1])
            if kiri[1] != nimi2:
                print(nimi2)
            return True
        if v�ljasta_liin(nimi1, kiri[0] , s�nastik) is False or v�ljasta_liin(nimi1, kiri[1] , s�nastik) is False:
            return False
    if nimi2 not in s�nastik:
        return False
v�ljasta_liin('Leida', 'Kalle', s�nastik)
s�nastik={
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
    if eellane in s�nastik[j�rglane]:
        print(eellane)
        return True
    else:
        isa, ema=s�nastik[j�rglane]
        if isa in s�nastik:
            v�ljasta_liin(eellane, isa, s�nastik)
            if ema in s�nastik:
                v�ljasta_liin(eellane, ema, s�nastik)
            else:
                return False
print('Kas liin leidub?', v�ljasta_liin('Leida', 'Kalle', s�nastik))
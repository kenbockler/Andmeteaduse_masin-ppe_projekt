import math
L = int(input('Sisestage Liini pikkus: '))
PMK =int(input('Sisestage kõrvutiseisvate postide maksimaalkaugus: '))
postide_arv = (L/PMK)+1
print(math.ceil(postide_arv))
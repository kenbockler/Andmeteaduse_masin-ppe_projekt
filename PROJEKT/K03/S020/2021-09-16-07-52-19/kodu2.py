'''
Kirjuta Pykkari programm, mis suvalise ristk�likukujulise maailma puhul v�rvib �ra maailma iga nurga.
Programm peab t��tama olenemata roboti algpositsioonist ja vaatesuunast.
V�ib eeldada, et maailm on seest t�hi
(s.t pykkar asub ristk�likukujulises seest t�hjas seintega piiratud maailmas).
'''
from pykkar import *
create_world("""
""")
suund = get_direction()
while not is_wall():
    step()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
'''    
if suund == "E":
    print(suund)
if suund == "S":
    print(suund)
if suund == "W":
    print(suund)
right()
right()
'''
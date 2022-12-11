'''
Kirjuta Pykkari programm, mis suvalise ristkülikukujulise maailma puhul värvib ära maailma iga nurga.
Programm peab töötama olenemata roboti algpositsioonist ja vaatesuunast.
Võib eeldada, et maailm on seest tühi
(s.t pykkar asub ristkülikukujulises seest tühjas seintega piiratud maailmas).
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
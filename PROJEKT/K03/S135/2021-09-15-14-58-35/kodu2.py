from pykkar import *
nurkadeArv = 0
create_world("""
""")
while True:
    if is_wall():
        right()
        break
    step()
if is_wall():
    paint()
    right()
    nurkadeArv += 1
while nurkadeArv != 4:
    if is_wall():
        paint()
        right()
        nurkadeArv += 1
    step()

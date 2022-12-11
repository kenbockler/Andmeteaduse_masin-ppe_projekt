from pykkar import *
create_world("""
""")
nurgad = 0
while not is_wall():
    step()
    if is_wall():
        nurgad += 1
        paint()
        right()
        step()
    if nurgad == 4:
        break

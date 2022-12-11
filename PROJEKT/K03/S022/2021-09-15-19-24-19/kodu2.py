from pykkar import *
create_world("""
""")
nurkadearv = 0
while not is_wall():
    step()
while is_wall():
    right()
while not is_wall():
    if nurkadearv > 4:
        break
    step()
    while is_wall():
        paint()
        nurkadearv = nurkadearv + 1
        right()
        
from pykkar import *
create_world("""
""")
i=0
while not is_wall() and i<4:
    right()
    i = i + 1
right()
while not is_wall():
    step()
right()
if i<4:
    paint()
while not is_wall():
    step()
right()
paint()
while not is_wall():
    step()
right()
paint()
while not is_wall():
    step()
right()
paint()
if i>=4:
    while not is_wall():
        step()
    right()
    paint()
bye()
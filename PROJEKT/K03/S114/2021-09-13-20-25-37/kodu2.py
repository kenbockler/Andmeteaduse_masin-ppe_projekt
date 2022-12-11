from pykkar import *
create_world("""
""")
i = 1
while i > 0:
    if get_direction() != 'N':
        right()
    elif get_direction() == 'N':
        i -=1
        right()
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

from pykkar import *
create_world("""
""")
if get_direction() == E:
    right()
if get_direction() == N:
    right()
    right()
if get_direction() == W:
    right()
    right()
    right()
while not is_wall():
    step()
if is_wall():
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
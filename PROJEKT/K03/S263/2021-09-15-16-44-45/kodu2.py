from pykkar import *
create_world("""
""")
if is_wall:
    right()
    step()
while not is_wall():
    step()
right()
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
while not is_wall():
    step()
right()
paint()

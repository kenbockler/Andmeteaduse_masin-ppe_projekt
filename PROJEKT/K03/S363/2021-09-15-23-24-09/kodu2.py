from pykkar import *
create_world("""
""")
suund = get_direction()
while get_direction() != "N":
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
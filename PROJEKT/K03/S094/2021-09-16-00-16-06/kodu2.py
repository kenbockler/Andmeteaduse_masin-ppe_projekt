from pykkar import *
create_world("""
""")
while(get_direction() == "W" or get_direction() == "N" or get_direction() == "E"):
    right()
    if (get_direction() == "S"):
        break
while not(is_wall()):
    step()
    if (is_wall()):
        break
while(is_wall()):
    right()
    if not(is_wall):
        break
while not(is_wall()):
    step()
    if (is_wall()):
        paint()
        right()
        continue

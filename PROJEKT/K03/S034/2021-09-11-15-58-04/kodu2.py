from pykkar import *
create_world("""
""")
asukoht = get_direction()
if asukoht == "S":
    right()
    right()
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
elif asukoht == "W":
    right()
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
elif asukoht == "N":
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
elif asukoht == "E":
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

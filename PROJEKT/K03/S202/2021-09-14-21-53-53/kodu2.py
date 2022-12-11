from pykkar import *
create_world("""
""")
gd = get_direction()
if gd == "S":
    while not is_wall():
        step()
elif gd == "W":
    right()
    right()
    right()
elif gd == "N":
    right()
    right()
elif gd == "E":
    right()
gd=get_direction()
if gd == "S":
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
paint()
print("Nurgad värvitud")

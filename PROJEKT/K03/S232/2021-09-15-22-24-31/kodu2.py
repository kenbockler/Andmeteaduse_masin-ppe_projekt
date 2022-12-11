from pykkar import *
create_world("""
""")
def gotowall():
    while not is_wall():
     step()
f = 0
g = get_direction()
gotowall()
right()
gotowall()
paint()
f += 1
while is_wall() and is_painted():
    right()
    gotowall()
    paint()
    f += 1
    if f == 4:
        break

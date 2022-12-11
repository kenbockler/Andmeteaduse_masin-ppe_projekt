from pykkar import *
def liigu():
    while not is_wall():
        step()
    paint()
    right()
create_world("""
""")
for i in range(4):
    liigu()
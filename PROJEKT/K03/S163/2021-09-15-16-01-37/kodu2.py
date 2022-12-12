from pykkar import *
create_world("""
""")
while True:
    if is_wall() == False:
        step()
    if is_wall() == True:
        right()
        right()
        right()
        if is_wall() == True:
            paint()
            right()
            right()
        else:
            right()
            right()
    
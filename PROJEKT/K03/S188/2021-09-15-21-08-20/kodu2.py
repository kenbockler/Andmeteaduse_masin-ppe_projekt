from pykkar import *
create_world("""
""")
i = 0
while is_wall():
    right()
while not is_wall():
    step()
    if is_wall() and i == 0:
        while is_wall():
            right()
        i += 1
    elif is_wall() and i < 4:
        paint()
        right()
        i += 1
    elif is_wall() and i == 4:
        paint()
        break

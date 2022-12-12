from pykkar import *
create_world("""
""")
if is_wall():
    right()
    right()
while not is_wall():
    step()
    if is_wall():
        right()
        while not is_wall():
            step()
            if is_wall():
                break
right()
paint()
i = 0
while i < 3:
    while not is_wall():
        step()
        if is_wall():
            right()
            paint()
            i += 1
            break
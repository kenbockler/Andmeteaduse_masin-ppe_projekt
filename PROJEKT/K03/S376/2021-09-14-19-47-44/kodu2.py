from pykkar import *
create_world("""
""")
suund = get_direction()
while suund != "W":
    right()
    suund = get_direction()
    if suund == "W":
        break
while not is_wall():
    step()
    if is_wall():
        right()
        while not is_wall():
            step()
        else:
            break
paint()
right()
while not is_wall():
    step()
    if is_wall():
        if is_painted():
            break
        else:
            paint()
            right()
    continue
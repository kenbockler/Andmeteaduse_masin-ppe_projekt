from pykkar import *
create_world("""
""")
nurki = 0
while nurki <= 10:
    if is_wall():
        paint()
        right()
    else:
        while not is_wall():
            step()
    nurki += 1
from pykkar import *
create_world("""
""")
while not is_wall():
    step()
right()
while True:
    while not is_wall():
        step()
    right()
    if is_painted():
        break
    else:
        paint()
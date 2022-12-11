from pykkar import *
create_world("""
""")
def left():
    right()
    right()
    right()
nurk = 0
while nurk < 4:
    if is_wall() == False:
        step()
    else:
        left()
        if is_wall():
            paint()
            nurk += 1
        right()
        right()

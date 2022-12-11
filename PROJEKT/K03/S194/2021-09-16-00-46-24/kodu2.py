from pykkar import *
create_world("""
""")
def turnaround():
    right()
    right()
def turn_left():
   right()
   right()
   right()
def nurgadvarvi():
    while not is_wall():
        step()
    right()
    p = 0
    while p < 4:
        while not is_wall():
            step()
        paint()
        p += 1
        right()
nurgadvarvi()
    
from pykkar import *
from time import sleep
create_world("""
""")
painted = 0
def left():
    right()
    right()
    right()
while True:
    step()
    if is_wall():
        left()
        if is_wall():
            paint()
            painted += 1
            if painted == 4:
                sleep(0.5)
                break
            right()
            right()
print("Valmis!")

from pykkar import *
create_world("""
""")
def left():
    rigth()
    right()
    right()
def forward():
    while not is_wall():
        step()
def northeast():
    while get_direction() != "N":
        right()
    forward()
    right()
    forward()
northeast()
while not is_painted():
    paint()
    right()
    forward()
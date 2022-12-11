from pykkar import *
create_world("""
""")
def bottom_right_corner_search():
    while not is_wall():
        step()
    right()
    step()
    while not is_wall():
        step()
    paint()
    right()
def next_corner():
    while not is_wall():
        step()
    paint()
    right()
bottom_right_corner_search()
next_corner()
next_corner()
next_corner()

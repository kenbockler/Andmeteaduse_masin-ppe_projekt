from pykkar import *
create_world("""
""")
while not is_wall():
    step()
right()
while not is_wall():
    step()
if is_wall() and not is_painted():
    paint()
right()
while not is_wall():
    step()
if is_wall() and not is_painted():
    paint()
right()
while not is_wall():
    step()
if is_wall() and not is_painted():
    paint()
right()
while not is_wall():
    step()
if is_wall() and not is_painted():
    paint()
right()
exitonclick()

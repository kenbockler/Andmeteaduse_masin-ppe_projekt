from pykkar import *
create_world("""
""")
while not is_wall():
    step()
right()
while not is_wall():
    step()
i = 0
while i < 4:
    i += 1
    paint()
    right()
    if i < 4:
        while not is_wall():
            step()
exitonclick()
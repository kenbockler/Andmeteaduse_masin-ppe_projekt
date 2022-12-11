from pykkar import *
i=0
create_world("""
""")
while not is_wall():
    step()
while i < 4:
    i+=1
    right()
    while not is_wall():
        step()
    paint()
exitonclick()

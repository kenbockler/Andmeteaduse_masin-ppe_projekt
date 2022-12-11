from pykkar import *
create_world("""
""")
n= 0
i= 1
while n< 4:
    while is_wall():
        right()
    while i== 1:
        step()
        if is_wall():
            right()
            i+= 1
    while i== 2 and n<4 :
        if not is_wall():
            step()
        elif is_wall():
            paint()
            right()
            n+= 1
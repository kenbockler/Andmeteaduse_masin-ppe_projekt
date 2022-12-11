from pykkar import *
create_world("""
""")
'''while not is_wall():
    step()
    if is_wall():
        right()
        paint()
        if is_painted():
            break
            right()'''
i=4
while not is_wall():
    step()
    if is_wall():
        break
while i>0:
    right()
    while not is_wall():
        step()
        if is_wall():
            paint()
            break
    i=i-1
right()
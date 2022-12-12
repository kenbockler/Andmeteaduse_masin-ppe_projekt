from pykkar import *
create_world("""
while True:
    if is_wall() == True:
        break
    else:
        step()
right()
n = 0
while n<4:
    if is_wall() == True:
        paint()
        right()
        n +=1
    else:
        step()
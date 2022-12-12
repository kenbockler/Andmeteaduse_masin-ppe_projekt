from pykkar import *
while not is_wall():
    step()
while True:
    right()
    while not is_wall():
        step()
    if is_painted():
        break
    else:
        paint()

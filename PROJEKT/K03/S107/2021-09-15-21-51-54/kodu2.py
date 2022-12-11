from pykkar import *
create_world('''
''')
while not is_wall():
        step()
while True:
    if is_wall():
        right()
    else:
        step()
    if is_wall():
            right()
            paint()

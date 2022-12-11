from pykkar import *
create_world("""
""")
while not is_wall():
    step()
else:
    paint()
    right()
    step()
    
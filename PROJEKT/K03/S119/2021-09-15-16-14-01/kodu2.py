from pykkar import *
create_world("""
""")
sein = 0
while True:
    if is_wall():
        right()
        sein += 1
        if sein > 1:
            paint()
    else:
        step()

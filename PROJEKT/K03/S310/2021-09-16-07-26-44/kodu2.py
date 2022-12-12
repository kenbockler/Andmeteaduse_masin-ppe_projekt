from pykkar import *
create_world("""
""")
ilmakaar = get_direction()
if ilmakaar == 'N':
        right()
elif ilmakaar == 'W':
        right()
        right()
elif ilmakaar == 'S':
        right()
        right()
        right()
i = 0
while i < 3:
    while not is_wall():
        step()
    paint()
    i = i + 1
    right()

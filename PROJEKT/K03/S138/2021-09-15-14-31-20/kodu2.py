from pykkar import *
create_world("""
""")
def Nurgas():
    i = 0
    kogus = 0
    while i < 4:
        i = i + 1
        if is_wall():
            kogus = kogus + 1
        right()
    return kogus
while not is_wall():
    step()
värvitud = 0
while True:
    nurgas = Nurgas()
    if nurgas == 1:
        right()
        while not is_wall():
            step()
    elif nurgas == 2:
        värvitud = värvitud + 1
        right()
        paint()
        if värvitud == 4:
            break
        while not is_wall():
            step()

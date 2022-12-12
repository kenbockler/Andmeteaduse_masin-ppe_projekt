from pykkar import *
create_world("""
""")
def nurk():
    pöörete_arv = 0
    while pöörete_arv <= 2:
        right()
        if is_wall():
            paint()
        pöörete_arv += 1
while not is_wall():
    step()
    if is_wall():
        nurk()

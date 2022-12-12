from pykkar import *
create_world("""
""")
def sein():
    x = 0
    if(is_wall()):
        x += 1
    right()
    if(is_wall()):
        x += 1
    right()
    if(is_wall()):
        x += 1
    right()
    if(is_wall()):
        x += 1
    right()
    if (x==2):
        paint()
        x = 0
while not is_painted():
    while(is_wall()):
        sein()
        right()
    while not is_wall(): 
        step()

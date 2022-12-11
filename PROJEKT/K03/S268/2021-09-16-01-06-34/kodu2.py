from pykkar import *
create_world("""
""")
while not is_wall(): 
    step()
right()
paint()
if is_wall(): 
    step()
while not is_wall():
    step()
right()
paint()
while not is_wall(): 
    step()
right()
paint()
while not is_wall(): 
    step()
right()
paint()

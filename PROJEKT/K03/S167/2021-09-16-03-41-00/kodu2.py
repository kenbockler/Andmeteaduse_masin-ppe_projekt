from pykkar import *
create_world("""
""")
a = get_direction()
print(a)
while not is_wall():
     step()
     if is_wall():
         break
right()
while not is_wall():
     step()
     if is_wall():
         break
right()
paint()
while not is_wall():
     step()
     if is_wall():
         break
right()
paint()
while not is_wall():
     step()
     if is_wall():
         break
right()
paint()
while not is_wall():
     step()
     if is_wall():
         break
right()
paint()
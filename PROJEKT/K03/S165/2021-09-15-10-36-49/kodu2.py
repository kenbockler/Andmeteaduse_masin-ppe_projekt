from pykkar import *
create_world("""
""")
while True:
    while not is_wall(): 
        step()
    right()    
    while not is_wall(): 
        step()
    värvitud = is_painted()
    if  värvitud == False:
        paint()
    else:
        break

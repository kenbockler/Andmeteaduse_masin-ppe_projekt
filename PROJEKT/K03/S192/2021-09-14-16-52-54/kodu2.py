from pykkar import *
create_world("""
""")
nurk = 1
while nurk <= 4:
    while not is_wall():
        step()
    right()
    right()
    right()
    if is_wall() == False:
        right()
        right()
    elif is_wall() == True:
        right()
        right()
        paint()
        nurk += 1
print("Nurgad on värvitud")        

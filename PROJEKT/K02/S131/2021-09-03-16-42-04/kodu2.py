import math
def pole_count(road_len : int, max_dis : int):
    poles = road_len/max_dis
    return int(math.ceil(poles)) + 1
while True:
    try:
        road_len = int(input('Sisesta tee pikkus täisarvuna (meetrites): '))
        max_dis = int(input('Sisesta maksimaalne postide kaugus täisarvune (meetrites): '))
        print(pole_count(road_len, max_dis))
        break
    except:
        print('Palun sisesta väärtused täisarvudena!\n')
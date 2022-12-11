def moos(big_ones, small_ones, amount):
    used_boxes = 0
    while big_ones >= 1 and amount >= 5:
        amount -= 5
        big_ones -= 1
        used_boxes  = used_boxes  +1
    if small_ones >= amount:
        used_boxes = used_boxes + amount
        return used_boxes
    else:
        return -1
print(moos(3, 8, 23))
print(moos(3, 3, 8))
print(moos(1, 2, 10))
print(moos(5, 1, 9))
print(moos(2, 100, 10))
    
import random
def minu_shuffle(random_list):
    for i in range(len(random_list)-1, 0, -1):
        random_index = random.randint(0, i + 1)
        random_list[i], random_list[random_index] = random_list[random_index], random_list[i]
        return(random_list)
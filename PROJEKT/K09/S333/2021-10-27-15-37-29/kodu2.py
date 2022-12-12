def minu_shuffle(järjend):
    from random import randint, sample
    for i in range(len(järjend)):
        juh_index0= randint(0,len(järjend)-1)
        juh_index1= randint(0,len(järjend)-1)
        järjend[juh_index0], järjend[juh_index1]= järjend[juh_index1], järjend[juh_index0]
  
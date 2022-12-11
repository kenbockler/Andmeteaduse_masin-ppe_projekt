'''-- Kodutöö nr. 15 - 2. Järjesta punktid --'''
def järjesta_punktid(järjend):
    for i in range(len(järjend)):
        min = i
        for j in range(i+1, len(järjend)):
            if järjend[j][1] == järjend[min][1]:
                if järjend[j][0] < järjend[min][0]:
                    min = j
            if järjend[j][0] == järjend[min][0]:
                if järjend[j][1] < järjend[min][1]:
                    min = j
            if järjend[j][1] < järjend[min][1]:
                min = j
        if i != min:
            järjend[i], järjend[min] = järjend[min], järjend[i]
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
p = [(1, 4), (6, 4), (4, 4), (3, 4)]
p = [(2, 3), (2, 5), (2, 2), (2, 4)]
p = [(4, 2), (5, 3), (6, 1)]
p = [(3, 6), (5, 3), (2, 2), (2, 1), (3, 5), (4, 6)]
p = [(1, 2), (2, 1)]
print(p)
järjesta_punktid(p)
print(p)
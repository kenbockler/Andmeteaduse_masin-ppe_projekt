p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(järjend):
    n = len(järjend)
    for i in range(n):
        for j in range(0, n-i-1):
            if järjend[j][1] > järjend[j + 1][1]:
                järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]
            elif järjend[j][1] == järjend[j + 1][1]:
                if järjend[j] > järjend[j + 1]:
                    järjend[j], järjend[j + 1] = järjend[j + 1], järjend[j]
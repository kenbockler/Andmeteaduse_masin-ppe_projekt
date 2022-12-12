p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(p):
    p = sorted(p, key=lambda t: (t[1], t[0]))
    return p
print(järjesta_punktid(p))
def uusfilminimi():
    file = open('filmid.txt','r')
    divided = file.split('\n')
    nimi = []
    quantity = len(divided)
    for i in quantity:
        x = divided[i]
        x = x.split('-')
        normalname += x
    file.close()
def loetleFilmid(kind):
    x = uusfilminimi()
    uuednimed = []
    try:
        zanr = x.index(kind) - 1
        film = x[zanr]

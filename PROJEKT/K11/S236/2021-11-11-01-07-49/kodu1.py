def seosta_lapsed_ja_vanemad(lapsed, nimed):
    sõnastik = {}
    l = []
    with open(lapsed) as f1:
        for rida in f1:
            rida.split()
    with open(nimed) as f2:
        for rida in f2:
            rida.split(" ", 2)
def võitja(väli):
    suurus = len(väli)
    otsitav_pikkus = 3
    max = suurus - otsitav_pikkus + 1
    tulemus = {'O': 0, 'X': 0}
    for rida in range(suurus):
        for n in range(max):
            lugeja = 0
            for i in range(otsitav_pikkus - 1):
                if väli[rida][i + n] == ' ':
                    break
                if väli[rida][i + n] == väli[rida][i + 1 + n]:
                    lugeja += 1
                if lugeja == otsitav_pikkus - 1:
                    tulemus[väli[rida][i + n]] += 1
    for n in range(max):
        for veerg in range(suurus):
            lugeja = 0
            for i in range(otsitav_pikkus - 1):
                if väli[i + n][veerg] == ' ':
                    break
                if väli[i + n][veerg] == väli[i + n + 1][veerg]:
                    lugeja += 1
                if lugeja == otsitav_pikkus - 1:
                    tulemus[väli[i + n][veerg]] += 1
    for n in range(max):
        for nihe in range(max):
            lugeja = 0
            for i in range(otsitav_pikkus - 1):
                if väli[i + n][i + nihe] == ' ':
                    break
                if väli[i + n][i + nihe] == väli[i + n + 1][i + nihe + 1]:
                    lugeja += 1
                if lugeja == otsitav_pikkus - 1:
                    tulemus[väli[i + n][i + nihe]] += 1
    for n in range(max):
        for nihe in range(max):
            lugeja = 0
            for i in range(otsitav_pikkus - 1):
                if väli[i + n][(suurus - 1) - i - nihe] == ' ':
                    break
                if väli[i + n][(suurus - 1) - i - nihe] == väli[i + n + 1][(suurus - 1) - i - nihe - 1]:
                    lugeja += 1
                if lugeja == otsitav_pikkus - 1:
                    tulemus[väli[i + n][(suurus - 1) - i - nihe]] += 1
    return tulemus
def v�itja(x):
    m�ngu_seis = {}
    j�rjestikused_X = ("X", "X", "X")
    j�rjestikused_O = ("O", "O", "O")
    rida1a = x[0][:3]
    rida1b = x[0][1:]
    rida2a = x[1][:3]
    rida2b = x[1][1:]
    rida3a = x[2][:3]
    rida3b = x[2][1:]
    rida4a = x[3][:3]
    rida4b = x[3][1:]
    rida5a = (x[0][0], x[1][0], x[2][0])
    rida5b = (x[1][0], x[2][0], x[3][0])
    rida6a = (x[0][1], x[1][1], x[2][1])
    rida6b = (x[1][1], x[2][1], x[3][1])
    rida7a = (x[0][2], x[1][2], x[2][2])
    rida7b = (x[1][2], x[2][2], x[3][2])
    rida8a = (x[0][3], x[1][3], x[2][3])
    rida8b = (x[1][3], x[2][3], x[3][3])
    rida9 = (x[1][0], x[2][1], x[3][2])
    rida10a = (x[0][0], x[1][1], x[2][2])
    rida10b = (x[1][1], x[2][2], x[3][3])
    rida11 = (x[0][1], x[1][2], x[2][3])
    rida12 = (x[1][3], x[2][2], x[3][1])
    rida13a = (x[0][3], x[1][2], x[2][1])
    rida13b = (x[1][2], x[2][1], x[3][0])
    rida14 = (x[0][2], x[1][1], x[2][0])
    k�ik_read = [rida1a, rida1b, rida2a, rida2b, rida3a, rida3b, rida4a, rida4b,
                 rida5a, rida5b, rida6a, rida6b, rida7a, rida7b, rida8a, rida8b,
                 rida9, rida10a, rida10b, rida11, rida12, rida13a, rida13b, rida14]
    for i in k�ik_read:
        if i.count("O") >= 3:
            m�ngu_seis["O"] = m�ngu_seis.get("O", 0) + 1
            m�ngu_seis["X"] = m�ngu_seis.get("X", 0)
        elif  i.count("X") >= 3:
            m�ngu_seis["X"] = m�ngu_seis.get("X", 0) + 1
            m�ngu_seis["O"] = m�ngu_seis.get("O", 0)
        else:
            m�ngu_seis["O"] = m�ngu_seis.get("O", 0)
            m�ngu_seis["X"] = m�ngu_seis.get("X", 0)
    return m�ngu_seis   

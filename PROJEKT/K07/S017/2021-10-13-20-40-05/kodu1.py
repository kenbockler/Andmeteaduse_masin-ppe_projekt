def poisse_ja_t�drukuid(j�rjend):
    m = 0
    n = 0
    for i in j�rjend:
        if i[-1] == "P":
            m += 1
        if i[-1] == "T":
            n += 1
    return (m, n)
print(poisse_ja_t�drukuid(["Mati P", "Kati T", "Siim Aleksander P", "J�ri P", "Veronika T"]))

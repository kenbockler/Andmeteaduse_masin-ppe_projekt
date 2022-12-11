def seosta_lapsed_ja_vanemad(fail1, fail2):
    f2 = open(fail2)
    isikutes�nastik = {}
    for rida in f2:
        rida = (rida.strip("\n")).split()
        isikutes�nastik[rida[0]] = rida[1] + " " + rida[2]
    f2.close()
    f1 = open(fail1)
    s�nastik = {}
    for rida in f1:
        rida = (rida.strip("\n")).split()
        laps = isikutes�nastik[rida[1]]
        vanem = isikutes�nastik[rida[0]]
        if laps not in s�nastik:
            s�nastik[laps] = set()
        if vanem not in s�nastik[laps]:
            s�nastik[laps].add(vanem)
    f1.close()
    return s�nastik
vastus = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for v�ti in vastus:
    print(v�ti, end = ": ")
    if len(vastus[v�ti]) == 2:
       nimed = ", ".join(str(s) for s in vastus[v�ti])
       print(nimed)
    else:
        print(str(vastus[v�ti]).strip("{'").strip("'}"))

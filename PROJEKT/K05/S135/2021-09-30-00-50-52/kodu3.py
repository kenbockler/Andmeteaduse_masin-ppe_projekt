def moos(suurKarp, vaikeKarp, moosiKogus):
    if moosiKogus > suurKarp * 5 + vaikeKarp or moosiKogus - moosiKogus // 5 * 5> vaikeKarp:
        return -1
    karpideArv = moosiKogus // 5
    if karpideArv > suurKarp:
        karpideArv = suurKarp
    moosiKogus -= karpideArv * 5
    if moosiKogus > 0:
        karpideArv += moosiKogus
    return karpideArv
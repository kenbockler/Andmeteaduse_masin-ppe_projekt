isikukoodid=open('lapsed.txt')
vanemad=open('nimed.txt')
def seosta_lapsed_ja_vanemad(isikukoodid,vanemad):
    s�nastik={}
    for rida in isikukoodid:
        if rida=='':
            break
        andmed=rida.strip().split()
        for kood in andmed:
            s�nastik[andmed[0]]=andmed[1]
    print(s�nastik)
    return s�nastik
seosta_lapsed_ja_vanemad(isikukoodid, vanemad)
isikukoodid.close()
vanemad.close()
    
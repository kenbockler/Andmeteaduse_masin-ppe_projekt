import math
liin = input("Kui pikk on liin? Sisesta t�isarv: ")
l = int(liin)
postid = input("Kui suur on maksimaalne kahe posti vahe? Sisesta t�isarv: ")
p = int(postid)
print("Poste kulub: ", math.ceil(l/p + 1))
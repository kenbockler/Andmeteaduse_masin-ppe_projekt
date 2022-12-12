x=input("Sisesta elektriliini pikkus: ")
y=input("Sisesta postide vahemaa: ")
if x<y:
    print("Sisesta sobiv postide vahemaa")
else:
    z=int(x)//int(y)+1
    print("Sinu elektriliinile saab rajada ", z, " posti")
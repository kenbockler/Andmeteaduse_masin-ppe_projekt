import turtle
f = open("turtle_palette.txt")
palett = ""
while True:
    rida = f.readline().strip()
    if rida == "":
        break
    for i in range(rida.count("{")):
        if rida.find("{") != -1 and rida.find("}") != -1:
            rida = rida[:rida.find("{")] + rida[rida.find("}")+1:]
    palett += " "+rida.strip()
f.close()
palett = palett.split()
f.close()
turtle.setup(800, 600)
turtle.speed(0)
turtle.delay(0)
pöördenurk = 360/len(palett)
suund = 90
raadius = 150
punkt = (25 + raadius, 50)
ringi_punkt = (25, 50)
for värv in palett:
    turtle.color(värv, värv)
    turtle.penup()
    turtle.goto(punkt)
    turtle.setheading(suund)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(raadius, extent = pöördenurk)
    suund = turtle.heading()
    punkt = turtle.position()
    turtle.penup()
    turtle.goto(ringi_punkt)
    turtle.end_fill()
turtle.exitonclick()
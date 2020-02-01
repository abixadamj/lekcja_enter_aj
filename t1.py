# Tu dodaję tekst
import turtle
z = turtle.Turtle()

def kwadrat(pozycja, bok):
    z.pu()
    z.goto(pozycja)
    z.pd()
    for k in range(4):
        z.fd(bok)
        z.rt(90)
co kolwiek

b = 10
p = 20, 60
r = -20, -30
#kwadrat(p, b)
#kwadrat(r, b)
for i in range(6):
    print(f"i wynosi {i}")
    kwadrat(p, b * i)



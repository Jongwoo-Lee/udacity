import turtle

def draw_triangle(tur,step):
    for i in range(1,4):
        tur.forward(tur.size*pow(2,step))
        tur.left(120)


def fractal(tur,step):
    if step == 0:
        return
    for i in range(1,4):
        fractal(tur,step-1)
        if i == 1:
            tur.forward(tur.size*pow(2,step))
            draw_triangle(tur,step)
        if i == 2:
            tur.left(120)
            tur.forward(tur.size*pow(2,step))
            tur.right(120)
            draw_triangle(tur,step)
        if i == 3:
            tur.right(120)
            tur.forward(tur.size*pow(2,step))
            tur.left(120)


def draw_fractal(step):

    window = turtle.Screen()
    window.bgcolor("black")
    
    asd = turtle.Turtle()
    asd.shape("turtle")
    asd.color("green")
    asd.speed(100)
    asd.size = 10

    asd.penup()
    asd.setx(-320)
    asd.sety(-200)
    asd.pendown()

    fractal(asd,step)
  


    window.exitonclick()


draw_fractal(5)

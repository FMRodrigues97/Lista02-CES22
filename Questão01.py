import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title('Tess becomes a traffic light')
wn.bgcolor('lightgreen')
tess = turtle.Turtle()
raio = 3

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color('black', 'darkgrey')
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape('circle')
tess.shapesize(3)
tess.fillcolor('green')

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:  # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


def mudar_para_vermelho():
    tess.fillcolor('red')


def mudar_para_verde():
    tess.fillcolor('green')


def mudar_para_azul():
    tess.fillcolor('blue')


def tonalidade_clara():
    wn.bgcolor('lightgreen')


def tonalidade_escura():
    wn.bgcolor('darkgreen')


def decrease_size():
    global raio
    if raio >= 2:
        raio -= 1
        tess.shapesize(raio)


def increase_size():
    global raio
    if raio <= 19:
        raio += 1
        tess.shapesize(raio)


# Bind the event handler to the space key.
wn.onkey(advance_state_machine, 'space')

# Pressionando as teclas "r", "g" ou "b" a cor muda para vermelho, verde ou azul, respectivamente.
wn.onkey(mudar_para_vermelho, 'r')
wn.onkey(mudar_para_verde, 'g')
wn.onkey(mudar_para_azul, 'b')

# Pressionando as teclas "+" ou "-" aumenta ou diminui, respectivamente, o raio do círculo.
wn.onkeypress(increase_size, "plus")
wn.onkeypress(decrease_size, "minus")

# Pressionando as teclas "d" ou "l" aumenta ou diminui a tonalidade de verde do fundo.
wn.onkey(tonalidade_clara, 'l')
wn.onkey(tonalidade_escura, 'd')

wn.listen()  # Listen for events
wn.mainloop()

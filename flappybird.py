import turtle , time , random

window = turtle.Screen()
canvas = window.getcanvas()
root = canvas.winfo_toplevel()
window.title('Flappy Bird')
window.bgcolor('blue')
window.bgpic('flappybird.gif')
window.setup(width=500, height=700)
window.tracer(0)

window.register_shape('bird.gif')

bird = turtle.Turtle()
bird.speed(0)
bird.color('yellow')
bird.shape('bird.gif')
bird.penup()
bird.goto(-180, 0)
bird.dx = 0
bird.dy = 1

point = 100
write = turtle.Turtle()
write.speed(0)
write.color('black')
write.shape('square')
write.hideturtle()
write.penup()
write.goto(0, 300)

Gravity = -0.3

def bird_up(x, y):
    bird.dy = bird.dy + 8

    if bird.dy > 8:
        bird.dy = 8

def close():
    global Continue
    Continue = False

pipes = []
window.listen()
window.onscreenclick(bird_up)
root.protocol("WM_DELETE_WINDOW", close)
Continue = True

starting_time = time.time()
while Continue:

    time.sleep(0.02)
    window.update()

    bird.dy = bird.dy + Gravity

    if (time.time() - starting_time > random.randint(5, 15)):
        starting_time = time.time()
        pipe_top = turtle.Turtle()
        pipe_top.speed(0)
        pipe_top.color('red')
        pipe_top.shape('square')
        pipe_top.h = random.randint(10, 20)
        pipe_top.shapesize(pipe_top.h, 2, outline=None)
        pipe_top.penup()
        pipe_top.goto(300, 250)
        pipe_top.dx = -2
        pipe_top.dy = 0

        pipe_lower = turtle.Turtle()
        pipe_lower.speed(0)
        pipe_lower.color('red')
        pipe_lower.shape('square')
        pipe_lower.h = 40 - pipe_top.h - random.randint(1, 10)
        pipe_lower.shapesize(pipe_lower.h, 2, outline=None)
        pipe_lower.penup()
        pipe_lower.goto(300, -250)
        pipe_lower.dx = -2
        pipe_lower.dy = 0

        pipes.append((pipe_top, pipe_lower))

    y = bird.ycor()
    y = y + bird.dy
    bird.sety(y)

    if len(pipes) > 0:
        for pipe in pipes:
            x = pipe[0].xcor()
            x = x + pipe[0].dx
            pipe[0].setx(x)
            x = pipe[1].xcor()
            x = x + pipe[1].dx
            pipe[1].setx(x)
            if pipe[0].xcor() < -300:
                pipe[0].hideturtle()
                pipe[1].hideturtle()
                pipes.pop(pipes.index(pipe))
            if (bird.xcor()+10>pipe[0].xcor()-20) and (bird.xcor()-10<pipe[0].xcor()+20):
                if (bird.ycor()+10>pipe[0].ycor()-pipe[0].h*10) or (bird.ycor()-10<pipe[1].ycor()+pipe[1].h*10):
                    point = point -1
                    write.clear()
                    write.write('Point: {}'.format(point), align='center', font=('Courier', 24, 'bold'))

        if point < 0:
            write.clear()
            write.write('You Lose', align='center', font=('Courier', 24, 'bold'))
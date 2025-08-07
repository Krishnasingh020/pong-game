#simple Pong game in python 3

import turtle

wn = turtle.Screen()
wn.title("Pong by @krishnasinhg020")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turns off the screen updates


#main game loop
while True:
    wn.update()

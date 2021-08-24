import turtle as T
import time as t
import random as r

COLOR = ["red","green","blue","orange","yellow","black","pink",'lime','olive','seagreen']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers in the game(2 - 10): ")
        print("\n\n")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input!!Please enter a character")
            print("\n\n")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Too many racers!! Enter something small")
            print("\n\n")

def Screen():

    WIDTH = 500
    HEIGHT = 500
    T.Screen().setup(WIDTH,HEIGHT)
    T.Screen().title("TurtleRace")

def turtle_racers(no):
    turtle_no = []
    x = -230; y = -230

    for a,b in enumerate(no):
        racers = T.Turtle()
        racers.color(b)
        racers.shape("turtle")
        racers.left(90)
        racers.penup()
        racers.setpos(x , y)
        x += (480 // len(colors))
        racers.pendown()
        turtle_no.append(racers)

    return turtle_no


def Race(colors):

    turtleobj = turtle_racers(colors)

    while True:
        for racers in turtleobj:
            dis = r.randrange(1,15)
            racers.forward(dis)

            x , y = racers.pos()
            if y >= 240:
                return colors[turtleobj.index(racers)]



Screen()
racers = get_number_of_racers()

r.shuffle(COLOR)
colors = COLOR[:racers]

winner = Race(colors)
print("The winner of the race is color: " + winner.upper())

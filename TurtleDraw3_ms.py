# Turtle-Draw
#
# By: Michael Santay
# # Credits: Michael Santay; based on TurtleDraw Lite example by Eric Pogue
#
#

print('Starting Turtle Draw')

import os
import sys
import turtle

screen = turtle.Screen()
screen.setup(width=450, height=450)

print("Enter file name (i.e., turtle-draw.txt):")
TDraw = input()

if os.path.exists(TDraw):
    print("Opening file...")
else:
    print("File does not exist.")
    sys.exit()

MyTurtle = turtle.Turtle()
MyTurtle.speed(10)
MyTurtle.penup()

print("Reading text line by line")

turtleDrawTextfile = open(TDraw, 'r')
line = turtleDrawTextfile.readline()
total_dist = 0

while line:
    line = line.strip()
    print(line, end='')

    parts = line.split()

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        MyTurtle.color(color)

        if MyTurtle.isdown():
            total_dist += MyTurtle.distance(x, y)

        MyTurtle.goto(x, y)
        MyTurtle.pendown()

    elif 'stop' in line.lower():
        MyTurtle.penup()

    line = turtleDrawTextfile.readline()

MyTurtle.penup()
MyTurtle.goto(50, -200) 
MyTurtle.color("black")

MyTurtle.write(f"Total distance marked: {total_dist:.2f}", font=("Arial", 8,))

turtleDrawTextfile.close()
input("Press Enter to close")
turtle.bye()

print('\nEnd')
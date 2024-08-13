#import colorgram
from turtle import Turtle, Screen
import turtle as t
import random
t.colormode(255)
#rgp_colors=[]
tim=t.Turtle()
tim.shape("circle")
tim.color("pink")
tim.penup()
tim.hideturtle()
#tim.pensize(10)
#colors= colorgram.extract("image.jpg",30)
#for color in colors:
#    r=color.rgb.r
#    g=color.rgb.g
#    b= color.rgb.b
#    new_color=(r,g,b)
#    rgp_colors.append(new_color)
#print(rgp_colors)

color_list=[(250, 246, 243), (248, 245, 246), (211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]
#

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup
tim.speed("fastest")

x_start = -200  # Starting x position
y_start = -200  # Starting y position
tim.setposition(x_start,y_start)
dot_size = 20  # Size of each dot
gap_size = 50  # Gap between each dot


for j in range (10):#y 0 1 2
    for i in range(10):#x 12345
        x = x_start + (i * gap_size)
        y = y_start + (j * gap_size)
        tim.goto(x, y)
        tim.dot(dot_size, random.choice(color_list))


screen=Screen()
screen.exitonclick()
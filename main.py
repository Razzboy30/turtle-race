from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red,blue,yellow,orange, green, purple):")
colors = ["red","blue","yellow","orange","green","purple"]
y_pos = [-70,-40,-10,20,50,80]
all_turtles = []
is_on = False

for t_ind in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[t_ind])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_pos[t_ind])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on= False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You have won! The winner is {winning_color} turtle")
            else:
                print(f"You have lost! The winner is {winning_color} turtle")
        
        rand_dist = random.randint(0,10)
        turtle.fd(rand_dist)
    
screen.exitonclick()
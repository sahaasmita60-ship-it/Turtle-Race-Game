from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(height=500,width=500)
is_race_on = False
bet=screen.textinput(title="Make your bet on a turtle",prompt="Enter the color you think is gonna win: ")
a=-210
colors=["violet","indigo","blue","green","yellow","orange","red"]
i=0
all=[]
for ind in range(0,7):
    while a<211:
      t=Turtle()
      t.shape("turtle")
      t.penup()
      t.color(colors[i])
      i+=1
      t.goto(x=-200,y=a)
      a+=70
      all.append(t)
if bet:
   is_race_on=True

while is_race_on==True:
   for t in all:
    if t.xcor()>220:
       is_race_on=False
       color=t.pencolor()
       if bet==color:
           print(f"You win. The {color} turtle has won. ")
           break
       else:
           print(f"You lose. The {color} turtle has won. ")
           break
    distance=random.randint(0,10)
    t.forward(distance)


screen.exitonclick()
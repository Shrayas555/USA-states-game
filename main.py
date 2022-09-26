import turtle
from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
image='blank_states_img.gif'
screen.addshape(image)
tim.shape(image)

screen.title('US STATE GAME')

import pandas as pd
data=pd.read_csv('50_states.csv')

missingstate=[]
guessedstate=[]
allstate=data['state'].tolist()
score=0
end=50
game=True
while game:

    guess = screen.textinput(f'{score}/{end} correct', 'whats another state name?').capitalize()
    if guess=='Exit':

        missingstate = [state for state in allstate if state not in guessedstate]
        newdata=pd.DataFrame(missingstate)
        newdata.to_csv('states-learn.csv')
        break

    if guess in allstate:
        t=Turtle()
        t.hideturtle()
        t.penup()
        a=data[data['state']==guess]
        t.goto(int(a['x']),int(a['y']))
        t.write(f'{guess}',align='center')
        score+=1
        guessedstate.append(guess)

    if score==end:
        game=False















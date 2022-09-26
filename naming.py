from turtle import Turtle
import pandas as pd
data=pd.read_csv('50_states.csv')
class Naming:
    def __init__(self):
        self.name=Turtle()
    def stating(self):

        self.name.penup()

        self.name.goto(int(temprow['x']), int(temprow['y']))



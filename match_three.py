from tkinter import *
import time
import math
from functools import partial
import random
import os
from PIL import Image
from fractions import Fraction
seed = [0,1]
def start_drag(event):
    global des
    # Store the initial position of the widget when dragging starts
    event.widget.startX = event.x  # Store initial X position
    event.widget.startY = event.y  # Store initial Y position
    options = [[0,0],[50,0],[50,50],[0,50],[-50,0],[0,-50],[-50,-50],[-50,50],[50,-50]]
    des = []
    for i in options:
        rat = [event.widget.winfo_x() + i[0], event.widget.winfo_y() + i[1]]
        print(rat)
        if rat in grid:
            des.append(rat)

def on_drag(event):
    global clock,widget,drop
    clock +=1
    # Update widget position as it's dragged
    widget = event.widget  # Get reference to the dragged widget

    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y

#https://www.reddit.com/r/algorithms/comments/3byyto/best_way_to_find_the_leftmost_first_digit_of_an/
def leftMostDigit(n):
    highestPower10 = math.floor(math.log10(n))
    return n / (10**highestPower10)

def snap(event):
    pass
def seeder():
    global seed
    seed = [seed[1],seed[0]+seed[1]]
    return leftMostDigit(seed[1])
def gridset():
# impintant!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       up is x not y
    grid = []
    colours = ["#FF0000","#0000FF", "#9D00FF", "#FF8000","#32CD32","#FF0000","#0000FF", "#9D00FF", "#FF8000","#32CD32"]
    for up in range(5):
        tmp=[]
        for a in range(5):
            colour = colours[int(seeder())]
            label = Label(root, bg=colour,height=2, width=4, padx=0, pady=0)
            label.place(x=(a*100)+740,y=(up*100)+400)
            tmp.append([label,[(a*100)+740,(up*100)+400],colour])
        grid.append(tmp)
    for i in grid:
        print(i)

if __name__ == '__main__':
    """who knows what this does"""
    root = Tk()
    root.title("Colour Quest")
    root.attributes("-fullscreen", True)
    gridset()
    root.mainloop()
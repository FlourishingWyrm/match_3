from tkinter import *
import time
import math
from functools import partial
import random
import os
from PIL import Image
from fractions import Fraction
seed = [0,1]
def pos_to_cor(x,y):
    """converts the pixel position to the location on the grid"""
    return (x -740)/100 , (y - 400)/100

def cor_to_pos(x,y):
    """converts the location on the grid to the pixel position on the screen"""
    return (x * 100) + 740, (y*100)+400



def start_drag(event):
    # Store the initial position of the widget when dragging starts
    event.widget.startX = event.x  # Store initial X position
    event.widget.startY = event.y  # Store initial Y position
    event.widget.trux =  event.widget.winfo_x()
    event.widget.truy =  event.widget.winfo_y()

def on_drag(event):
    # Update widget position as it's dragged
    widget = event.widget  # Get reference to the dragged widget

    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y

    widget.place(x=x,y=y)
    widget.bind("<ButtonRelease-1>", snap)

#https://www.reddit.com/r/algorithms/comments/3byyto/best_way_to_find_the_leftmost_first_digit_of_an/
def leftMostDigit(n):
    highestPower10 = math.floor(math.log10(n))
    return n / (10**highestPower10)

def snap(event):
    widget = event.widget  # Get reference to the dragged widget

    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    sx = widget.trux
    sy = widget.truy
    most = 9999999999999999999999999999999999999
    locs = pos_to_cor(sx,sy)
    dists = []
    for t in [1,0,-1]:
        for l in [1,0,-1]:
            dists.append(cor_to_pos(locs[1]+t,locs[0]+l))
    print(dists)
    for i in dists:
        prop = (math.sqrt((i[0]-x)*(i[0]-x)+(i[1]-y)*(i[1]-y)))
        print(prop)
        if prop < most:
            print("     "+str(prop))
            most = prop
            fx,fy = i
    pos_to_cor(fx,fy)
    print(x,y)
    print(fx,fy)
    print(pos_to_cor(fx,fy))
    widget.place(x=fx,y=fy)




# dists.append(math.sqrt(((i[0] - x) * (i[1] - y)) + ((i[1] - y) * (i[1] - y))))

    # widget.place(x=widget.trux,y=widget.truy)

def seeder():
    global seed
    seed = [seed[1],seed[0]+seed[1]]
    return leftMostDigit(seed[1])
def gridset():
# impintant!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       up is x not y
    grid = [["",[-100,-100],""]]
    colours = ["#FF0000","#0000FF", "#9D00FF", "#FF8000","#32CD32","#FF0000","#0000FF", "#9D00FF", "#FF8000","#32CD32"]
    for up in range(5):
        tmp=["",[-100,-100],""]
        for a in range(5):
            colour = colours[int(seeder())]
            label = Label(root, bg=colour,height=2, width=4, padx=0, pady=0)
            label.bind("<ButtonPress-1>", start_drag)  # Detect mouse press to start dragging
            label.bind("<B1-Motion>", on_drag)  # Move label while dragging
            label.place(x=(a*100)+740,y=(up*100)+400)
            tmp.append([label,[(a*100)+740,(up*100)+400],colour])

        grid.append(tmp)
    # for i in grid:
    #     print(i)

if __name__ == '__main__':
    """who knows what this does"""
    root = Tk()
    root.title("Colour Quest")
    root.attributes("-fullscreen", True)
    gridset()
    root.mainloop()
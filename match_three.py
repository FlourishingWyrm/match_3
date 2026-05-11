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
    return int((x -740)/100) , int((y - 400)/100)

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
    # updates the position
    widget.place(x=x,y=y)
    widget.bind("<ButtonRelease-1>", snap)

#https://www.reddit.com/r/algorithms/comments/3byyto/best_way_to_find_the_leftmost_first_digit_of_an/
def leftMostDigit(n):
    """finds the left most diget of a number"""
    highestPower10 = math.floor(math.log10(n))
    return n / (10**highestPower10)

def snap(event):
    """snaps back to the grid and swaps the two tiles (if applicable)"""
    widget = event.widget  # Get reference to the dragged widget
    # possably not nessary can be commented out later
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y

    # could be simplified but gets the original x value of the tile
    sx = widget.trux
    sy = widget.truy
    # unreachable by normal computers
    most = 9999999999999999999999999999999999999
    # converts the pixel position to a position on the grid this could be unnessary ut it makes the math a tad easier to understand
    locs = pos_to_cor(sx,sy)
    # acceptable places for the tile to be moved to
    dists = []
    # essentaly creates a 3x3 grid centered in the start location of tthe piece selected in the grid format
    for t in [1,0,-1]:
        for l in [1,0,-1]:
            dists.append(cor_to_pos(locs[0]+l, locs[1]+t))
    # testing print functions not required but left for now
    print(x, y)
    for i in dists:

        print((i[0],i[1]))
    for i in dists:
        # calculates the distance using fun maths
        prop = math.sqrt((x-i[0])*(x-i[0])+(y-i[1])*(y-i[1]))
        print(prop)
        # if the distance is the shortest its x and y values will be used
        if prop < most and [i[0],i[1]] in acc:
            print("     "+str(prop))
            most = prop
            fx,fy = i
    # thinking code (code written to understand ideas)
    pos_to_cor(fx,fy)
    print(x,y)
    print(fx,fy)
    print(pos_to_cor(fx,fy))

    # swaps the two tiles to be swapped
    widget.place(x=fx,y=fy)
    sec = pos_to_cor(fx+100,fy+100)
    grid[sec[1]][sec[0]][0].place(x=sx,y=sy)
    print(grid[sec[1]][sec[0]],grid[locs[1]+1][locs[0]+1])
    grid[sec[1]][sec[0]],grid[locs[1]+1][locs[0]+1] = grid[locs[1]+1][locs[0]+1],grid[sec[1]][sec[0]]
    print(grid[sec[1]][sec[0]],grid[locs[1]+1][locs[0]+1])
    check()

def check():
    # checks for matches (ie 3 in a row)
    for col in grid[1:]:
        for i in range(5):
            try:
                if col[i][1] == col[i+1][1] == col[i+2][1]: # if match 3
                    if col[i][1] == col[i + 3][1] == col[i + 4][1]: # if match 5
                        print(col[i][2],col[i+1][2],col[i+2][2],col[i + 3][2],col[i + 4][2]) # print for prints sake

                    print(col[i][2],col[i+1][2],col[i+2][2])
            except IndexError:
                continue

# dists.append(math.sqrt(((i[0] - x) * (i[1] - y)) + ((i[1] - y) * (i[1] - y))))

    # widget.place(x=widget.trux,y=widget.truy)

def seeder():
    """updates the seed"""
    global seed
    seed = [seed[1],seed[0]+seed[1]]
    return leftMostDigit(seed[1])
def gridset():
    """creates the grid"""
    global acc,grid
    grid = [["","",999999]] # to make impossable to reach
    acc = []
    colours = ["#FF0000","#0000FF", "#9D00FF", "#FF8000","#32CD32","#FF0000","#0000FF", "#9D00FF", "#FF8000","#32CD32"]
    for up in range(5):
        tmp=[["NONE","",99999]] # to make impossable to reach
        for a in range(5): # creates a row
            x,y = ((a*100)+740,(up*100)+400) # creates the co-ordinates
            colour = colours[int(seeder())] # gets the colour value for the lable (tile)
            label = Label(root, bg=colour,height=2, width=4, padx=0, pady=0,text=str(a+5*up)) # creates the label
            label.bind("<ButtonPress-1>", start_drag)  # Detect mouse press to start dragging
            label.bind("<B1-Motion>", on_drag)  # Move label while dragging
            acc.append([x,y])# appends co-ordinates to an important spot
            label.place(x=x,y=y) # puts the tile on the grid where it goes
            tmp.append([label,colour,str(a+5*up)]) # appends the label and its friends to the row
        print(tmp)

        grid.append(tmp) # puts the row on the rows spot, grid
    # for i in grid:
    #     print(i)

if __name__ == '__main__':
    """who knows what this does"""
    root = Tk()
    root.title("Colour Quest")
    root.attributes("-fullscreen", True)
    gridset()
    root.mainloop()

from tkinter import *
import time
import math
from functools import partial
import random
import os
from PIL import Image
from fractions import Fraction

from samba import colour
colours = ["#FF0000","#0000FF", "#9D00FF", "#FF8000","#32CD32","#FF0000","#0000FF", "#9D00FF", "#FF8000","#32CD32"]
seed = [5,9]
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
    for i in dists:
        # calculates the distance using fun maths
        prop = math.sqrt((x-i[0])*(x-i[0])+(y-i[1])*(y-i[1]))
        # if the distance is the shortest its x and y values will be used
        if prop < most and [i[0],i[1]] in acc:
            most = prop
            fx,fy = i
    # thinking code (code written to understand ideas)
    pos_to_cor(fx,fy)

    # swaps the two tiles to be swapped
    widget.place(x=fx,y=fy)
    sec = pos_to_cor(fx+100,fy+100)
    grid[sec[1]][sec[0]][0].place(x=sx,y=sy)
    grid[sec[1]][sec[0]],grid[locs[1]+1][locs[0]+1] = grid[locs[1]+1][locs[0]+1],grid[sec[1]][sec[0]]
    print(grid[sec[1]][sec[0]],grid[locs[1]+1][locs[0]+1])
    check()

def check():
    """checks for matches (ie 3 in a row)"""
    for x in range(1,6):
        for y in range(1,6):
            try:
                if grid[x][y][1] == grid[x][y+1][1] == grid[x][y+2][1]: # across check due to the downward check checking out of bounds causing it to be skipped
                    fall_replace([x, y + 2])
                    # fall_replace([x, y + 1])
                    # fall_replace([x, y])


                if grid[x][y][1] == grid[x+1][y][1] == grid[x+2][y][1]:
                    fall_replace([x + 2, y])
                    # fall_replace([x + 1, y])
                    # fall_replace([x,y])



            except IndexError:
                continue
            except TypeError:
                continue

def fall_replace(i):
    try:
        if i[1]>0:
            if i[0] >0:
                y = i[1]
                x = i[0]
                # tile[y][x]
                print(grid[y][x])
                grid[y][x] = grid[y-1][x]
                print(grid[y][x])
                grid[y][x][0].config( bg=grid[y][x][1],text=str(x+5*y))




                # print(grid[i[0]-1][i[1]][0])
                # if grid[i[0]-1][i[1]][0] == ["spawn"]:
                #     print("prewhy")
                #     x, y = cor_to_pos(i[0], i[1])
                #     label = Label(root, bg=colours[int(seeder())], height=2, width=4, padx=0, pady=0,
                #                   text=str(i[0] + 5 * i[1]))  # creates the label
                #     label.bind("<ButtonPress-1>", start_drag)  # Detect mouse press to start dragging
                #     label.bind("<B1-Motion>", on_drag)  # Move label while dragging
                #     acc.append([x, y])  # appends co-ordinates to an important spot
                #     grid[i[0]][i[1]] =[label, colour, str(i[0] + 5 * i[1])]  # appends the label and its friends to the row
                #     grid[i[0]][i[1]][0].config(bg=colours[int(seeder())])
                #     #
                #     print("why")
                # else:
                #     print("prewa")
                #     grid[i[0]][i[1]][0].config(bg=grid[i[0]-1][i[1]][1])
                #
                #     grid[i[0]][i[1]] = grid[i[0]-1][i[1]]
                #     x, y = cor_to_pos(i[0], i[1])
                #     grid[i[0]][i[1]][0].place(x=x, y=y)
                #     print("ewa")
                #     print(fall_replace([i[0]-1, i[1]]))
                #
                #
                #
                #     print("wa")

                # print("1")
                # x,y = cor_to_pos(i[0],i[1])
                # print("2")
                # grid[i[0]][i[1]][0].place(x=x,y=y)
                # print(3)
    except AttributeError:
        print("attribute")
        return "fuck"
    except TclError:
        print("tcl")
        return "you"
    # for item in grid:
    #     g = []
    #     for part in item:
    #         g.append(part)
    #     print(g)
def seeder():
    """updates the seed"""
    global seed
    seed = [seed[1],seed[0]+seed[1]]
    return leftMostDigit(seed[1])
def gridset():
    """creates the grid"""
    global acc,grid
    grid = [["spawn"]] # to make impossable to reach
    acc = []

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

        grid.append(tmp) # puts the row on the rows spot, grid

if __name__ == '__main__':
    """who knows what this does"""
    root = Tk()
    root.title("e")
    root.attributes("-fullscreen", True)
    gridset()
    root.mainloop()

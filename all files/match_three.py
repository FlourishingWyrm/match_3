import os
import subprocess
import platform
from tkinter import *
import time
import math

game_state = ["none",1.0,[20,2,7000],0]
colours = ["#FF0000", "#0000FF", "#9D00FF", "#FF8000", "#32CD32", "#FF0000", "#0000FF", "#9D00FF", "#FF8000", "#32CD32"]
level = [1,2]
seed = level
saved = "q"
with open("vars"+".txt", "r") as f:
    exec(f.read())


def wipe(f):
    with open('storage.txt', 'w') as a:
        a.write('n')
    f.destroy()

    saq("'q'")

def uppper(f):
    global level
    level = [level[0]+3,level[1]+5]
    game_state[2][2] = game_state[2][2] *1.5
    wipe(f)

def pos_to_cor(x, y):
    """converts the pixel position to the location on the grid"""
    return int((x - 740) / 100), int((y - 400) / 100)


def cor_to_pos(x, y):
    """converts the location on the grid to the pixel position on the screen"""
    return (x * 100) + 740, (y * 100) + 400


def start_drag(event):
    # Store the initial position of the widget when dragging starts
    event.widget.startX = event.x  # Store initial X position
    event.widget.startY = event.y  # Store initial Y position
    event.widget.trux = event.widget.winfo_x()
    event.widget.truy = event.widget.winfo_y()


def on_drag(event):
    # Update widget position as it's dragged
    widget = event.widget  # Get reference to the dragged widget

    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    # updates the position
    widget.place(x=x, y=y)
    widget.bind("<ButtonRelease-1>", snap)


# https://www.reddit.com/r/algorithms/comments/3byyto/best_way_to_find_the_leftmost_first_digit_of_an/
def leftMostDigit(n):
    """finds the left most diget of a number"""
    highestPower10 = math.floor(math.log10(n))
    return n / (10 ** highestPower10)


def snap(event):
    """snaps back to the grid and swaps the two tiles (if applicable)"""
    print(game_state)
    game_state[2][0] -= 1
    game_state[2][1] -= 1
    if game_state[2][1] == 0:
        game_state[1] = 1.0
    if game_state[2][0] <1:
        # Label(fg="#000000",height=999,width=999).place(x=0,y=0)
        Label(fg="#000000", text="  you died,L  ",font=("Arial", "90", "bold"), height=10,width=10).place(x=650,y=-100)
        Button(bg="#7F6FF8", text="again?",command=lambda: wipe(root)).place(x=930,y=700)
        return ""
    game_state[-1].config(text="Moves:    "+str(game_state[2][0]))

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
    locs = pos_to_cor(sx, sy)
    # acceptable places for the tile to be moved to
    dists = []
    # essentaly creates a 3x3 grid centered in the start location of tthe piece selected in the grid format
    for t in [1, 0, -1]:
        for l in [1, 0, -1]:
            dists.append(cor_to_pos(locs[0] + l, locs[1] + t))
    print(dists)
    for i in dists:

        # calculates the distance using fun maths
        prop = math.sqrt((x - i[0]) * (x - i[0]) + (y - i[1]) * (y - i[1]))
        # if the distance is the shortest its x and y values will be used
        print([i[0], i[1]] in acc)
        print(acc)
        if prop < most and [i[0], i[1]] in acc:
            most = prop
            print("1234567890")
            fx, fy = i

    # thinking code (code written to understand ideas)
    # pos_to_cor(fx, fy)
    # somehow casuing error
    # swaps the two tiles to be swapped
    print(fx, fy, "alkurhfalilygfiagerfilushrfd")
    widget.place(x=fx, y=fy)
    sec = pos_to_cor(fx + 100, fy + 100)
    grid[sec[1]][sec[0]][0].place(x=sx, y=sy)
    grid[sec[1]][sec[0]], grid[locs[1] + 1][locs[0] + 1] = grid[locs[1] + 1][locs[0] + 1], grid[sec[1]][sec[0]]
    check(1)


def check(a=0):
    """checks for matches (ie 3 in a row)"""
    for x in range(1, 6):
        for y in range(1, 6):
            try:
                if grid[x][y][1] == grid[x][y + 1][1] == grid[x][y + 2][1]:  # across check due to the downward check checking out of bounds causing it to be skipped
                    score(grid[x][y][1])
                    grid[x][y + 2][0].destroy()
                    fall_replace([x, y + 2])
                    time.sleep(0.1)  # sleep
                    root.update()  # update
                    grid[x][y + 1][0].destroy()
                    fall_replace([x, y + 1])
                    time.sleep(0.1)  # sleep
                    root.update()  # update
                    grid[x][y][0].destroy()
                    fall_replace([x, y])
                    time.sleep(0.1)  # sleep
                    root.update()  # update
                    if a == 1:
                        game_state[0] = grid[x][y][1]

                    check()  # allows for continuous checks
            except IndexError:
                print("s")
                continue
            except TypeError:
                print("xe")
                continue
    for x in range(1, 6):
        for y in range(1, 6):
            try:
                if grid[x][y][1] == grid[x + 1][y][1] == grid[x + 2][y][1]:
                    score(grid[x][y][1])
                    grid[x][y][0].destroy()
                    fall_replace([x, y])
                    time.sleep(0.1)  # sleep
                    root.update()  # update
                    grid[x + 1][y][0].destroy()
                    fall_replace([x + 1, y])
                    time.sleep(0.1)  # sleep
                    root.update()  # update
                    grid[x + 2][y][0].destroy()
                    fall_replace([x + 2, y])
                    time.sleep(0.1)  # sleep
                    root.update()  # update
                    if a == 1:
                        game_state[0] = grid[x][y][1]

                    check()  # allows for continuous checks
            except IndexError:
                print("s")
                continue
            except TypeError:
                print("xe")
                continue
    if game_state[3] >= game_state[2][2]:
        Label(fg="#000000", text="  YAY, Win  ", font=("Arial", "90", "bold"), height=10, width=10).place(x=650,
                                                                                                            y=-100)
        Button(bg="#7F6FF8", text="next level?", command=lambda: uppper(root)).place(x=930, y=700)
        return ""


def fall_replace(i):
    try:
        x = i[1]
        y = i[0]
        if i[1] > 0:
            if i[0] > 0:
                print(x, y)
                print(grid[y][x])
                grid[y][x] = grid[y - 1][x]
                print(grid[y][x])
                update()
                print(fall_replace([y - 1, x]))

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
        return "censored"
    except TclError:
        print("tcl")
        return "you"
    except IndexError:
        qx = i[1]
        qy = i[0]
        print(qx, qy)

        colour = colours[int(seeder())]
        for f in grid:
            print(f)
        print(grid[qy][qx])
        star = grid[qy][qx]
        star = str(star)
        print(star)
        grid[qy][qx] = [Label(root, bg=colour, height=2, width=4, padx=0, pady=0, text="n"), colour, "n"]
        grid[qy][qx][0].bind("<ButtonPress-1>", start_drag)  # Detect mouse press to start dragging
        grid[qy][qx][0].bind("<B1-Motion>", on_drag)  # Move label while dragging
        print(grid[qy][qx])
        for f in grid:
            print(f)
        update()
        return ""



def update():
    print("s;kdfuheo")
    try:
        for x in range(1, 6):
            for y in range(1, 6):
                xe, ye = cor_to_pos(y - 1, x - 1)
                grid[x][y][0].place(x=xe, y=ye)
    except IndexError:
        return "a"
    except TypeError:
        print("72.5")


def score(type):
    game_state[1]+=0.1

    game_state[3]+= 100*game_state[1]
    game_state[4].config(text=str(round(game_state[3],2)),font=("Arial", "25", "bold"))
    game_state[5].config(text=str(round(game_state[1],2)))
    game_state[4].place(x=1610, y=25)
    root.update()
    time.sleep(0.1)
    game_state[4].config(text=str(round(game_state[3],2)), font=("Arial", "15"))
    game_state[4].place(x=1620,y=35)


def seeder():
    """updates the seed"""
    global seed
    seed = [seed[1], seed[0] + seed[1]]
    return leftMostDigit(seed[1])

def saq(save):
    """saves and quits"""
    if save == "'q'":
        seeds = level
        game_stated = ['NONE', 1.0, [20, 0,game_state[2][2]], 0]
    else:
        seeds = seed
        game_stated = game_state
    tiledeet = []
    for row in grid[1:]:
        for tiles in row[1:]:
            tiledeet.append([tiles[1],tiles[2]])
    text = f"tilled = {tiledeet}\ngame_state = {game_stated[:4]}\nseed = {seeds}\nlevel = {level}\nsaved = {save}\nacc = {acc}"
    with open("vars.txt","w") as va:
        va.write(text)
    if save == "'q'":
        subprocess.run(["python", "match_three.py"])
    quit()

def gridset():
    """creates the grid"""
    global acc,grid,game_state
    grid = [["spawn"]]  # to make impossable to reach

    if saved == "q":
        acc = []

        for up in range(5):
            tmp = [["NONE", "", 99999]]  # to make impossable to reach
            for a in range(5):  # creates a row
                x, y = ((a * 100) + 740, (up * 100) + 400)  # creates the co-ordinates
                colour = colours[int(seeder())]  # gets the colour value for the lable (tile)
                label = Label(root, bg=colour, height=2, width=4, padx=0, pady=0, text=str(a + 5 * up))  # creates the label
                label.bind("<ButtonPress-1>", start_drag)  # Detect mouse press to start dragging
                label.bind("<B1-Motion>", on_drag)  # Move label while dragging
                acc.append([x, y])  # appends co-ordinates to an important spot
                label.place(x=x, y=y)  # puts the tile on the grid where it goes
                tmp.append([label, colour, str(a + 5 * up)])  # appends the label and its friends to the row

            grid.append(tmp)  # puts the row on the rows spot, grid
    else:
        h = 1
        w = 1
        for component in tilled: # ignore red im smarter than the computer
            if w == 1:
                tmp = [["NONE", "", 99999]]  # to make impossable to reach
            label = Label(root, bg=component[0], height=2, width=4, padx=0, pady=0, text="n")  # creates the label
            label.bind("<ButtonPress-1>", start_drag)  # Detect mouse press to start dragging
            label.bind("<B1-Motion>", on_drag)  # Move label while dragging
            x,y = cor_to_pos(w-1,h-1)
            label.place(x=x, y=y)  # puts the tile on the grid where it goes
            tmp.append([label, component[0], "n"])  # appends the label and its friends to the row
            w +=1
            if w == 6:
                grid.append(tmp)
                h += 1
                w = 1
    print(grid)
    scoreback = Label(root, bg="#48F07F", width=20, height=3)
    score = Label(bg="#48F07F",text=round(game_state[3],2))
    multi = Label(bg="#00FF00",text=str(round(game_state[1],2)))
    hands = Label(bg="#FFFFFF", text="Moves:    "+str(game_state[2][0]), font=("Arial", "15"))
    if game_state[2][0]>0:
        Button(root,text="X",command=lambda: saq("'y'")).place(x=1800,y=0)
    game_state.append(score)
    game_state.append(multi)
    game_state.append(hands)
    Label(root,bg="#912321",fg="#F5F355", text="MATCH THR33",font=("Times New Roman", "50")).place(x=730,y=30)
    Label(root, bg="#05670F", text="Required score  "+str(game_state[2][2]),font=("Arial", "15")).place(x=0,y=0)
    multi.place(x=1600,y=90)
    score.place(x=1615,y=30)
    hands.place(x=1600,y=150)
    scoreback.place(x=1600, y=15)

    check()



if __name__ == '__main__':
    """who knows what this does"""
    root = Tk()
    with open("storage" + ".txt", "r") as f:
        trial = f.read()
    print(trial)
    while (not trial[0].lower() == "n" and not trial[0].lower() == "y"):
        trial = input("do you want the instructions and licences?, please enter yes or no") + " "
        print(trial[0].lower()=="n")
    if trial[0].lower() == "n":
        root.title("match thr33")
        root.attributes("-fullscreen", True)
        gridset()
    else:
        if platform.system() == 'Windows':
            os.startfile("hi.txt")
        elif platform.system() == 'Darwin':  # macOS
            os.system(f'open "hi.txt"')
        else:  # Linux and other Unix-like systems
            os.system(f'xdg-open "hi.txt"')
        time.sleep(60)
        root.title("match thr33")
        root.attributes("-fullscreen", True)
        gridset()

    root.mainloop()

from tkinter import *
import random,time
from itertools import chain

chance = random.choice(["Player","Bot"])
count = 0
def assign(cell):
    global chance
    if cell in options:
        options.remove(cell)
        if cell['text'] == "":
            if chance == "Player":
                cell['text'] = "X"
                cell['fg'] = "green"
                cell['bg'] = 'lightgreen'
                chance = "Bot"
                is_win()
                choice = move(options)
                assign(choice)
            else:
                time.sleep(0.05)
                cell['text'] = "O"
                cell['fg'] = 'red'
                cell['bg'] = 'pink'
                chance = "Player"
                is_win()

def win(match_result):
    if match_result == "Player":
        result.config(text="You Won",bg="lightgreen",fg="green")
    elif match_result == "Bot":
        result.config(text="You Lose",bg='pink',fg='red')
    else:
        result.config(text="Draw",fg='brown',bg="lightyellow")
    disable(game_cells)

def is_win():
    global count
    c = game_cells
    count+=1
    for i in range(3):
        if c[i][0]['text'] == c[i][1]['text'] == c[i][2]['text']:
            if c[i][0]['text']=='X':
                return win("Player")
            elif c[i][0]['text']=='O':
                return win("Bot")
        if c[0][i]['text'] == c[1][i]['text'] == c[2][i]['text']:
            if c[0][i]['text']== "X":
                return win("Player")
            elif c[0][i]['text']== "O":
                return win("Bot")
    if c[0][0]['text'] == c[1][1]['text'] == c[2][2]['text']:
        if c[0][0]['text']=='X':
            return win("Player")
        elif c[0][0]['text']=="O":
            return win("Bot")
    if c[0][2]['text'] == c[1][1]['text'] == c[2][0]['text']:
        if c[0][2]['text']=='X':
            return win("Player")
        elif c[0][2]['text']=='O':
            return win("Bot")
    if count == 9:
        return win("Draw")

def move(options):
    if options:
        s = random.choice(options)
        return s
def cells():
    w = 7
    h = 3
    bw = 3
    f = ("Arial",36,"bold")
    col = "#cbcbcb"

    space = Label(root,width=3,bg=col)
    space.grid(row=1,column=0)

    Title = Label(root,text="Tic Tac Toe",font=("Comic Sans MS",27,"bold"),fg="#000000",bg=col)
    Title.grid(row = 0,column=2,pady=25)

    cell1 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell1))
    cell1.grid(row=1,column=1)

    cell2 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell2))
    cell2.grid(row=1,column=2)

    cell3 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell3))
    cell3.grid(row=1,column=3)

    cell4 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell4))
    cell4.grid(row=2,column=1)

    cell5 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell5))
    cell5.grid(row=2,column=2)

    cell6 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell6))
    cell6.grid(row=2,column=3)

    cell7 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell7))
    cell7.grid(row=3,column=1)

    cell8 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell8))
    cell8.grid(row=3,column=2)

    cell9 = Button(root,width=w,borderwidth=bw,relief="solid",height=h,font=f,command= lambda : assign(cell9))
    cell9.grid(row=3,column=3)

    cells = [[cell1,cell2,cell3],[cell4,cell5,cell6],[cell7,cell8,cell9]]
    return cells

def disable(game_cells):
    for i in range(3):
        for j in range(3):
            game_cells[i][j]['state'] = DISABLED

def window():
    col = "#cbcbcb"
    root.title("Tic Tac Toe")
    root.geometry("720x880")
    root.minsize(720,880)
    root.maxsize(720,880)
    root.configure(bg=col)
    icon = PhotoImage(file="tkinter/tic-tac-toe.png")
    root.iconphoto(False,icon)

root = Tk()
window()
game_cells = cells()
options = list(chain.from_iterable(game_cells))
if chance == 'Bot':
    assign(move(options))
result = Label(root,text="",font=("Times New Roman",36,"bold"),fg="Red",borderwidth=4,relief="solid",width=7,height=1)
result.grid(row=4,column=2,pady=30)

root.mainloop()
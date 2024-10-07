from tkinter import Tk, Label, PhotoImage, Button, DISABLED, NORMAL
from tkinter.font import Font
from random import choice

class Tic_Tac_Toe:
    def __init__(self):
        self.root = Tk()
        self.fonts = self.load_fonts()
        self.game_cells, self.result = self.cells()
        self.options = self.shuffle()
        self.chance = choice(["Player", "Bot"])

    def load_fonts(self):
        fonts = {}
        fonts['Times New Roman'] = Font(family="Times New Roman",size=22,weight="bold")
        fonts['Comic Sans MS'] = Font(family="Comic Sans MS",size=22,weight="bold")
        fonts['Arial'] = Font(family="Arial",size=30,weight="bold")
        return fonts

    def window(self):
        col = "#cbcbcb"
        width = 640
        height = 760
        self.root.title("Tic Tac Toe")
        self.root.geometry(f"{width}x{height}")
        self.root.minsize(width,height)
        self.root.maxsize(width,height)
        self.root.configure(bg=col)
        icon = PhotoImage(file="./tic-tac-toe.png")         # Set window icon
        self.root.iconphoto(False, icon)

    def assign(self, cell):
        if cell in self.options:
            self.options.remove(cell)
            if self.chance == "Player":
                cell.config(text="X", fg="green", bg="lightgreen")
                if not self.win(self.is_win(self.game_cells)):
                    # Bot's move using minimax
                    self.chance = "Bot"
                    self.assign(self.move(self.options))
            else:
                cell.config(text="O", fg="red", bg="pink")
                self.chance = "Player"
                self.win(self.is_win(self.game_cells))
                

    def win(self, match_result):
        if match_result is not None:
            if match_result == 10:
                values = ("You Won","green","lightgreen")
            elif match_result == -10:
                values = ("You Lose","red","pink")
            else:
                values = ("Draw","brown","lightyellow")
            self.result.config(text=values[0], fg=values[1], bg=values[2])
            self.disable()
            self.result['state'] = NORMAL
            return True
        return False

    def cells(self):
        col = "#cbcbcb"

        # Space and title
        space = Label(self.root, width=4, bg=col)
        space.grid(row=1, column=0)
        title = Label(self.root, text="Tic Tac Toe", font=self.fonts['Comic Sans MS'],fg="#000000", bg=col)
        title.grid(row=0, column=2, pady=10)

        pos = [[], [], []]
        for i in range(3):
            for j in range(3):
                cell = Button(self.root, width=7, borderwidth=3, relief="solid", height=4, font=self.fonts['Arial'], command=lambda i=i, j=j: self.assign(self.game_cells[i][j]))
                cell.grid(row=i + 1, column=j + 1)
                pos[i].append(cell)
        result = Button(self.root, text="", font =self.fonts['Times New Roman'], state=DISABLED, fg="Red", borderwidth=3,relief="solid",width=7,height=1,command = lambda : self.reset())
        result.grid(row=4,column=2,pady=30)
        return pos,result
    
    def is_win(self, game_cells):
        # Define winning patterns (rows, columns, diagonals)
        winning_patterns = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
            [(0, 2), (1, 1), (2, 0)],  # Diagonal 2
        ]

        # Check for win conditions
        for player in ['X', 'O']:
            for pattern in winning_patterns:
                if all(game_cells[x][y]['text'] == player for x, y in pattern):
                    return 10 if player == 'X' else -10

        # Check if the board is full (a draw)
        if all(game_cells[i][j]['text'] != '' for i in range(3) for j in range(3)):
            return 0

        # No winner yet
        return None


    def shuffle(self):
        arr = [i for i in range(9)]
        options = []
        for i in range(3):
            for j in range(3):
                pos = choice(arr)
                options.insert(pos, self.game_cells[i][j])
                arr.remove(pos)
        return options

    def disable(self):
        for i in range(3):
            for j in range(3):
                self.game_cells[i][j]['state'] = DISABLED

    def reset(self):
        self.game_cells, self.result = self.cells()
        self.options = self.shuffle()
        # self.chance = choice(["Player", "Bot"])
        # if self.chance == "Bot":
        #     self.move(self.options)

    def move(self, options):
        if len(options) == 9:
            return choice(options)
        return self.minimax(self.game_cells,options,-100,100,False)[1]

    def minimax(self, game_cells, options, alpha, beta, maximizingPlayer):
        result = self.is_win(game_cells)
        if result is not None:
            return [result, None]  # Return the result and None for no move

        if maximizingPlayer:
            maxEval = [alpha, None]
            for cell in options:                              
                cell['text'] = 'X'
                new_options = options.copy()
                new_options.remove(cell)
                Eval = self.minimax(game_cells, new_options, alpha, beta, False)
                if Eval[0] > maxEval[0]:
                    maxEval = [Eval[0], cell]
                cell['text'] = ''
                alpha = max(alpha, maxEval[0])
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = [beta, None]
            for cell in options:
                cell['text'] = 'O'
                new_options = options.copy()
                new_options.remove(cell)
                Eval = self.minimax(game_cells, new_options, alpha, beta, True)
                if Eval[0] < minEval[0]:
                    minEval = [Eval[0], cell]
                cell['text'] = ''
                beta = min(beta, minEval[0])
                if beta <= alpha:
                    break
            return minEval


def main():
    game = Tic_Tac_Toe()
    game.window()
    if game.chance == 'Bot':
        game.assign(game.move(game.options))
    game.root.mainloop()

if __name__ == "__main__":
    main()


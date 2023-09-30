
import tkinter as tk
from tkinter import messagebox
from typing import List, Optional


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.player_turn = 'X'

        # Initialize buttons
        self.buttons: List[List[Optional[tk.Button]]] = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, width=10, height=5,
                                               command=lambda row=i, col=j: self.click(row, col),
                                               bg='white', fg='black')
                self.buttons[i][j].grid(row=i, column=j)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=3)

    def click(self, i, j):
        if self.buttons[i][j]["text"] == "":
            self.buttons[i][j]["text"] = self.player_turn
            if self.player_turn == 'X':
                self.buttons[i][j]["fg"] = 'red'
            else:
                self.buttons[i][j]["fg"] = 'blue'
            self.buttons[i][j]["state"] = 'disabled'
            if self.check_winner(self.player_turn):
                messagebox.showinfo("Game Over", "{} Wins!".format(self.player_turn))
                self.reset_game()
                return
            elif self.player_turn == 'X':
                self.player_turn = 'O'
            else:
                self.player_turn = 'X'

    def check_winner(self, player):
        for i in range(3):
            row_win = all(self.buttons[i][j]['text'] == player for j in range(3))
            col_win = all(self.buttons[j][i]['text'] == player for j in range(3))
            if row_win or col_win:
                return True

        diagonal1_win = all(self.buttons[i][i]['text'] == player for i in range(3))
        diagonal2_win = all(self.buttons[i][2 - i]['text'] == player for i in range(3))

        if diagonal1_win or diagonal2_win:
            return True

        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["state"] = "normal"
                self.buttons[i][j]["fg"] = "black"
        self.player_turn = 'X'

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()

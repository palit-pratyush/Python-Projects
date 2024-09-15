import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticky Tacky Toey") 
        self.player1_name = ""
        self.player2_name = ""
        self.player1_symbol = ""
        self.player2_symbol = ""
        self.current_player = 1  
        self.player1_score = 0
        self.player2_score = 0
        self.tie_score = 0
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.final_match_button = tk.Button(root, text="Final Match", command=self.final_match)   
        self.reset_button.grid(row=0, column=0, padx=10, pady=10)
        self.final_match_button.grid(row=0, column=1, padx=10, pady=10) 
        self.setup_players()
        self.create_board()
    def setup_players(self):
        player1_frame = tk.Frame(root)
        player1_frame.grid(row=1, column=0, padx=10, pady=10)
        tk.Label(player1_frame, text="Player 1 Name:").pack()
        self.player1_name_entry = tk.Entry(player1_frame)
        self.player1_name_entry.pack()
        tk.Label(player1_frame, text="Player 1 Symbol (X/O):").pack()
        self.player1_symbol_entry = tk.Entry(player1_frame)
        self.player1_symbol_entry.pack()
        player2_frame = tk.Frame(root)
        player2_frame.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(player2_frame, text="Player 2 Name:").pack()
        self.player2_name_entry = tk.Entry(player2_frame)
        self.player2_name_entry.pack()
        tk.Label(player2_frame, text="Player 2 Symbol (X/O):").pack()
        self.player2_symbol_entry = tk.Entry(player2_frame)
        self.player2_symbol_entry.pack()
        tk.Button(root, text="Start Game", command=self.start_game).grid(row=2, column=0, columnspan=2, padx=10,pady=10)
    def create_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(root, text="", width=10, height=3,
                                                    command=lambda r=row, c=col: self.make_move(r, c))
                self.buttons[row][col].grid(row=row+3, column=col, padx=5, pady=5)
    def start_game(self):
        self.player1_name = self.player1_name_entry.get()
        self.player2_name = self.player2_name_entry.get()
        self.player1_symbol = self.player1_symbol_entry.get().upper()
        self.player2_symbol = self.player2_symbol_entry.get().upper()
        if(self.player1_symbol==self.player2_symbol):
            messagebox.showinfo("HOW DARE YOU!!!","Same Symbols:(")
            self.reset_game()
        self.reset_game()
    def make_move(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            if self.current_player == 1:
                self.buttons[row][col]["text"] = self.player1_symbol
                self.current_player = 2
            else:
                self.buttons[row][col]["text"] = self.player2_symbol
                self.current_player = 1
            if self.check_winner():
                winner = self.player1_name if self.current_player == 2 else self.player2_name
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.update_scores(winner)
            elif all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.update_scores("Tie")
    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.current_player = 1
    def final_match(self):
        if self.player1_score > self.player2_score:
            winner = self.player1_name
        elif self.player2_score > self.player1_score:
            winner = self.player2_name
        else:
            winner = "It's a tie!"
        messagebox.showinfo("Final Match Result", f"The winner of the final match is: {winner}")
        self.reset_scores()
    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] != "":
                return True
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False
    def update_scores(self, winner):
        if winner == self.player1_name:
            self.player1_score += 1
        elif winner == self.player2_name:
            self.player2_score += 1
        else:
            self.tie_score += 1
        self.reset_game()
        self.show_scores()
    def reset_scores(self):
        self.player1_score = 0
        self.player2_score = 0
        self.tie_score = 0
        self.reset_game()
        self.show_scores()
    def show_scores(self):
        score_text = f"Scores:\n{self.player1_name} ({self.player1_symbol}): {self.player1_score}\n" \
                     f"{self.player2_name} ({self.player2_symbol}): {self.player2_score}\n" \
                     f"Ties: {self.tie_score}"
        messagebox.showinfo("Scores", score_text)
if __name__ == "__main__":
    root = tk.Tk()
    ttt = TicTacToe(root)
    root.mainloop()

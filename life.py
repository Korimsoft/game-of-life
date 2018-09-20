#!/usr/bin/env python3

import tkinter as tk
from views import cell_matrix_view as cmv, control_panel as cp
from logic import board
#from logic import game-controller

#Main application
class Application(tk.Frame):
    def __init__(self, board, master=None):
        tk.Frame.__init__(self, master)
        self.grid()                    
        self.board = board
        self.__create_widgets()

    def __create_widgets(self):
        self.control_panel = cp.ControlPanel(self.board, self.master)
        self.control_panel.grid()
        self.game_view = cmv.CellMatrixView(self.board, 15, self.master)
        self.game_view.grid()
    
# Create the application instance and run
if __name__ == "__main__" :
    game = board.Board(31,40)

    root = tk.Tk()
    app = Application(game, root)
    ## board_view = BoardView(app, game , 20)
    ## board_view.display_board()
    app.mainloop()


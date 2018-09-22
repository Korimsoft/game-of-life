#! /usr/bin/env python3

import tkinter as tk

#
class CellMatrixView(tk.Canvas):
    def __init__(self, board, cell_size=10, master = None):
        self.cell_size = cell_size
        self.width = board.width*cell_size
        self.height = board.height*cell_size
        tk.Canvas.__init__(self, master, width=self.width, height=self.height, bg="white")
        self.board = board
        self.bind("<Button-1>", self.clicked)
        self.board.board_changed_event.append(self.board_changed)
        self.__display_board()

    def __display_cell(self, i, j, state):
        x0 = j*self.cell_size
        y0 = i*self.cell_size
                        
        x1 = x0 + self.cell_size
        y1 = y0 + self.cell_size
             
        self.create_oval(x0, y0, x1, y1, fill=("#fd2b86" if state==1 else "white"), outline="#83a260")

    def __display_board(self):
        self.delete("all")
        for i in range(self.board.height):
            for j in range(self.board.width):
                self.__display_cell(i, j, self.board.current_gen_cells[i, j])

    
    # Callback called on board change
    def board_changed(self, board):
        self.__display_board()

    #Callback on click
    def clicked(self, event):
        i = event.y // self.cell_size
        j = event.x // self.cell_size
        state = 1 if self.board.current_gen_cells[i, j] == 0 else 0
        self.board.set_cell_state(i, j, state)

#! /usr/bin/env python3
import tkinter as tk
from logic import board

class ControlPanel(tk.Frame):
    
    def __init__(self, board, master = None):
        tk.Frame.__init__(self, master)
        self.board = board
        self.__create_widgets()
        
    def __create_widgets(self):
        self.start_stop_button = tk.Button(self, text="Start", command=self.__start_simulation)
        self.start_stop_button.grid(row = 0, column = 0)
        self.clear_button = tk.Button(self, text="Clear", command = self.__clear)
        self.clear_button.grid(row = 0, column = 1)
                
    def __start_simulation(self):
        self.continue_running = True
        self.start_stop_button = tk.Button(self, text = "Stop", command = self.__stop_simulation)
        self.start_stop_button.grid(row=0, column=0)
        self.__simulation_step()

    def __stop_simulation(self):
        self.continue_running = False
        self.start_stop_button = tk.Button(self, text="Start", command=self.__start_simulation)
        self.start_stop_button.grid(row=0, column=0)

    def __simulation_step(self):
        if self.continue_running:
            self.board.evolve()
            self.after(100, self.__simulation_step)

    def __clear(self):
        self.__stop_simulation()
        self.board.clear()
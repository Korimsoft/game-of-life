#!/usr/bin/env python3

import numpy

# Game of life - logic (game board)
class Board:

    # Class constructor
    def __init__(self, width, height):
        self.current_gen_cells = numpy.zeros((height, width))
        self.next_gen_cells = numpy.zeros((height, width))
        self.width = width
        self.height = height
        self.board_changed_event = []

    # Activate a cell
    # Use for creating an initial state
    def set_cell_state(self, i, j, state):
        self.current_gen_cells[i][j] = state
        self.__on_board_changed()
    
    # Check the cell according to the rules
    #1. Any live cell with fewer than two live neighbors dies, as if by under population.
    #2. Any live cell with two or three live neighbors lives on to the next generation.
    #3. Any live cell with more than three live neighbors dies, as if by overpopulation.
    #4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    def __calculate_next_gen_cell(self, i, j):
        count = self.__count_alive_neighbours(self.current_gen_cells, i, j)
        cell = self.current_gen_cells[i,j]
        if (cell == 1 and (count == 2 or count == 3)):
            self.next_gen_cells[i,j] = 1
        elif (cell == 0 and count == 3):
            self.next_gen_cells[i,j] = 1

    def __count_alive_neighbours(self, cells, i, j):
        current = cells[i,j]
        # This is a hack, so that a current cell is not counted in neighbors if it is alive
        cells[i, j] = 2
        subarray = cells[max(i-1, 0):min(i+2,self.height),max(j-1, 0):min(j+2,self.width)]
        flattened = numpy.ndenumerate(subarray)
        alive_neighbours = [cell for cell in flattened if cell[1] == 1]
        cells[i,j] = current
        return len(alive_neighbours)

    # Calculate a next generation of the board
    def evolve(self):
        for i in range(self.height):
            for j in range(self.width):
                self.__calculate_next_gen_cell(i, j)
        self.current_gen_cells = self.next_gen_cells
        self.next_gen_cells = numpy.zeros((self.height, self.width))
        self.__on_board_changed()

    def clear(self):
        self.current_gen_cells = numpy.zeros((self.height, self.width))
        self.next_gen_cells = numpy.zeros((self.height, self.width))
        self.__on_board_changed()

    # Notify the listeners that board has changed
    def __on_board_changed(self):
        for callback in self.board_changed_event:
            callback(self)

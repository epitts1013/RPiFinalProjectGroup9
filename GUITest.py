'''
Names: Connor Waits, Jonas Kety, Eric Pitts
Date: 4/30/18
Description: Implementation of GUI into Sudoku Generator
'''

###IMPORTS###
from Tkinter import *
from random import randint

###CLASSES###
# creates GUI window
class App(Frame):
    # constructor takes two arguments: the window and the board with removed elements
    def __init__(self, master, puzzle):
        Frame.__init__(self, master)
        # buttons placed in 9x9 grid
        # rows represented by A-I
        # columns represented by 1-9
        # naming convention is button{row}{col}
        # buttons named based on grid position
        # row A
        self.buttonA1 = Button(master, text="A1", height=3, width=6)
        self.buttonA1.grid(row=0, column=0, sticky=N+E+S+W)
        self.buttonA2 = Button(master, text="A2", height=3, width=6)
        self.buttonA2.grid(row=0, column=1, sticky=N+E+S+W)
        self.buttonA3 = Button(master, text="A3", height=3, width=6)
        self.buttonA3.grid(row=0, column=2, sticky=N+E+S+W)
        self.buttonA4 = Button(master, text="A4", height=3, width=6)
        self.buttonA4.grid(row=0, column=3, sticky=N+E+S+W)
        self.buttonA5 = Button(master, text="A5", height=3, width=6)
        self.buttonA5.grid(row=0, column=4,sticky=N+E+S+W)
        self.buttonA6 = Button(master, text="A6", height=3, width=6)
        self.buttonA6.grid(row=0, column=5, sticky=N+E+S+W)
        self.buttonA7 = Button(master, text="A7", height=3, width=6)
        self.buttonA7.grid(row=0, column=6, sticky=N+E+S+W)
        self.buttonA8 = Button(master, text="A8", height=3, width=6)
        self.buttonA8.grid(row=0, column=7, sticky=N+E+S+W)
        self.buttonA9 = Button(master, text="A9", height=3, width=6)
        self.buttonA9.grid(row=0, column=8, sticky=N+E+S+W)

        # row B
        self.buttonB1 = Button(master, text="B1", height=3, width=6)
        self.buttonB1.grid(row=1, column=0, sticky=N+E+S+W)
        self.buttonB2 = Button(master, text="B2", height=3, width=6)
        self.buttonB2.grid(row=1, column=1, sticky=N+E+S+W)
        self.buttonB3 = Button(master, text="B3", height=3, width=6)
        self.buttonB3.grid(row=1, column=2, sticky=N+E+S+W)
        self.buttonB4 = Button(master, text="B4", height=3, width=6)
        self.buttonB4.grid(row=1, column=3, sticky=N+E+S+W)
        self.buttonB5 = Button(master, text="B5", height=3, width=6)
        self.buttonB5.grid(row=1, column=4, sticky=N+E+S+W)
        self.buttonB6 = Button(master, text="B6", height=3, width=6)
        self.buttonB6.grid(row=1, column=5, sticky=N+E+S+W)
        self.buttonB7 = Button(master, text="B7", height=3, width=6)
        self.buttonB7.grid(row=1, column=6, sticky=N+E+S+W)
        self.buttonB8 = Button(master, text="B8", height=3, width=6)
        self.buttonB8.grid(row=1, column=7, sticky=N+E+S+W)
        self.buttonB9 = Button(master, text="B9", height=3, width=6)
        self.buttonB9.grid(row=1, column=8, sticky=N+E+S+W)

        # row C
        self.buttonC1 = Button(master, text="C1", height=3, width=6)
        self.buttonC1.grid(row=2, column=0, sticky=N+E+S+W)
        self.buttonC2 = Button(master, text="C2", height=3, width=6)
        self.buttonC2.grid(row=2, column=1, sticky=N+E+S+W)
        self.buttonC3 = Button(master, text="C3", height=3, width=6)
        self.buttonC3.grid(row=2, column=2, sticky=N+E+S+W)
        self.buttonC4 = Button(master, text="C4", height=3, width=6)
        self.buttonC4.grid(row=2, column=3, sticky=N+E+S+W)
        self.buttonC5 = Button(master, text="C5", height=3, width=6)
        self.buttonC5.grid(row=2, column=4, sticky=N+E+S+W)
        self.buttonC6 = Button(master, text="C6", height=3, width=6)
        self.buttonC6.grid(row=2, column=5, sticky=N+E+S+W)
        self.buttonC7 = Button(master, text="C7", height=3, width=6)
        self.buttonC7.grid(row=2, column=6, sticky=N+E+S+W)
        self.buttonC8 = Button(master, text="C8", height=3, width=6)
        self.buttonC8.grid(row=2, column=7, sticky=N+E+S+W)
        self.buttonC9 = Button(master, text="C9", height=3, width=6)
        self.buttonC9.grid(row=2, column=8, sticky=N+E+S+W)

        # row D
        self.buttonD1 = Button(master, text="D1", height=3, width=6)
        self.buttonD1.grid(row=3, column=0, sticky=N+E+S+W)
        self.buttonD2 = Button(master, text="D2", height=3, width=6)
        self.buttonD2.grid(row=3, column=1, sticky=N+E+S+W)
        self.buttonD3 = Button(master, text="D3", height=3, width=6)
        self.buttonD3.grid(row=3, column=2, sticky=N+E+S+W)
        self.buttonD4 = Button(master, text="D4", height=3, width=6)
        self.buttonD4.grid(row=3, column=3, sticky=N+E+S+W)
        self.buttonD5 = Button(master, text="D5", height=3, width=6)
        self.buttonD5.grid(row=3, column=4, sticky=N+E+S+W)
        self.buttonD6 = Button(master, text="D6", height=3, width=6)
        self.buttonD6.grid(row=3, column=5, sticky=N+E+S+W)
        self.buttonD7 = Button(master, text="D7", height=3, width=6)
        self.buttonD7.grid(row=3, column=6, sticky=N+E+S+W)
        self.buttonD8 = Button(master, text="D8", height=3, width=6)
        self.buttonD8.grid(row=3, column=7, sticky=N+E+S+W)
        self.buttonD9 = Button(master, text="D9", height=3, width=6)
        self.buttonD9.grid(row=3, column=8, sticky=N+E+S+W)

        # row E
        self.buttonE1 = Button(master, text="E1", height=3, width=6)
        self.buttonE1.grid(row=4, column=0, sticky=N+E+S+W)
        self.buttonE2 = Button(master, text="E2", height=3, width=6)
        self.buttonE2.grid(row=4, column=1, sticky=N+E+S+W)
        self.buttonE3 = Button(master, text="E3", height=3, width=6)
        self.buttonE3.grid(row=4, column=2, sticky=N+E+S+W)
        self.buttonE4 = Button(master, text="E4", height=3, width=6)
        self.buttonE4.grid(row=4, column=3, sticky=N+E+S+W)
        self.buttonE5 = Button(master, text="E5", height=3, width=6)
        self.buttonE5.grid(row=4, column=4, sticky=N+E+S+W)
        self.buttonE6 = Button(master, text="E6", height=3, width=6)
        self.buttonE6.grid(row=4, column=5, sticky=N+E+S+W)
        self.buttonE7 = Button(master, text="E7", height=3, width=6)
        self.buttonE7.grid(row=4, column=6, sticky=N+E+S+W)
        self.buttonE8 = Button(master, text="E8", height=3, width=6)
        self.buttonE8.grid(row=4, column=7, sticky=N+E+S+W)
        self.buttonE9 = Button(master, text="E9", height=3, width=6)
        self.buttonE9.grid(row=4, column=8, sticky=N+E+S+W)

        # row F
        self.buttonF1 = Button(master, text="F1", height=3, width=6)
        self.buttonF1.grid(row=5, column=0, sticky=N+E+S+W)
        self.buttonF2 = Button(master, text="F2", height=3, width=6)
        self.buttonF2.grid(row=5, column=1, sticky=N+E+S+W)
        self.buttonF3 = Button(master, text="F3", height=3, width=6)
        self.buttonF3.grid(row=5, column=2, sticky=N+E+S+W)
        self.buttonF4 = Button(master, text="F4", height=3, width=6)
        self.buttonF4.grid(row=5, column=3, sticky=N+E+S+W)
        self.buttonF5 = Button(master, text="F5", height=3, width=6)
        self.buttonF5.grid(row=5, column=4, sticky=N+E+S+W)
        self.buttonF6 = Button(master, text="F6", height=3, width=6)
        self.buttonF6.grid(row=5, column=5, sticky=N+E+S+W)
        self.buttonF7 = Button(master, text="F7", height=3, width=6)
        self.buttonF7.grid(row=5, column=6, sticky=N+E+S+W)
        self.buttonF8 = Button(master, text="F8", height=3, width=6)
        self.buttonF8.grid(row=5, column=7, sticky=N+E+S+W)
        self.buttonF9 = Button(master, text="F9", height=3, width=6)
        self.buttonF9.grid(row=5, column=8, sticky=N+E+S+W)

        # row G
        self.buttonG1 = Button(master, text="G1", height=3, width=6)
        self.buttonG1.grid(row=6, column=0, sticky=N+E+S+W)
        self.buttonG2 = Button(master, text="G2", height=3, width=6)
        self.buttonG2.grid(row=6, column=1, sticky=N+E+S+W)
        self.buttonG3 = Button(master, text="G3", height=3, width=6)
        self.buttonG3.grid(row=6, column=2, sticky=N+E+S+W)
        self.buttonG4 = Button(master, text="G4", height=3, width=6)
        self.buttonG4.grid(row=6, column=3, sticky=N+E+S+W)
        self.buttonG5 = Button(master, text="G5", height=3, width=6)
        self.buttonG5.grid(row=6, column=4, sticky=N+E+S+W)
        self.buttonG6 = Button(master, text="G6", height=3, width=6)
        self.buttonG6.grid(row=6, column=5, sticky=N+E+S+W)
        self.buttonG7 = Button(master, text="G7", height=3, width=6)
        self.buttonG7.grid(row=6, column=6, sticky=N+E+S+W)
        self.buttonG8 = Button(master, text="G8", height=3, width=6)
        self.buttonG8.grid(row=6, column=7, sticky=N+E+S+W)
        self.buttonG9 = Button(master, text="G9", height=3, width=6)
        self.buttonG9.grid(row=6, column=8, sticky=N+E+S+W)

        # row H
        self.buttonH1 = Button(master, text="H1", height=3, width=6)
        self.buttonH1.grid(row=7, column=0, sticky=N+E+S+W)
        self.buttonH2 = Button(master, text="H2", height=3, width=6)
        self.buttonH2.grid(row=7, column=1, sticky=N+E+S+W)
        self.buttonH3 = Button(master, text="H3", height=3, width=6)
        self.buttonH3.grid(row=7, column=2, sticky=N+E+S+W)
        self.buttonH4 = Button(master, text="H4", height=3, width=6)
        self.buttonH4.grid(row=7, column=3, sticky=N+E+S+W)
        self.buttonH5 = Button(master, text="H5", height=3, width=6)
        self.buttonH5.grid(row=7, column=4, sticky=N+E+S+W)
        self.buttonH6 = Button(master, text="H6", height=3, width=6)
        self.buttonH6.grid(row=7, column=5, sticky=N+E+S+W)
        self.buttonH7 = Button(master, text="H7", height=3, width=6)
        self.buttonH7.grid(row=7, column=6, sticky=N+E+S+W)
        self.buttonH8 = Button(master, text="H8", height=3, width=6)
        self.buttonH8.grid(row=7, column=7, sticky=N+E+S+W)
        self.buttonH9 = Button(master, text="H9", height=3, width=6)
        self.buttonH9.grid(row=7, column=8, sticky=N+E+S+W)

        # row I
        self.buttonI1 = Button(master, text="I1", height=3, width=6)
        self.buttonI1.grid(row=8, column=0, sticky=N+E+S+W)
        self.buttonI2 = Button(master, text="I2", height=3, width=6)
        self.buttonI2.grid(row=8, column=1, sticky=N+E+S+W)
        self.buttonI3 = Button(master, text="I3", height=3, width=6)
        self.buttonI3.grid(row=8, column=2, sticky=N+E+S+W)
        self.buttonI4 = Button(master, text="I4", height=3, width=6)
        self.buttonI4.grid(row=8, column=3, sticky=N+E+S+W)
        self.buttonI5 = Button(master, text="I5", height=3, width=6)
        self.buttonI5.grid(row=8, column=4, sticky=N+E+S+W)
        self.buttonI6 = Button(master, text="I6", height=3, width=6)
        self.buttonI6.grid(row=8, column=5, sticky=N+E+S+W)
        self.buttonI7 = Button(master, text="I7", height=3, width=6)
        self.buttonI7.grid(row=8, column=6, sticky=N+E+S+W)
        self.buttonI8 = Button(master, text="I8", height=3, width=6)
        self.buttonI8.grid(row=8, column=7, sticky=N+E+S+W)
        self.buttonI9 = Button(master, text="I9", height=3, width=6)
        self.buttonI9.grid(row=8, column=8, sticky=N+E+S+W)

###FUNCTIONS###
def generateDebugPuzzle():
    puzzle = []
    for row in range(9):
        puzzle.append([])
        for col in range(9):
            puzzle[row].append(randint(1,9))

    return puzzle

###MAIN###
global DEBUG
DEBUG = False

if DEBUG == True:
    puzzle = generateDebugPuzzle

window = Tk()
app = App(window, puzzle)
window.mainloop()

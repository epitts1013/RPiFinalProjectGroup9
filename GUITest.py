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
        # buttons labelled 0-80
        # row 0 (buttons 0-8)
        self.button0 = Button(master, text="0", height=3, width=6)
        self.button0.grid(row=0, column=0, sticky=N+E+S+W)
        self.button1 = Button(master, text="1", height=3, width=6)
        self.button1.grid(row=0, column=1, sticky=N+E+S+W)
        self.button2 = Button(master, text="2", height=3, width=6)
        self.button2.grid(row=0, column=2, sticky=N+E+S+W)
        self.button3 = Button(master, text="3", height=3, width=6)
        self.button3.grid(row=0, column=3, sticky=N+E+S+W)
        self.button4 = Button(master, text="4", height=3, width=6)
        self.button4.grid(row=0, column=4,sticky=N+E+S+W)
        self.button5 = Button(master, text="5", height=3, width=6)
        self.button5.grid(row=0, column=5, sticky=N+E+S+W)
        self.button6 = Button(master, text="6", height=3, width=6)
        self.button6.grid(row=0, column=6, sticky=N+E+S+W)
        self.button7 = Button(master, text="7", height=3, width=6)
        self.button7.grid(row=0, column=7, sticky=N+E+S+W)
        self.button8 = Button(master, text="8", height=3, width=6)
        self.button8.grid(row=0, column=8, sticky=N+E+S+W)

        # row 1 (buttons 9-17)
        self.button9 = Button(master, text="9", height=3, width=6)
        self.button9.grid(row=1, column=0, sticky=N+E+S+W)
        self.button10 = Button(master, text="10", height=3, width=6)
        self.button10.grid(row=1, column=1, sticky=N+E+S+W)
        self.button11 = Button(master, text="11", height=3, width=6)
        self.button11.grid(row=1, column=2, sticky=N+E+S+W)
        self.button12 = Button(master, text="12", height=3, width=6)
        self.button12.grid(row=1, column=3, sticky=N+E+S+W)
        self.button13 = Button(master, text="13", height=3, width=6)
        self.button13.grid(row=1, column=4, sticky=N+E+S+W)
        self.button14 = Button(master, text="14", height=3, width=6)
        self.button14.grid(row=1, column=5, sticky=N+E+S+W)
        self.button15 = Button(master, text="15", height=3, width=6)
        self.button15.grid(row=1, column=6, sticky=N+E+S+W)
        self.button16 = Button(master, text="16", height=3, width=6)
        self.button16.grid(row=1, column=7, sticky=N+E+S+W)
        self.button17 = Button(master, text="17", height=3, width=6)
        self.button17.grid(row=1, column=8, sticky=N+E+S+W)

        # row 2 (buttons 18-26)
        self.button18 = Button(master, text="18", height=3, width=6)
        self.button18.grid(row=2, column=0, sticky=N+E+S+W)
        self.button19 = Button(master, text="19", height=3, width=6)
        self.button19.grid(row=2, column=1, sticky=N+E+S+W)
        self.button20 = Button(master, text="20", height=3, width=6)
        self.button20.grid(row=2, column=2, sticky=N+E+S+W)
        self.button21 = Button(master, text="21", height=3, width=6)
        self.button21.grid(row=2, column=3, sticky=N+E+S+W)
        self.button22 = Button(master, text="22", height=3, width=6)
        self.button22.grid(row=2, column=4, sticky=N+E+S+W)
        self.button23 = Button(master, text="23", height=3, width=6)
        self.button23.grid(row=2, column=5, sticky=N+E+S+W)
        self.button24 = Button(master, text="24", height=3, width=6)
        self.button24.grid(row=2, column=6, sticky=N+E+S+W)
        self.button25 = Button(master, text="25", height=3, width=6)
        self.button25.grid(row=2, column=7, sticky=N+E+S+W)
        self.button26 = Button(master, text="26", height=3, width=6)
        self.button26.grid(row=2, column=8, sticky=N+E+S+W)

        # row 3 (buttons 27-35)
        self.button27 = Button(master, text="27", height=3, width=6)
        self.button27.grid(row=3, column=0, sticky=N+E+S+W)
        self.button28 = Button(master, text="28", height=3, width=6)
        self.button28.grid(row=3, column=1, sticky=N+E+S+W)
        self.button29 = Button(master, text="29", height=3, width=6)
        self.button29.grid(row=3, column=2, sticky=N+E+S+W)
        self.button30 = Button(master, text="30", height=3, width=6)
        self.button30.grid(row=3, column=3, sticky=N+E+S+W)
        self.button31 = Button(master, text="31", height=3, width=6)
        self.button31.grid(row=3, column=4, sticky=N+E+S+W)
        self.button32 = Button(master, text="32", height=3, width=6)
        self.button32.grid(row=3, column=5, sticky=N+E+S+W)
        self.button33 = Button(master, text="33", height=3, width=6)
        self.button33.grid(row=3, column=6, sticky=N+E+S+W)
        self.button34 = Button(master, text="34", height=3, width=6)
        self.button34.grid(row=3, column=7, sticky=N+E+S+W)
        self.button35 = Button(master, text="35", height=3, width=6)
        self.button35.grid(row=3, column=8, sticky=N+E+S+W)

        # row 4 (buttons 36-44)
        self.button36 = Button(master, text="36", height=3, width=6)
        self.button36.grid(row=4, column=0, sticky=N+E+S+W)
        self.button37 = Button(master, text="37", height=3, width=6)
        self.button37.grid(row=4, column=1, sticky=N+E+S+W)
        self.button38 = Button(master, text="38", height=3, width=6)
        self.button38.grid(row=4, column=2, sticky=N+E+S+W)
        self.button39 = Button(master, text="39", height=3, width=6)
        self.button39.grid(row=4, column=3, sticky=N+E+S+W)
        self.button40 = Button(master, text="40", height=3, width=6)
        self.button40.grid(row=4, column=4, sticky=N+E+S+W)
        self.button41 = Button(master, text="41", height=3, width=6)
        self.button41.grid(row=4, column=5, sticky=N+E+S+W)
        self.button42 = Button(master, text="42", height=3, width=6)
        self.button42.grid(row=4, column=6, sticky=N+E+S+W)
        self.button43 = Button(master, text="43", height=3, width=6)
        self.button43.grid(row=4, column=7, sticky=N+E+S+W)
        self.button44 = Button(master, text="44", height=3, width=6)
        self.button44.grid(row=4, column=8, sticky=N+E+S+W)

        # row 5 (buttons 45-53)
        self.button45 = Button(master, text="45", height=3, width=6)
        self.button45.grid(row=5, column=0, sticky=N+E+S+W)
        self.button46 = Button(master, text="46", height=3, width=6)
        self.button46.grid(row=5, column=1, sticky=N+E+S+W)
        self.button47 = Button(master, text="47", height=3, width=6)
        self.button47.grid(row=5, column=2, sticky=N+E+S+W)
        self.button48 = Button(master, text="48", height=3, width=6)
        self.button48.grid(row=5, column=3, sticky=N+E+S+W)
        self.button49 = Button(master, text="49", height=3, width=6)
        self.button49.grid(row=5, column=4, sticky=N+E+S+W)
        self.button50 = Button(master, text="50", height=3, width=6)
        self.button50.grid(row=5, column=5, sticky=N+E+S+W)
        self.button51 = Button(master, text="51", height=3, width=6)
        self.button51.grid(row=5, column=6, sticky=N+E+S+W)
        self.button52 = Button(master, text="52", height=3, width=6)
        self.button52.grid(row=5, column=7, sticky=N+E+S+W)
        self.button53 = Button(master, text="53", height=3, width=6)
        self.button53.grid(row=5, column=8, sticky=N+E+S+W)

        # row 6 (buttons 54-62)
        self.button54 = Button(master, text="54", height=3, width=6)
        self.button54.grid(row=6, column=0, sticky=N+E+S+W)
        self.button55 = Button(master, text="55", height=3, width=6)
        self.button55.grid(row=6, column=1, sticky=N+E+S+W)
        self.button56 = Button(master, text="56", height=3, width=6)
        self.button56.grid(row=6, column=2, sticky=N+E+S+W)
        self.button57 = Button(master, text="57", height=3, width=6)
        self.button57.grid(row=6, column=3, sticky=N+E+S+W)
        self.button58 = Button(master, text="58", height=3, width=6)
        self.button58.grid(row=6, column=4, sticky=N+E+S+W)
        self.button59 = Button(master, text="59", height=3, width=6)
        self.button59.grid(row=6, column=5, sticky=N+E+S+W)
        self.button60 = Button(master, text="60", height=3, width=6)
        self.button60.grid(row=6, column=6, sticky=N+E+S+W)
        self.button61 = Button(master, text="61", height=3, width=6)
        self.button61.grid(row=6, column=7, sticky=N+E+S+W)
        self.button62 = Button(master, text="62", height=3, width=6)
        self.button62.grid(row=6, column=8, sticky=N+E+S+W)

        # row 7 (buttons 63-71)
        self.button63 = Button(master, text="63", height=3, width=6)
        self.button63.grid(row=7, column=0, sticky=N+E+S+W)
        self.button64 = Button(master, text="64", height=3, width=6)
        self.button64.grid(row=7, column=1, sticky=N+E+S+W)
        self.button65 = Button(master, text="65", height=3, width=6)
        self.button65.grid(row=7, column=2, sticky=N+E+S+W)
        self.button66 = Button(master, text="66", height=3, width=6)
        self.button66.grid(row=7, column=3, sticky=N+E+S+W)
        self.button67 = Button(master, text="67", height=3, width=6)
        self.button67.grid(row=7, column=4, sticky=N+E+S+W)
        self.button68 = Button(master, text="68", height=3, width=6)
        self.button68.grid(row=7, column=5, sticky=N+E+S+W)
        self.button69 = Button(master, text="69", height=3, width=6)
        self.button69.grid(row=7, column=6, sticky=N+E+S+W)
        self.button70 = Button(master, text="70", height=3, width=6)
        self.button70.grid(row=7, column=7, sticky=N+E+S+W)
        self.button71 = Button(master, text="71", height=3, width=6)
        self.button71.grid(row=7, column=8, sticky=N+E+S+W)

        # row 8 (buttons 72-80)
        self.button72 = Button(master, text="72", height=3, width=6)
        self.button72.grid(row=8, column=0, sticky=N+E+S+W)
        self.button73 = Button(master, text="73", height=3, width=6)
        self.button73.grid(row=8, column=1, sticky=N+E+S+W)
        self.button74 = Button(master, text="74", height=3, width=6)
        self.button74.grid(row=8, column=2, sticky=N+E+S+W)
        self.button75 = Button(master, text="75", height=3, width=6)
        self.button75.grid(row=8, column=3, sticky=N+E+S+W)
        self.button76 = Button(master, text="76", height=3, width=6)
        self.button76.grid(row=8, column=4, sticky=N+E+S+W)
        self.button77 = Button(master, text="77", height=3, width=6)
        self.button77.grid(row=8, column=5, sticky=N+E+S+W)
        self.button78 = Button(master, text="78", height=3, width=6)
        self.button78.grid(row=8, column=6, sticky=N+E+S+W)
        self.button79 = Button(master, text="79", height=3, width=6)
        self.button79.grid(row=8, column=7, sticky=N+E+S+W)
        self.button80 = Button(master, text="80", height=3, width=6)
        self.button80.grid(row=8, column=8, sticky=N+E+S+W)

        def processPuzzle(pButton):
            pass

        def processNumpad(nButton):
            pass

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
puzzle = []

if DEBUG == True:
    puzzle = generateDebugPuzzle

window = Tk()
app = App(window, puzzle)
window.mainloop()

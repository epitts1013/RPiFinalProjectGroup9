'''
Names: Connor Waits, Jonas Kety, Eric Pitts
Date: 4/30/18
Description: Implementation of GUI into Sudoku Generator
'''

###IMPORTS###
from Tkinter import *
from random import randint

###CLASSES###
# creates GUI window for the start menu interface
class SudokuMenu(Frame):
    #constructor takes one argument: the window
    def __init__(self, master):
        Frame.__init__(self, master)
        # difficulty variable, set to easy by default
<<<<<<< HEAD
        self.difficulty = "Easy"
=======
        self.difficulty = "easy"
>>>>>>> 9a8b916987d5854a0a42d7fd4b95747204e8d2e6
        # labels for title and instructions
        self.labelTitle = Label(master, text="SUDOKU", font=("TkDefaultFont",28))
        self.labelTitle.grid(row=0, column=0, padx=20, pady=(20,0))
        self.labelDir = Label(master, text="How To Play:\nClick on a box to select it,\
 then\nclick on one of the numpad\nnumbers on the right to place\nthat number in the selected\
 box.", font=("TkDefaultFont",16))
        self.labelDir.grid(row=1, column=0, pady=(0,20), padx=20, rowspan=3)
        # buttons for difficulty and quit
        self.buttonEasy = Button(master, text="Easy", font=("TkDefaultFont",12), height=2, width=18, command=lambda: self.process(self.buttonEasy))
        self.buttonEasy.grid(row=0, column=1, pady=(20,0), padx=(0,20))
        self.buttonMedium = Button(master, text="Medium", font=("TkDefaultFont",12), height=2, width=18, command=lambda: self.process(self.buttonMedium))
        self.buttonMedium.grid(row=1, column=1, padx=(0,20))
        self.buttonHard = Button(master, text="Hard", font=("TkDefaultFont",12), height=2, width=18, command=lambda: self.process(self.buttonHard))
        self.buttonHard.grid(row=2, column=1, padx=(0,20))
        self.buttonQuit = Button(master, text="Quit", font=("TkDefaultFont",12), height=2, width=18)
        self.buttonQuit.grid(row=3, column=1, pady=(0,20), padx=(0,20))

    # handles button presses
    # in this case, sets difficulty variable based on user selection, and
    # closes the main menu
    def process(self, button):
        global DEBUG
        # sets difficulty based on button pressed
        if button == self.buttonEasy:
<<<<<<< HEAD
            self.difficulty = "Easy"
        elif button == self.buttonMedium:
            self.difficulty = "Medium"
        elif button == self.buttonHard:
            self.difficulty = "Hard"
=======
            self.difficulty = "easy"
        elif button == self.buttonMedium:
            self.difficulty = "medium"
        elif button == self.buttonHard:
            self.difficulty = "hard"
>>>>>>> 9a8b916987d5854a0a42d7fd4b95747204e8d2e6
        if DEBUG == True:
            print self.difficulty
        # ends window.mainloop(), allowing puzzle to generate
        window.destroy()

    # exits program from main menu
    def game_quit():
        pass

# creates GUI window for the puzzle interface
class SudokuPuzzle(Frame):
    # constructor takes two arguments: the window and the board with removed elements
    def __init__(self, master, puzzle):
        Frame.__init__(self, master)
        # selectedButton stores the Button that was last selected by the user
        # initialized to None
        self.selectedButton = None
        # puzzle buttons placed in 9x9 grid on left of interface
        # buttons labelled 0-80
        # row 0 (buttons 0-8)
        self.button0 = Button(master, text="0", height=3, width=6, command=lambda: self.processPuzzle(self.button0))
        self.button0.grid(row=0, column=0, sticky=N+E+S+W, pady=(20,0), padx=(20,0))
        self.button1 = Button(master, text="1", height=3, width=6, command=lambda: self.processPuzzle(self.button1))
        self.button1.grid(row=0, column=1, sticky=N+E+S+W, pady=(20,0))
        self.button2 = Button(master, text="2", height=3, width=6, command=lambda: self.processPuzzle(self.button2))
        self.button2.grid(row=0, column=2, sticky=N+E+S+W, pady=(20,0))
        self.button3 = Button(master, text="3", height=3, width=6, command=lambda: self.processPuzzle(self.button3))
        self.button3.grid(row=0, column=3, sticky=N+E+S+W, pady=(20,0))
        self.button4 = Button(master, text="4", height=3, width=6, command=lambda: self.processPuzzle(self.button4))
        self.button4.grid(row=0, column=4,sticky=N+E+S+W, pady=(20,0))
        self.button5 = Button(master, text="5", height=3, width=6, command=lambda: self.processPuzzle(self.button5))
        self.button5.grid(row=0, column=5, sticky=N+E+S+W, pady=(20,0))
        self.button6 = Button(master, text="6", height=3, width=6, command=lambda: self.processPuzzle(self.button6))
        self.button6.grid(row=0, column=6, sticky=N+E+S+W, pady=(20,0))
        self.button7 = Button(master, text="7", height=3, width=6, command=lambda: self.processPuzzle(self.button7))
        self.button7.grid(row=0, column=7, sticky=N+E+S+W, pady=(20,0))
        self.button8 = Button(master, text="8", height=3, width=6, command=lambda: self.processPuzzle(self.button8))
        self.button8.grid(row=0, column=8, sticky=N+E+S+W, pady=(20,0))

        # row 1 (buttons 9-17)
        self.button9 = Button(master, text="9", height=3, width=6, command=lambda: self.processPuzzle(self.button9))
        self.button9.grid(row=1, column=0, sticky=N+E+S+W, padx=(20,0))
        self.button10 = Button(master, text="10", height=3, width=6, command=lambda: self.processPuzzle(self.button10))
        self.button10.grid(row=1, column=1, sticky=N+E+S+W)
        self.button11 = Button(master, text="11", height=3, width=6, command=lambda: self.processPuzzle(self.button11))
        self.button11.grid(row=1, column=2, sticky=N+E+S+W)
        self.button12 = Button(master, text="12", height=3, width=6, command=lambda: self.processPuzzle(self.button12))
        self.button12.grid(row=1, column=3, sticky=N+E+S+W)
        self.button13 = Button(master, text="13", height=3, width=6, command=lambda: self.processPuzzle(self.button13))
        self.button13.grid(row=1, column=4, sticky=N+E+S+W)
        self.button14 = Button(master, text="14", height=3, width=6, command=lambda: self.processPuzzle(self.button14))
        self.button14.grid(row=1, column=5, sticky=N+E+S+W)
        self.button15 = Button(master, text="15", height=3, width=6, command=lambda: self.processPuzzle(self.button15))
        self.button15.grid(row=1, column=6, sticky=N+E+S+W)
        self.button16 = Button(master, text="16", height=3, width=6, command=lambda: self.processPuzzle(self.button16))
        self.button16.grid(row=1, column=7, sticky=N+E+S+W)
        self.button17 = Button(master, text="17", height=3, width=6, command=lambda: self.processPuzzle(self.button17))
        self.button17.grid(row=1, column=8, sticky=N+E+S+W)

        # row 2 (buttons 18-26)
        self.button18 = Button(master, text="18", height=3, width=6, command=lambda: self.processPuzzle(self.button18))
        self.button18.grid(row=2, column=0, sticky=N+E+S+W, padx=(20,0))
        self.button19 = Button(master, text="19", height=3, width=6, command=lambda: self.processPuzzle(self.button19))
        self.button19.grid(row=2, column=1, sticky=N+E+S+W)
        self.button20 = Button(master, text="20", height=3, width=6, command=lambda: self.processPuzzle(self.button20))
        self.button20.grid(row=2, column=2, sticky=N+E+S+W)
        self.button21 = Button(master, text="21", height=3, width=6, command=lambda: self.processPuzzle(self.button21))
        self.button21.grid(row=2, column=3, sticky=N+E+S+W)
        self.button22 = Button(master, text="22", height=3, width=6, command=lambda: self.processPuzzle(self.button22))
        self.button22.grid(row=2, column=4, sticky=N+E+S+W)
        self.button23 = Button(master, text="23", height=3, width=6, command=lambda: self.processPuzzle(self.button23))
        self.button23.grid(row=2, column=5, sticky=N+E+S+W)
        self.button24 = Button(master, text="24", height=3, width=6, command=lambda: self.processPuzzle(self.button24))
        self.button24.grid(row=2, column=6, sticky=N+E+S+W)
        self.button25 = Button(master, text="25", height=3, width=6, command=lambda: self.processPuzzle(self.button25))
        self.button25.grid(row=2, column=7, sticky=N+E+S+W)
        self.button26 = Button(master, text="26", height=3, width=6, command=lambda: self.processPuzzle(self.button26))
        self.button26.grid(row=2, column=8, sticky=N+E+S+W)

        # row 3 (buttons 27-35)
        self.button27 = Button(master, text="27", height=3, width=6, command=lambda: self.processPuzzle(self.button27))
        self.button27.grid(row=3, column=0, sticky=N+E+S+W, padx=(20,0))
        self.button28 = Button(master, text="28", height=3, width=6, command=lambda: self.processPuzzle(self.button28))
        self.button28.grid(row=3, column=1, sticky=N+E+S+W)
        self.button29 = Button(master, text="29", height=3, width=6, command=lambda: self.processPuzzle(self.button29))
        self.button29.grid(row=3, column=2, sticky=N+E+S+W)
        self.button30 = Button(master, text="30", height=3, width=6, command=lambda: self.processPuzzle(self.button30))
        self.button30.grid(row=3, column=3, sticky=N+E+S+W)
        self.button31 = Button(master, text="31", height=3, width=6, command=lambda: self.processPuzzle(self.button31))
        self.button31.grid(row=3, column=4, sticky=N+E+S+W)
        self.button32 = Button(master, text="32", height=3, width=6, command=lambda: self.processPuzzle(self.button32))
        self.button32.grid(row=3, column=5, sticky=N+E+S+W)
        self.button33 = Button(master, text="33", height=3, width=6, command=lambda: self.processPuzzle(self.button33))
        self.button33.grid(row=3, column=6, sticky=N+E+S+W)
        self.button34 = Button(master, text="34", height=3, width=6, command=lambda: self.processPuzzle(self.button34))
        self.button34.grid(row=3, column=7, sticky=N+E+S+W)
        self.button35 = Button(master, text="35", height=3, width=6, command=lambda: self.processPuzzle(self.button35))
        self.button35.grid(row=3, column=8, sticky=N+E+S+W)

        # row 4 (buttons 36-44)
        self.button36 = Button(master, text="36", height=3, width=6, command=lambda: self.processPuzzle(self.button36))
        self.button36.grid(row=4, column=0, sticky=N+E+S+W, padx=(20,0))
        self.button37 = Button(master, text="37", height=3, width=6, command=lambda: self.processPuzzle(self.button37))
        self.button37.grid(row=4, column=1, sticky=N+E+S+W)
        self.button38 = Button(master, text="38", height=3, width=6, command=lambda: self.processPuzzle(self.button38))
        self.button38.grid(row=4, column=2, sticky=N+E+S+W)
        self.button39 = Button(master, text="39", height=3, width=6, command=lambda: self.processPuzzle(self.button39))
        self.button39.grid(row=4, column=3, sticky=N+E+S+W)
        self.button40 = Button(master, text="40", height=3, width=6, command=lambda: self.processPuzzle(self.button40))
        self.button40.grid(row=4, column=4, sticky=N+E+S+W)
        self.button41 = Button(master, text="41", height=3, width=6, command=lambda: self.processPuzzle(self.button41))
        self.button41.grid(row=4, column=5, sticky=N+E+S+W)
        self.button42 = Button(master, text="42", height=3, width=6, command=lambda: self.processPuzzle(self.button42))
        self.button42.grid(row=4, column=6, sticky=N+E+S+W)
        self.button43 = Button(master, text="43", height=3, width=6, command=lambda: self.processPuzzle(self.button43))
        self.button43.grid(row=4, column=7, sticky=N+E+S+W)
        self.button44 = Button(master, text="44", height=3, width=6, command=lambda: self.processPuzzle(self.button44))
        self.button44.grid(row=4, column=8, sticky=N+E+S+W)

        # row 5 (buttons 45-53)
        self.button45 = Button(master, text="45", height=3, width=6, command=lambda: self.processPuzzle(self.button45))
        self.button45.grid(row=5, column=0, sticky=N+E+S+W, padx=(20,0))
        self.button46 = Button(master, text="46", height=3, width=6, command=lambda: self.processPuzzle(self.button46))
        self.button46.grid(row=5, column=1, sticky=N+E+S+W)
        self.button47 = Button(master, text="47", height=3, width=6, command=lambda: self.processPuzzle(self.button47))
        self.button47.grid(row=5, column=2, sticky=N+E+S+W)
        self.button48 = Button(master, text="48", height=3, width=6, command=lambda: self.processPuzzle(self.button48))
        self.button48.grid(row=5, column=3, sticky=N+E+S+W)
        self.button49 = Button(master, text="49", height=3, width=6, command=lambda: self.processPuzzle(self.button49))
        self.button49.grid(row=5, column=4, sticky=N+E+S+W)
        self.button50 = Button(master, text="50", height=3, width=6, command=lambda: self.processPuzzle(self.button50))
        self.button50.grid(row=5, column=5, sticky=N+E+S+W)
        self.button51 = Button(master, text="51", height=3, width=6, command=lambda: self.processPuzzle(self.button51))
        self.button51.grid(row=5, column=6, sticky=N+E+S+W)
        self.button52 = Button(master, text="52", height=3, width=6, command=lambda: self.processPuzzle(self.button52))
        self.button52.grid(row=5, column=7, sticky=N+E+S+W)
        self.button53 = Button(master, text="53", height=3, width=6, command=lambda: self.processPuzzle(self.button53))
        self.button53.grid(row=5, column=8, sticky=N+E+S+W)

        # row 6 (buttons 54-62)
        self.button54 = Button(master, text="54", height=3, width=6, command=lambda: self.processPuzzle(self.button54))
        self.button54.grid(row=6, column=0, sticky=N+E+S+W, padx=(20,0))
        self.button55 = Button(master, text="55", height=3, width=6, command=lambda: self.processPuzzle(self.button55))
        self.button55.grid(row=6, column=1, sticky=N+E+S+W)
        self.button56 = Button(master, text="56", height=3, width=6, command=lambda: self.processPuzzle(self.button56))
        self.button56.grid(row=6, column=2, sticky=N+E+S+W)
        self.button57 = Button(master, text="57", height=3, width=6, command=lambda: self.processPuzzle(self.button57))
        self.button57.grid(row=6, column=3, sticky=N+E+S+W)
        self.button58 = Button(master, text="58", height=3, width=6, command=lambda: self.processPuzzle(self.button58))
        self.button58.grid(row=6, column=4, sticky=N+E+S+W)
        self.button59 = Button(master, text="59", height=3, width=6, command=lambda: self.processPuzzle(self.button59))
        self.button59.grid(row=6, column=5, sticky=N+E+S+W)
        self.button60 = Button(master, text="60", height=3, width=6, command=lambda: self.processPuzzle(self.button60))
        self.button60.grid(row=6, column=6, sticky=N+E+S+W)
        self.button61 = Button(master, text="61", height=3, width=6, command=lambda: self.processPuzzle(self.button61))
        self.button61.grid(row=6, column=7, sticky=N+E+S+W)
        self.button62 = Button(master, text="62", height=3, width=6, command=lambda: self.processPuzzle(self.button62))
        self.button62.grid(row=6, column=8, sticky=N+E+S+W)

        # row 7 (buttons 63-71)
        self.button63 = Button(master, text="63", height=3, width=6, command=lambda: self.processPuzzle(self.button63))
        self.button63.grid(row=7, column=0, sticky=N+E+S+W, padx=(20,0))
        self.button64 = Button(master, text="64", height=3, width=6, command=lambda: self.processPuzzle(self.button64))
        self.button64.grid(row=7, column=1, sticky=N+E+S+W)
        self.button65 = Button(master, text="65", height=3, width=6, command=lambda: self.processPuzzle(self.button65))
        self.button65.grid(row=7, column=2, sticky=N+E+S+W)
        self.button66 = Button(master, text="66", height=3, width=6, command=lambda: self.processPuzzle(self.button66))
        self.button66.grid(row=7, column=3, sticky=N+E+S+W)
        self.button67 = Button(master, text="67", height=3, width=6, command=lambda: self.processPuzzle(self.button67))
        self.button67.grid(row=7, column=4, sticky=N+E+S+W)
        self.button68 = Button(master, text="68", height=3, width=6, command=lambda: self.processPuzzle(self.button68))
        self.button68.grid(row=7, column=5, sticky=N+E+S+W)
        self.button69 = Button(master, text="69", height=3, width=6, command=lambda: self.processPuzzle(self.button69))
        self.button69.grid(row=7, column=6, sticky=N+E+S+W)
        self.button70 = Button(master, text="70", height=3, width=6, command=lambda: self.processPuzzle(self.button70))
        self.button70.grid(row=7, column=7, sticky=N+E+S+W)
        self.button71 = Button(master, text="71", height=3, width=6, command=lambda: self.processPuzzle(self.button71))
        self.button71.grid(row=7, column=8, sticky=N+E+S+W)

        # row 8 (buttons 72-80)
        self.button72 = Button(master, text="72", height=3, width=6, command=lambda: self.processPuzzle(self.button72))
        self.button72.grid(row=8, column=0, sticky=N+E+S+W, pady=(0,20), padx=(20,0))
        self.button73 = Button(master, text="73", height=3, width=6, command=lambda: self.processPuzzle(self.button73))
        self.button73.grid(row=8, column=1, sticky=N+E+S+W, pady=(0,20))
        self.button74 = Button(master, text="74", height=3, width=6, command=lambda: self.processPuzzle(self.button74))
        self.button74.grid(row=8, column=2, sticky=N+E+S+W, pady=(0,20))
        self.button75 = Button(master, text="75", height=3, width=6, command=lambda: self.processPuzzle(self.button75))
        self.button75.grid(row=8, column=3, sticky=N+E+S+W, pady=(0,20))
        self.button76 = Button(master, text="76", height=3, width=6, command=lambda: self.processPuzzle(self.button76))
        self.button76.grid(row=8, column=4, sticky=N+E+S+W, pady=(0,20))
        self.button77 = Button(master, text="77", height=3, width=6, command=lambda: self.processPuzzle(self.button77))
        self.button77.grid(row=8, column=5, sticky=N+E+S+W, pady=(0,20))
        self.button78 = Button(master, text="78", height=3, width=6, command=lambda: self.processPuzzle(self.button78))
        self.button78.grid(row=8, column=6, sticky=N+E+S+W, pady=(0,20))
        self.button79 = Button(master, text="79", height=3, width=6, command=lambda: self.processPuzzle(self.button79))
        self.button79.grid(row=8, column=7, sticky=N+E+S+W, pady=(0,20))
        self.button80 = Button(master, text="80", height=3, width=6, command=lambda: self.processPuzzle(self.button80))
        self.button80.grid(row=8, column=8, sticky=N+E+S+W, pady=(0,20))

        # numpad buttons placed in 3x3 grid on right of interface
        self.numpad1 = Button(master, text="1", height=3, width=6, command=lambda: self.processNumpad(self.numpad1))
        self.numpad1.grid(row=5, column=9, padx=(50,0))
        self.numpad2 = Button(master, text="2", height=3, width=6, command=lambda: self.processNumpad(self.numpad2))
        self.numpad2.grid(row=5, column=10)
        self.numpad3 = Button(master, text="3", height=3, width=6, command=lambda: self.processNumpad(self.numpad3))
        self.numpad3.grid(row=5, column=11, padx=(0,20))
        self.numpad4 = Button(master, text="4", height=3, width=6, command=lambda: self.processNumpad(self.numpad4))
        self.numpad4.grid(row=4, column=9, padx=(50,0))
        self.numpad5 = Button(master, text="5", height=3, width=6, command=lambda: self.processNumpad(self.numpad5))
        self.numpad5.grid(row=4, column=10)
        self.numpad6 = Button(master, text="6", height=3, width=6, command=lambda: self.processNumpad(self.numpad6))
        self.numpad6.grid(row=4, column=11, padx=(0,20))
        self.numpad7 = Button(master, text="7", height=3, width=6, command=lambda: self.processNumpad(self.numpad7))
        self.numpad7.grid(row=3, column=9, padx=(50,0))
        self.numpad8 = Button(master, text="8", height=3, width=6, command=lambda: self.processNumpad(self.numpad8))
        self.numpad8.grid(row=3, column=10)
        self.numpad9 = Button(master, text="9", height=3, width=6, command=lambda: self.processNumpad(self.numpad9))
        self.numpad9.grid(row=3, column=11, padx=(0,20))
        self.numpadClear = Button(master, text="Clear", height=3, width=6, command=lambda: self.processNumpad(self.numpadClear))
<<<<<<< HEAD
        self.numpadClear.grid(row=6, column = 10, columnspan=2, sticky=W+E, padx=(0,20))

        # button for requesting puzzle check

=======
        self.numpadClear.grid(row=6, column=10, columnspan=2, sticky=W+E, padx=(0,20))

        # button for requesting puzzle check
        self.checkButton = Button(master, text="Check Puzzle", height=3, width=6, command=lambda: self.checkPuzzle())
        self.checkButton.grid(row=0, column=10, columnspan=2, sticky=W+E, padx=(0,20), pady=(20,0))
        
>>>>>>> 9a8b916987d5854a0a42d7fd4b95747204e8d2e6
    # process function for puzzle buttons, allows user to select a box to edit
    def processPuzzle(self, pButton):
        if self.selectedButton == None:
            pass
        else:
            self.selectedButton.config(bg="SystemButtonFace")
        self.selectedButton = pButton
        pButton.config(bg="green")

    # process function for numpad buttons, allows user to edit selected box
    def processNumpad(self, nButton):
        if self.selectedButton == None:
            pass
        else:
            if nButton == self.numpad1:
                self.selectedButton.config(text="1")
            elif nButton == self.numpad2:
                self.selectedButton.config(text="2")
            elif nButton == self.numpad3:
                self.selectedButton.config(text="3")
            elif nButton == self.numpad4:
                self.selectedButton.config(text="4")
            elif nButton == self.numpad5:
                self.selectedButton.config(text="5")
            elif nButton == self.numpad6:
                self.selectedButton.config(text="6")
            elif nButton == self.numpad7:
                self.selectedButton.config(text="7")
            elif nButton == self.numpad8:
                self.selectedButton.config(text="8")
            elif nButton == self.numpad9:
                self.selectedButton.config(text="9")
            elif nButton == self.numpadClear:
                self.selectedButton.config(text="")

    # checks to see if the users answer to the puzzle is correct
    def checkPuzzle(self):
        pass

###FUNCTIONS###


###MAIN###
global DEBUG
DEBUG = True

puzzle = []
window = Tk()
window.title("Sudoku")
app = SudokuMenu(window)
window.mainloop()
window = None
window = Tk()
window.title("Sudoku")
app = SudokuPuzzle(window, puzzle)
window.mainloop()

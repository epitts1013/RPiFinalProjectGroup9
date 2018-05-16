###
# Names: Jonas Kety, Eric Pitts, Connor Waits
# Date: May 15, 2018 
# Description: Sudoku! Generates a sudoku puzzle, and then creates a GUI based on the difficulty chosen.
# Need hints? Set DEBUG to True and check the console for the answers.
###
### Imports (and debugger) ###
from Tkinter import *
from random import randint
global DEBUG
global defaultColor
DEBUG = False

### Sudoku Function ###
def sudoku(r1, r2, r3, r4, r5 ,r6 ,r7 ,r8, r9):
        pop_list = []
        r1 = []
        r2 = []
        r3 = []
        r4 = []
        r5 = []
        r6 = []
        r7 = []
        r8 = []
        r9 = []

        columns = []
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        c5 = []
        c6 = []
        c7 = []
        c8 = []
        c9 = []
        # creates a list of the column lists
        columns.append(c1)
        columns.append(c2)
        columns.append(c3)
        columns.append(c4)
        columns.append(c5)
        columns.append(c6)
        columns.append(c7)
        columns.append(c8)
        columns.append(c9)

        blocks = []
        b1 = []
        b2 = []
        b3 = []
        b4 = []
        b5 = []
        b6 = []
        b7 = []
        b8 = []
        b9 = []
        # creates a list of the block lists
        blocks.append(b1)
        blocks.append(b2)
        blocks.append(b3)
        blocks.append(b4)
        blocks.append(b5)
        blocks.append(b6)
        blocks.append(b7)
        blocks.append(b8)
        blocks.append(b9)

        # creates the list of integers for the rows to pick from
        def population():
                for i in range(1, 10):
                        pop_list.append(i)
                return pop_list

        # adds integers from the population list to create the 1st row
        def row_1():
                pop_list = population()
                for i in range(0, 9): 
                        k = randint(0, len(pop_list)-1)
                        r1.append(pop_list[k])
                        del pop_list[k]
                # adds the integers in the first row to their corresponding columns and blocks
                for i in range(0, 9):
                        columns[i].append(r1[i])
                        if i in range(0, 3):
                                blocks[0].append(r1[i])
                        elif i in range(3, 6):
                                blocks[1].append(r1[i])
                        elif i in range(6, 9):
                                blocks[2].append(r1[i])
                return r1
        r1 = row_1()
        #creates the 2nd row
        i = 0
        pop_list = population()
        while (len(r2) < 9):
                # actually picks the numbers for each row
                # if the counter is below 54, which is the maximum amount of tries that it should take
                # to guess to fill each row
                # if the counter exceeds 54, it goes into an algorithm to clear all progess and start over, because
                # it got caught filling out a row in such away that was impossible
                if (i <= 54):
                        i += 1
                        # chooses the random index to pull from the population list
                        k = randint(0,len(pop_list)-1)
                        # only if the pop_list[k] is not in r2 and not in the column
                        if (pop_list[k] not in r2) and (pop_list[k] not in columns[(len(r2)-1)]):
                                # appends to appropriate column and block
                                if (len(r2) in range(0, 3)) and (pop_list[k] not in blocks[0]):
                                        r2.append(pop_list[k])
                                        columns[(len(r2)-1)].append(pop_list[k])
                                        blocks[0].append(pop_list[k])
                                        # deletes value from population list
                                        del pop_list[k]
                                elif (len(r2) in range(3, 6)) and (pop_list[k] not in blocks[1]):
                                        r2.append(pop_list[k])
                                        columns[(len(r2)-1)].append(pop_list[k])
                                        blocks[1].append(pop_list[k])
                                        # deletes value from population list
                                        del pop_list[k]
                                elif (len(r2) in range(6, 9)) and (pop_list[k] not in blocks[2]):
                                        r2.append(pop_list[k])
                                        columns[(len(r2)-1)].append(pop_list[k])
                                        blocks[2].append(pop_list[k])
                                        # deletes value from population list
                                        del pop_list[k]
                # clears the previous row from each of its columns and blocks and then resets the counter to start over.                                                                
                else:
                        # clears r2
                        r2 = []
                        # clears all the columns and blocks
                        columns[0] = []
                        columns[1] = []
                        columns[2] = []
                        columns[3] = []
                        columns[4] = []
                        columns[5] = []
                        columns[6] = []
                        columns[7] = []
                        columns[8] = []
                        blocks[0] = []
                        blocks[1] = []
                        blocks[2] = []
                        # puts the first row back in their respective columns and blocks
                        for i in range(0, 9):
                                columns[i].append(r1[i])
                                if i in range(0, 3):
                                        blocks[0].append(r1[i])
                                elif i in range(3, 6):
                                        blocks[1].append(r1[i])
                                elif i in range(6, 9):
                                        blocks[2].append(r1[i])
                                # sets counter to 0 and regenerates the population list
                        i = 0
                        pop_list = population()
        # the 3rd row
        i = 0
        j = 0
        pop_list = population()
        while (len(r3) < 9):
                # actually picks the numbers for each row
                # if the counter is below 54, which is the maximum amount of tries that it should take
                # to guess to fill each row
                # if the counter exceeds 54, it goes into an algorithm to clear all progess and start over, because
                # it got caught filling out a row in such away that was impossible
                if (i <= 54):
                        # adjusts counter
                        i += 1
                        # chooses random index for population list
                        k = randint(0,len(pop_list)-1)
                        # checks if population list at k is valid for that spot and appends it to
                        # appropriate lists if it is
                        if (pop_list[k] not in r3) and (pop_list[k] not in columns[(len(r3)-1)]):
                                if (len(r3) in range(0, 3)) and (pop_list[k] not in blocks[0]):
                                        r3.append(pop_list[k])
                                        columns[(len(r3)-1)].append(pop_list[k])
                                        blocks[0].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r3) in range(3, 6)) and (pop_list[k] not in blocks[1]):
                                        r3.append(pop_list[k])
                                        columns[(len(r3)-1)].append(pop_list[k])
                                        blocks[1].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r3) in range(6, 9)) and (pop_list[k] not in blocks[2]):
                                        r3.append(pop_list[k])
                                        columns[(len(r3)-1)].append(pop_list[k])
                                        blocks[2].append(pop_list[k])
                                        del pop_list[k]
                else:
                        # clears row 3
                        r3 = []
                        # deletes the last element in each column, but only if an element was added to it during the loop
                        columns = []
                        if (len(c1) == 3):
                                del c1[-1]
                        if (len(c2) == 3):
                                del c2[-1]
                        if (len(c3) == 3):
                                del c3[-1]
                        if (len(c4) == 3):
                                del c4[-1]
                        if (len(c5) == 3):
                                del c5[-1]
                        if (len(c6) == 3):
                                del c6[-1]
                        if (len(c7) == 3):
                                del c7[-1]
                        if (len(c8) == 3):
                                del c8[-1]
                        if (len(c9) == 3):
                                del c9[-1]
                        # and then appends each column back to columns
                        columns.append(c1)
                        columns.append(c2)
                        columns.append(c3)
                        columns.append(c4)
                        columns.append(c5)
                        columns.append(c6)
                        columns.append(c7)
                        columns.append(c8)
                        columns.append(c9)
                        # does the same thing for blocks
                        blocks = []
                        if (len(b1) == 9):
                                del b1[-1]
                        if (len(b1) == 8):
                                del b1[-1]
                        if (len(b1) == 7):
                                del b1[-1]
                        if (len(b2) == 9):
                                del b2[-1]
                        if (len(b2) == 8):
                                del b2[-1]
                        if (len(b2) == 7):
                                del b2[-1]
                        if (len(b3) == 9):
                                del b3[-1]
                        if (len(b3) == 8):
                                del b3[-1]
                        if (len(b3) == 7):
                                del b3[-1]
                        blocks.append(b1)
                        blocks.append(b2)
                        blocks.append(b3)
                        blocks.append(b4)
                        blocks.append(b5)
                        blocks.append(b6)
                        blocks.append(b7)
                        blocks.append(b8)
                        blocks.append(b9)
                        # resets the counter and population list
                        i = 0
                        pop_list = population()
                        # if the entire loop has iterated several times, then the this board cannot be filled out, so break out of
                        # the loop and execute Sudoku again
                        j += 1
                        if (j == 10):
                                return (r1, r2, r3, r4, r5, r6, r7, r8, r9)

        # the 4th row
        i = 0
        j = 0
        pop_list = population()
        while (len(r4) < 9):
                if (i <= 54):
                        #increments counter and chooses a random index
                        i += 1
                        k = randint(0,len(pop_list)-1)
                        # checks if population list at k is valid for that spot and appends it to
                        # appropriate lists if it is
                        if (pop_list[k] not in r4) and (pop_list[k] not in columns[(len(r4))]):
                                if (len(r4) in range(0, 3)) and (pop_list[k] not in blocks[3]):
                                        r4.append(pop_list[k])
                                        columns[(len(r4)-1)].append(pop_list[k])
                                        blocks[3].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r4) in range(3, 6)) and (pop_list[k] not in blocks[4]):
                                        r4.append(pop_list[k])
                                        columns[(len(r4)-1)].append(pop_list[k])
                                        blocks[4].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r4) in range(6, 9)) and (pop_list[k] not in blocks[5]):
                                        r4.append(pop_list[k])
                                        columns[(len(r4)-1)].append(pop_list[k])
                                        blocks[5].append(pop_list[k])
                                        del pop_list[k]
                else:
                        # clears row 4
                        r4 = []
                        # deletes the last element in each column, but only if an element was added to it during the loop
                        columns = []
                        if (len(c1) == 4):
                                del c1[-1]
                        if (len(c2) == 4):
                                del c2[-1]
                        if (len(c3) == 4):
                                del c3[-1]
                        if (len(c4) == 4):
                                del c4[-1]
                        if (len(c5) == 4):
                                del c5[-1]
                        if (len(c6) == 4):
                                del c6[-1]
                        if (len(c7) == 4):
                                del c7[-1]
                        if (len(c8) == 4):
                                del c8[-1]
                        if (len(c9) == 4):
                                del c9[-1]
                        # and then appends each column back to columns
                        columns.append(c1)
                        columns.append(c2)
                        columns.append(c3)
                        columns.append(c4)
                        columns.append(c5)
                        columns.append(c6)
                        columns.append(c7)
                        columns.append(c8)
                        columns.append(c9)
                        # does the same thing for blocks
                        blocks = []
                        if (len(b4) == 3):
                                del b4[-1]
                        if (len(b4) == 2):
                                del b4[-1]
                        if (len(b4) == 1):
                                del b4[-1]
                        if (len(b5) == 3):
                                del b5[-1]
                        if (len(b5) == 2):
                                del b5[-1]
                        if (len(b5) == 1):
                                del b5[-1]
                        if (len(b6) == 3):
                                del b6[-1]
                        if (len(b6) == 2):
                                del b6[-1]
                        if (len(b6) == 1):
                                del b6[-1]
                        blocks.append(b1)
                        blocks.append(b2)
                        blocks.append(b3)
                        blocks.append(b4)
                        blocks.append(b5)
                        blocks.append(b6)
                        blocks.append(b7)
                        blocks.append(b8)
                        blocks.append(b9)
                        # resets the counter and population list
                        i = 0
                        pop_list = population()
                        # if the entire loop has iterated several times, then the this board cannot be filled out, so break out of
                        # the loop and execute Sudoku again
                        j += 1
                        if (j == 10):
                                return (r1, r2, r3, r4, r5, r6, r7, r8, r9)

        # the 5th row
        i = 0
        j = 0
        pop_list = population()
        while (len(r5) < 9):
                if (i <= 54):
                        #increments counter and chooses a random index
                        i += 1
                        k = randint(0,len(pop_list)-1)
                        # checks if population list at k is valid for that spot and appends it to
                        # appropriate lists if it is
                        if (pop_list[k] not in r5) and (pop_list[k] not in columns[(len(r5))]):
                                if (len(r5) in range(0, 3)) and (pop_list[k] not in blocks[3]):
                                        r5.append(pop_list[k])
                                        columns[(len(r5)-1)].append(pop_list[k])
                                        blocks[3].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r5) in range(3, 6)) and (pop_list[k] not in blocks[4]):
                                        r5.append(pop_list[k])
                                        columns[(len(r5)-1)].append(pop_list[k])
                                        blocks[4].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r5) in range(6, 9)) and (pop_list[k] not in blocks[5]):
                                        r5.append(pop_list[k])
                                        columns[(len(r5)-1)].append(pop_list[k])
                                        blocks[5].append(pop_list[k])
                                        del pop_list[k]
                else:
                        # clears row 5
                        r5 = []
                        # deletes the last element in each column, but only if an element was added to it during the loop
                        columns = []
                        if (len(c1) == 5):
                                del c1[-1]
                        if (len(c2) == 5):
                                del c2[-1]
                        if (len(c3) == 5):
                                del c3[-1]
                        if (len(c4) == 5):
                                del c4[-1]
                        if (len(c5) == 5):
                                del c5[-1]
                        if (len(c6) == 5):
                                del c6[-1]
                        if (len(c7) == 5):
                                del c7[-1]
                        if (len(c8) == 5):
                                del c8[-1]
                        if (len(c9) == 5):
                                del c9[-1]
                        # and then appends each column back to columns
                        columns.append(c1)
                        columns.append(c2)
                        columns.append(c3)
                        columns.append(c4)
                        columns.append(c5)
                        columns.append(c6)
                        columns.append(c7)
                        columns.append(c8)
                        columns.append(c9)
                        # does the same thing for blocks
                        blocks = []
                        if (len(b4) == 6):
                                del b4[-1]
                        if (len(b4) == 5):
                                del b4[-1]
                        if (len(b4) == 4):
                                del b4[-1]
                        if (len(b5) == 6):
                                del b5[-1]
                        if (len(b5) == 5):
                                del b5[-1]
                        if (len(b5) == 4):
                                del b5[-1]
                        if (len(b6) == 6):
                                del b6[-1]
                        if (len(b6) == 5):
                                del b6[-1]
                        if (len(b6) == 4):
                                del b6[-1]
                        blocks.append(b1)
                        blocks.append(b2)
                        blocks.append(b3)
                        blocks.append(b4)
                        blocks.append(b5)
                        blocks.append(b6)
                        blocks.append(b7)
                        blocks.append(b8)
                        blocks.append(b9)
                        # resets the counter and population list
                        i = 0
                        pop_list = population()
                        # if the entire loop has iterated several times, then the this board cannot be filled out, so break out of
                        # the loop and execute Sudoku again
                        j += 1
                        if (j == 10):
                                return (r1, r2, r3, r4, r5, r6, r7, r8, r9)

        # the 6th row
        i = 0
        j = 0
        pop_list = population()
        while (len(r6) < 9):
                if (i <= 54):
                        #increments counter and chooses a random index
                        i += 1
                        k = randint(0,len(pop_list)-1)
                        # checks if population list at k is valid for that spot and appends it to
                        # appropriate lists if it is
                        if (pop_list[k] not in r6) and (pop_list[k] not in columns[(len(r6))]):
                                if (len(r6) in range(0, 3)) and (pop_list[k] not in blocks[3]):
                                        r6.append(pop_list[k])
                                        columns[(len(r6)-1)].append(pop_list[k])
                                        blocks[3].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r6) in range(3, 6)) and (pop_list[k] not in blocks[4]):
                                        r6.append(pop_list[k])
                                        columns[(len(r6)-1)].append(pop_list[k])
                                        blocks[4].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r6) in range(6, 9)) and (pop_list[k] not in blocks[5]):
                                        r6.append(pop_list[k])
                                        columns[(len(r6)-1)].append(pop_list[k])
                                        blocks[5].append(pop_list[k])
                                        del pop_list[k]
                else:
                        # clears row 6
                        r6 = []
                        # deletes the last element in each column, but only if an element was added to it during the loop
                        columns = []
                        if (len(c1) == 6):
                                del c1[-1]
                        if (len(c2) == 6):
                                del c2[-1]
                        if (len(c3) == 6):
                                del c3[-1]
                        if (len(c4) == 6):
                                del c4[-1]
                        if (len(c5) == 6):
                                del c5[-1]
                        if (len(c6) == 6):
                                del c6[-1]
                        if (len(c7) == 6):
                                del c7[-1]
                        if (len(c8) == 6):
                                del c8[-1]
                        if (len(c9) == 6):
                                del c9[-1]
                        # and then appends each column back to columns
                        columns.append(c1)
                        columns.append(c2)
                        columns.append(c3)
                        columns.append(c4)
                        columns.append(c5)
                        columns.append(c6)
                        columns.append(c7)
                        columns.append(c8)
                        columns.append(c9)
                        # does the same thing for blocks
                        blocks = []
                        if (len(b4) == 9):
                                del b4[-1]
                        if (len(b4) == 8):
                                del b4[-1]
                        if (len(b4) == 7):
                                del b4[-1]
                        if (len(b5) == 9):
                                del b5[-1]
                        if (len(b5) == 8):
                                del b5[-1]
                        if (len(b5) == 7):
                                del b5[-1]
                        if (len(b6) == 9):
                                del b6[-1]
                        if (len(b6) == 8):
                                del b6[-1]
                        if (len(b6) == 7):
                                del b6[-1]
                        blocks.append(b1)
                        blocks.append(b2)
                        blocks.append(b3)
                        blocks.append(b4)
                        blocks.append(b5)
                        blocks.append(b6)
                        blocks.append(b7)
                        blocks.append(b8)
                        blocks.append(b9)
                        # resets the counter and population list
                        i = 0
                        pop_list = population()
                        # if the entire loop has iterated several times, then the this board cannot be filled out, so break out of
                        # the loop and execute Sudoku again
                        j += 1
                        if (j == 10):
                                return (r1, r2, r3, r4, r5, r6, r7, r8, r9)

        # the 7th row
        i = 0
        j = 0
        pop_list = population()
        while (len(r7) < 9):
                if (i <= 54):
                        #increments counter and chooses a random index
                        i += 1
                        k = randint(0,len(pop_list)-1)
                        # checks if population list at k is valid for that spot and appends it to
                        # appropriate lists if it is
                        if (pop_list[k] not in r7) and (pop_list[k] not in columns[(len(r7))]):
                                if (len(r7) in range(0, 3)) and (pop_list[k] not in blocks[6]):
                                        r7.append(pop_list[k])
                                        columns[(len(r7)-1)].append(pop_list[k])
                                        blocks[6].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r7) in range(3, 6)) and (pop_list[k] not in blocks[7]):
                                        r7.append(pop_list[k])
                                        columns[(len(r7)-1)].append(pop_list[k])
                                        blocks[7].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r7) in range(6, 9)) and (pop_list[k] not in blocks[8]):
                                        r7.append(pop_list[k])
                                        columns[(len(r7)-1)].append(pop_list[k])
                                        blocks[8].append(pop_list[k])
                                        del pop_list[k]
                else:
                        # clears row 7
                        r7 = []
                        # deletes the last element in each column, but only if an element was added to it during the loop
                        columns = []
                        if (len(c1) == 7):
                                del c1[-1]
                        if (len(c2) == 7):
                                del c2[-1]
                        if (len(c3) == 7):
                                del c3[-1]
                        if (len(c4) == 7):
                                del c4[-1]
                        if (len(c5) == 7):
                                del c5[-1]
                        if (len(c6) == 7):
                                del c6[-1]
                        if (len(c7) == 7):
                                del c7[-1]
                        if (len(c8) == 7):
                                del c8[-1]
                        if (len(c9) == 7):
                                del c9[-1]
                        # and then appends each column back to columns
                        columns.append(c1)
                        columns.append(c2)
                        columns.append(c3)
                        columns.append(c4)
                        columns.append(c5)
                        columns.append(c6)
                        columns.append(c7)
                        columns.append(c8)
                        columns.append(c9)
                        # does the same thing for blocks
                        blocks = []
                        if (len(b7) == 3):
                                del b7[-1]
                        if (len(b7) == 2):
                                del b7[-1]
                        if (len(b7) == 1):
                                del b7[-1]
                        if (len(b8) == 3):
                                del b8[-1]
                        if (len(b8) == 2):
                                del b8[-1]
                        if (len(b8) == 1):
                                del b8[-1]
                        if (len(b9) == 3):
                                del b9[-1]
                        if (len(b9) == 2):
                                del b9[-1]
                        if (len(b9) == 1):
                                del b9[-1]
                        blocks.append(b1)
                        blocks.append(b2)
                        blocks.append(b3)
                        blocks.append(b4)
                        blocks.append(b5)
                        blocks.append(b6)
                        blocks.append(b7)
                        blocks.append(b8)
                        blocks.append(b9)
                        # resets the counter and population list
                        i = 0
                        pop_list = population()
                        # if the entire loop has iterated several times, then the this board cannot be filled out, so break out of
                        # the loop and execute Sudoku again
                        j += 1
                        if (j == 10):
                                return (r1, r2, r3, r4, r5, r6, r7, r8, r9)
        # the 8th row
        i = 0
        j = 0
        pop_list = population()
        while (len(r8) < 9):
                if (i <= 54):
                        #increments counter and chooses a random index
                        i += 1
                        k = randint(0,len(pop_list)-1)
                        # checks if population list at k is valid for that spot and appends it to
                        # appropriate lists if it is
                        if (pop_list[k] not in r8) and (pop_list[k] not in columns[(len(r8))]):
                                if (len(r8) in range(0, 3)) and (pop_list[k] not in blocks[6]):
                                        r8.append(pop_list[k])
                                        columns[(len(r8)-1)].append(pop_list[k])
                                        blocks[6].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r8) in range(3, 6)) and (pop_list[k] not in blocks[7]):
                                        r8.append(pop_list[k])
                                        columns[(len(r8)-1)].append(pop_list[k])
                                        blocks[7].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r8) in range(6, 9)) and (pop_list[k] not in blocks[8]):
                                        r8.append(pop_list[k])
                                        columns[(len(r8)-1)].append(pop_list[k])
                                        blocks[8].append(pop_list[k])
                                        del pop_list[k]
                else:
                        # clears row 8
                        r8 = []
                        # deletes the last element in each column, but only if an element was added to it during the loop
                        columns = []
                        if (len(c1) == 8):
                                del c1[-1]
                        if (len(c2) == 8):
                                del c2[-1]
                        if (len(c3) == 8):
                                del c3[-1]
                        if (len(c4) == 8):
                                del c4[-1]
                        if (len(c5) == 8):
                                del c5[-1]
                        if (len(c6) == 8):
                                del c6[-1]
                        if (len(c7) == 8):
                                del c7[-1]
                        if (len(c8) == 8):
                                del c8[-1]
                        if (len(c9) == 8):
                                del c9[-1]
                        # and then appends each column back to columns
                        columns.append(c1)
                        columns.append(c2)
                        columns.append(c3)
                        columns.append(c4)
                        columns.append(c5)
                        columns.append(c6)
                        columns.append(c7)
                        columns.append(c8)
                        columns.append(c9)
                        # does the same thing for blocks
                        blocks = []
                        if (len(b7) == 6):
                                del b7[-1]
                        if (len(b7) == 5):
                                del b7[-1]
                        if (len(b7) == 4):
                                del b7[-1]
                        if (len(b8) == 6):
                                del b8[-1]
                        if (len(b8) == 5):
                                del b8[-1]
                        if (len(b8) == 4):
                                del b8[-1]
                        if (len(b9) == 6):
                                del b9[-1]
                        if (len(b9) == 5):
                                del b9[-1]
                        if (len(b9) == 4):
                                del b9[-1]
                        blocks.append(b1)
                        blocks.append(b2)
                        blocks.append(b3)
                        blocks.append(b4)
                        blocks.append(b5)
                        blocks.append(b6)
                        blocks.append(b7)
                        blocks.append(b8)
                        blocks.append(b9)
                        # resets the counter and population list
                        i = 0
                        pop_list = population()
                        # if the entire loop has iterated several times, then the this board cannot be filled out, so break out of
                        # the loop and execute Sudoku again
                        j += 1
                        if (j == 10):
                                return (r1, r2, r3, r4, r5, r6, r7, r8, r9)

        # the 9th row
        i = 0
        j = 0
        pop_list = population()
        while (len(r9) < 9):
                if (i <= 54):
                        #increments counter and chooses a random index
                        i += 1
                        k = randint(0,len(pop_list)-1)
                        # checks if population list at k is valid for that spot and appends it to
                        # appropriate lists if it is
                        if (pop_list[k] not in r9) and (pop_list[k] not in columns[(len(r9))]):
                                if (len(r9) in range(0, 3)) and (pop_list[k] not in blocks[6]):
                                        r9.append(pop_list[k])
                                        columns[(len(r9)-1)].append(pop_list[k])
                                        blocks[6].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r9) in range(3, 6)) and (pop_list[k] not in blocks[7]):
                                        r9.append(pop_list[k])
                                        columns[(len(r9)-1)].append(pop_list[k])
                                        blocks[7].append(pop_list[k])
                                        del pop_list[k]
                                elif (len(r9) in range(6, 9)) and (pop_list[k] not in blocks[8]):
                                        r9.append(pop_list[k])
                                        columns[(len(r9)-1)].append(pop_list[k])
                                        blocks[8].append(pop_list[k])
                                        del pop_list[k]
                else:
                        # clears row 9
                        r9 = []
                        # deletes the last element in each column, but only if an element was added to it during the loop
                        columns = []
                        if (len(c1) == 9):
                                del c1[-1]
                        if (len(c2) == 9):
                                del c2[-1]
                        if (len(c3) == 9):
                                del c3[-1]
                        if (len(c4) == 9):
                                del c4[-1]
                        if (len(c5) == 9):
                                del c5[-1]
                        if (len(c6) == 9):
                                del c6[-1]
                        if (len(c7) == 9):
                                del c7[-1]
                        if (len(c8) == 9):
                                del c8[-1]
                        if (len(c9) == 9):
                                del c9[-1]
                        # and then appends each column back to columns
                        columns.append(c1)
                        columns.append(c2)
                        columns.append(c3)
                        columns.append(c4)
                        columns.append(c5)
                        columns.append(c6)
                        columns.append(c7)
                        columns.append(c8)
                        columns.append(c9)
                        # does the same thing for blocks
                        blocks = []
                        if (len(b7) == 9):
                                del b7[-1]
                        if (len(b7) == 8):
                                del b7[-1]
                        if (len(b7) == 7):
                                del b7[-1]
                        if (len(b8) == 9):
                                del b8[-1]
                        if (len(b8) == 8):
                                del b8[-1]
                        if (len(b8) == 7):
                                del b8[-1]
                        if (len(b9) == 9):
                                del b9[-1]
                        if (len(b9) == 8):
                                del b9[-1]
                        if (len(b9) == 7):
                                del b9[-1]
                        blocks.append(b1)
                        blocks.append(b2)
                        blocks.append(b3)
                        blocks.append(b4)
                        blocks.append(b5)
                        blocks.append(b6)
                        blocks.append(b7)
                        blocks.append(b8)
                        blocks.append(b9)
                        # resets the counter and population list
                        i = 0
                        pop_list = population()
                        # if the entire loop has iterated several times, then the this board cannot be filled out, so break out of
                        # the loop and execute Sudoku again
                        j += 1
                        if (j == 10):
                                r9 = []
                                return (r1, r2, r3, r4, r5, r6, r7, r8, r9)
        return (r1, r2, r3, r4, r5, r6, r7, r8, r9)

### Calls the Sudoku Function ###
# this is called before the window is made so Tkinter has something to base the window on
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []
# call the sudoku function until r9 is filled 
while ((len(r9) < 9)):
        (r1, r2, r3, r4, r5, r6, r7, r8, r9) = sudoku(r1, r2, r3, r4, r5, r6, r7, r8, r9)
# creates the list of solutions, to check puzzle against later
solution = []
for i in range(0, 9):
        solution.append(r1[i])
for i in range(0, 9):
        solution.append(r2[i])
for i in range(0, 9):
        solution.append(r3[i])
for i in range(0, 9):
        solution.append(r4[i])
for i in range(0, 9):
        solution.append(r5[i])
for i in range(0, 9):
        solution.append(r6[i])
for i in range(0, 9):
        solution.append(r7[i])
for i in range(0, 9):
        solution.append(r8[i])
for i in range(0, 9):
        solution.append(r9[i])

# gives the solution if DEBUG is set to true
if DEBUG == True:
        print r1
        print r2
        print r3
        print r4
        print r5
        print r6
        print r7
        print r8
        print r9
        print solution

### Window Classes ###
# creates GUI window for the start menu interface
class SudokuMenu(Frame):
        #constructor takes one argument: the window
        def __init__(self, master):
                Frame.__init__(self, master)
                global defaultColor
                # difficulty variable, set to easy by default
                self.difficulty = "Easy"
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
                self.buttonQuit = Button(master, text="Quit", font=("TkDefaultFont",12), height=2, width=18, command=lambda: self.process(self.buttonQuit))
                self.buttonQuit.grid(row=3, column=1, pady=(0,20), padx=(0,20))
                defaultColor = self.buttonEasy['background']

        # handles button presses
        # in this case, sets difficulty variable based on user selection, and
        # closes the main menu
        def process(self, button):
                global DEBUG
                global d
                # sets difficulty based on button pressed
                if button == self.buttonEasy:
                        self.difficulty = "Easy"
                        d = randint(49, 55)
                elif button == self.buttonMedium:
                        self.difficulty = "Medium"
                        d = randint(40, 48)
                elif button == self.buttonHard:
                        self.difficulty = "Hard"
                        d = randint(56, 64)
                # quits the game if the quit button is pressed
                # doesn't allow the second window to generate
                elif button == self.buttonQuit:
                        quit()
                                        
                if DEBUG == True:
                        print self.difficulty
                # ends window.mainloop(), allowing puzzle to generate
                window.destroy()
                return d

# creates GUI window for the puzzle interface
class SudokuPuzzle(Frame):
        # constructor takes two arguments: the window and the board with removed elements
        def __init__(self, master):
                Frame.__init__(self, master)
                # selectedButton stores the Button that was last selected by the user
                # initialized to None
                self.selectedButton = None

                # master list of puzzle buttons
                # for use in iterating through all buttons
                self.masterList = []

                # the status label
                # gives the user important information
                # i.e. "Not correct", "Not finished", etc.
                self.labelStatus = Label(master, text = "")
                self.labelStatus.grid(row=1, column=9, sticky=N+S+E+W, padx=(0,20), rowspan=2, columnspan=3)

                # puzzle buttons placed in 9x9 grid on left of interface
                # buttons labelled 0-80
                # row 0 (buttons 0-8)
                self.button0 = Button(master, text=r1[0], height=1, width=2, command=lambda: self.processPuzzle(self.button0))
                self.button0.grid(row=0, column=0, sticky=N+E+S+W, pady=(20,0), padx=(20,0))
                self.masterList.append(self.button0)
                self.button1 = Button(master, text=r1[1], height=1, width=2, command=lambda: self.processPuzzle(self.button1))
                self.button1.grid(row=0, column=1, sticky=N+E+S+W, pady=(20,0))
                self.masterList.append(self.button1)
                self.button2 = Button(master, text=r1[2], height=1, width=2, command=lambda: self.processPuzzle(self.button2))
                self.button2.grid(row=0, column=2, sticky=N+E+S+W, pady=(20,0))
                self.masterList.append(self.button2)
                self.button3 = Button(master, text=r1[3], height=1, width=2, command=lambda: self.processPuzzle(self.button3))
                self.button3.grid(row=0, column=3, sticky=N+E+S+W, pady=(20,0))
                self.masterList.append(self.button3)
                self.button4 = Button(master, text=r1[4], height=1, width=2, command=lambda: self.processPuzzle(self.button4))
                self.button4.grid(row=0, column=4,sticky=N+E+S+W, pady=(20,0))
                self.masterList.append(self.button4)
                self.button5 = Button(master, text=r1[5], height=1, width=2, command=lambda: self.processPuzzle(self.button5))
                self.button5.grid(row=0, column=5, sticky=N+E+S+W, pady=(20,0))
                self.masterList.append(self.button5)
                self.button6 = Button(master, text=r1[6], height=1, width=2, command=lambda: self.processPuzzle(self.button6))
                self.button6.grid(row=0, column=6, sticky=N+E+S+W, pady=(20,0))
                self.masterList.append(self.button6)
                self.button7 = Button(master, text=r1[7], height=1, width=2, command=lambda: self.processPuzzle(self.button7))
                self.button7.grid(row=0, column=7, sticky=N+E+S+W, pady=(20,0))
                self.masterList.append(self.button7)
                self.button8 = Button(master, text=r1[8], height=1, width=2, command=lambda: self.processPuzzle(self.button8))
                self.button8.grid(row=0, column=8, sticky=N+E+S+W, pady=(20,0))
                self.masterList.append(self.button8)

                # row 1 (buttons 9-17)
                self.button9 = Button(master, text=r2[0], height=1, width=2, command=lambda: self.processPuzzle(self.button9))
                self.button9.grid(row=1, column=0, sticky=N+E+S+W, padx=(20,0))
                self.masterList.append(self.button9)
                self.button10 = Button(master, text=r2[1], height=1, width=2, command=lambda: self.processPuzzle(self.button10))
                self.button10.grid(row=1, column=1, sticky=N+E+S+W)
                self.masterList.append(self.button10)
                self.button11 = Button(master, text=r2[2], height=1, width=2, command=lambda: self.processPuzzle(self.button11))
                self.button11.grid(row=1, column=2, sticky=N+E+S+W)
                self.masterList.append(self.button11)
                self.button12 = Button(master, text=r2[3], height=1, width=2, command=lambda: self.processPuzzle(self.button12))
                self.button12.grid(row=1, column=3, sticky=N+E+S+W)
                self.masterList.append(self.button12)
                self.button13 = Button(master, text=r2[4], height=1, width=2, command=lambda: self.processPuzzle(self.button13))
                self.button13.grid(row=1, column=4, sticky=N+E+S+W)
                self.masterList.append(self.button13)
                self.button14 = Button(master, text=r2[5], height=1, width=2, command=lambda: self.processPuzzle(self.button14))
                self.button14.grid(row=1, column=5, sticky=N+E+S+W)
                self.masterList.append(self.button14)
                self.button15 = Button(master, text=r2[6], height=1, width=2, command=lambda: self.processPuzzle(self.button15))
                self.button15.grid(row=1, column=6, sticky=N+E+S+W)
                self.masterList.append(self.button15)
                self.button16 = Button(master, text=r2[7], height=1, width=2, command=lambda: self.processPuzzle(self.button16))
                self.button16.grid(row=1, column=7, sticky=N+E+S+W)
                self.masterList.append(self.button16)
                self.button17 = Button(master, text=r2[8], height=1, width=2, command=lambda: self.processPuzzle(self.button17))
                self.button17.grid(row=1, column=8, sticky=N+E+S+W)
                self.masterList.append(self.button17)

                # row 2 (buttons 18-26)
                self.button18 = Button(master, text=r3[0], height=1, width=2, command=lambda: self.processPuzzle(self.button18))
                self.button18.grid(row=2, column=0, sticky=N+E+S+W, padx=(20,0))
                self.masterList.append(self.button18)
                self.button19 = Button(master, text=r3[1], height=1, width=2, command=lambda: self.processPuzzle(self.button19))
                self.button19.grid(row=2, column=1, sticky=N+E+S+W)
                self.masterList.append(self.button19)
                self.button20 = Button(master, text=r3[2], height=1, width=2, command=lambda: self.processPuzzle(self.button20))
                self.button20.grid(row=2, column=2, sticky=N+E+S+W)
                self.masterList.append(self.button20)
                self.button21 = Button(master, text=r3[3], height=1, width=2, command=lambda: self.processPuzzle(self.button21))
                self.button21.grid(row=2, column=3, sticky=N+E+S+W)
                self.masterList.append(self.button21)
                self.button22 = Button(master, text=r3[4], height=1, width=2, command=lambda: self.processPuzzle(self.button22))
                self.button22.grid(row=2, column=4, sticky=N+E+S+W)
                self.masterList.append(self.button22)
                self.button23 = Button(master, text=r3[5], height=1, width=2, command=lambda: self.processPuzzle(self.button23))
                self.button23.grid(row=2, column=5, sticky=N+E+S+W)
                self.masterList.append(self.button23)
                self.button24 = Button(master, text=r3[6], height=1, width=2, command=lambda: self.processPuzzle(self.button24))
                self.button24.grid(row=2, column=6, sticky=N+E+S+W)
                self.masterList.append(self.button24)
                self.button25 = Button(master, text=r3[7], height=1, width=2, command=lambda: self.processPuzzle(self.button25))
                self.button25.grid(row=2, column=7, sticky=N+E+S+W)
                self.masterList.append(self.button25)
                self.button26 = Button(master, text=r3[8], height=1, width=2, command=lambda: self.processPuzzle(self.button26))
                self.button26.grid(row=2, column=8, sticky=N+E+S+W)
                self.masterList.append(self.button26)

                # row 3 (buttons 27-35)
                self.button27 = Button(master, text=r4[0], height=1, width=2, command=lambda: self.processPuzzle(self.button27))
                self.button27.grid(row=3, column=0, sticky=N+E+S+W, padx=(20,0))
                self.masterList.append(self.button27)
                self.button28 = Button(master, text=r4[1], height=1, width=2, command=lambda: self.processPuzzle(self.button28))
                self.button28.grid(row=3, column=1, sticky=N+E+S+W)
                self.masterList.append(self.button28)
                self.button29 = Button(master, text=r4[2], height=1, width=2, command=lambda: self.processPuzzle(self.button29))
                self.button29.grid(row=3, column=2, sticky=N+E+S+W)
                self.masterList.append(self.button29)
                self.button30 = Button(master, text=r4[3], height=1, width=2, command=lambda: self.processPuzzle(self.button30))
                self.button30.grid(row=3, column=3, sticky=N+E+S+W)
                self.masterList.append(self.button30)
                self.button31 = Button(master, text=r4[4], height=1, width=2, command=lambda: self.processPuzzle(self.button31))
                self.button31.grid(row=3, column=4, sticky=N+E+S+W)
                self.masterList.append(self.button31)
                self.button32 = Button(master, text=r4[5], height=1, width=2, command=lambda: self.processPuzzle(self.button32))
                self.button32.grid(row=3, column=5, sticky=N+E+S+W)
                self.masterList.append(self.button32)
                self.button33 = Button(master, text=r4[6], height=1, width=2, command=lambda: self.processPuzzle(self.button33))
                self.button33.grid(row=3, column=6, sticky=N+E+S+W)
                self.masterList.append(self.button33)
                self.button34 = Button(master, text=r4[7], height=1, width=2, command=lambda: self.processPuzzle(self.button34))
                self.button34.grid(row=3, column=7, sticky=N+E+S+W)
                self.masterList.append(self.button34)
                self.button35 = Button(master, text=r4[8], height=1, width=2, command=lambda: self.processPuzzle(self.button35))
                self.button35.grid(row=3, column=8, sticky=N+E+S+W)
                self.masterList.append(self.button35)

                # row 4 (buttons 36-44)
                self.button36 = Button(master, text=r5[0], height=1, width=2, command=lambda: self.processPuzzle(self.button36))
                self.button36.grid(row=4, column=0, sticky=N+E+S+W, padx=(20,0))
                self.masterList.append(self.button36)
                self.button37 = Button(master, text=r5[1], height=1, width=2, command=lambda: self.processPuzzle(self.button37))
                self.button37.grid(row=4, column=1, sticky=N+E+S+W)
                self.masterList.append(self.button37)
                self.button38 = Button(master, text=r5[2], height=1, width=2, command=lambda: self.processPuzzle(self.button38))
                self.button38.grid(row=4, column=2, sticky=N+E+S+W)
                self.masterList.append(self.button38)
                self.button39 = Button(master, text=r5[3], height=1, width=2, command=lambda: self.processPuzzle(self.button39))
                self.button39.grid(row=4, column=3, sticky=N+E+S+W)
                self.masterList.append(self.button39)
                self.button40 = Button(master, text=r5[4], height=1, width=2, command=lambda: self.processPuzzle(self.button40))
                self.button40.grid(row=4, column=4, sticky=N+E+S+W)
                self.masterList.append(self.button40)
                self.button41 = Button(master, text=r5[5], height=1, width=2, command=lambda: self.processPuzzle(self.button41))
                self.button41.grid(row=4, column=5, sticky=N+E+S+W)
                self.masterList.append(self.button41)
                self.button42 = Button(master, text=r5[6], height=1, width=2, command=lambda: self.processPuzzle(self.button42))
                self.button42.grid(row=4, column=6, sticky=N+E+S+W)
                self.masterList.append(self.button42)
                self.button43 = Button(master, text=r5[7], height=1, width=2, command=lambda: self.processPuzzle(self.button43))
                self.button43.grid(row=4, column=7, sticky=N+E+S+W)
                self.masterList.append(self.button43)
                self.button44 = Button(master, text=r5[8], height=1, width=2, command=lambda: self.processPuzzle(self.button44))
                self.button44.grid(row=4, column=8, sticky=N+E+S+W)
                self.masterList.append(self.button44)

                # row 5 (buttons 45-53)
                self.button45 = Button(master, text=r6[0], height=1, width=2, command=lambda: self.processPuzzle(self.button45))
                self.button45.grid(row=5, column=0, sticky=N+E+S+W, padx=(20,0))
                self.masterList.append(self.button45)
                self.button46 = Button(master, text=r6[1], height=1, width=2, command=lambda: self.processPuzzle(self.button46))
                self.button46.grid(row=5, column=1, sticky=N+E+S+W)
                self.masterList.append(self.button46)
                self.button47 = Button(master, text=r6[2], height=1, width=2, command=lambda: self.processPuzzle(self.button47))
                self.button47.grid(row=5, column=2, sticky=N+E+S+W)
                self.masterList.append(self.button47)
                self.button48 = Button(master, text=r6[3], height=1, width=2, command=lambda: self.processPuzzle(self.button48))
                self.button48.grid(row=5, column=3, sticky=N+E+S+W)
                self.masterList.append(self.button48)
                self.button49 = Button(master, text=r6[4], height=1, width=2, command=lambda: self.processPuzzle(self.button49))
                self.button49.grid(row=5, column=4, sticky=N+E+S+W)
                self.masterList.append(self.button49)
                self.button50 = Button(master, text=r6[5], height=1, width=2, command=lambda: self.processPuzzle(self.button50))
                self.button50.grid(row=5, column=5, sticky=N+E+S+W)
                self.masterList.append(self.button50)
                self.button51 = Button(master, text=r6[6], height=1, width=2, command=lambda: self.processPuzzle(self.button51))
                self.button51.grid(row=5, column=6, sticky=N+E+S+W)
                self.masterList.append(self.button51)
                self.button52 = Button(master, text=r6[7], height=1, width=2, command=lambda: self.processPuzzle(self.button52))
                self.button52.grid(row=5, column=7, sticky=N+E+S+W)
                self.masterList.append(self.button52)
                self.button53 = Button(master, text=r6[8], height=1, width=2, command=lambda: self.processPuzzle(self.button53))
                self.button53.grid(row=5, column=8, sticky=N+E+S+W)
                self.masterList.append(self.button53)

                # row 6 (buttons 54-62)
                self.button54 = Button(master, text=r7[0], height=1, width=2, command=lambda: self.processPuzzle(self.button54))
                self.button54.grid(row=6, column=0, sticky=N+E+S+W, padx=(20,0))
                self.masterList.append(self.button54)
                self.button55 = Button(master, text=r7[1], height=1, width=2, command=lambda: self.processPuzzle(self.button55))
                self.button55.grid(row=6, column=1, sticky=N+E+S+W)
                self.masterList.append(self.button55)
                self.button56 = Button(master, text=r7[2], height=1, width=2, command=lambda: self.processPuzzle(self.button56))
                self.button56.grid(row=6, column=2, sticky=N+E+S+W)
                self.masterList.append(self.button56)
                self.button57 = Button(master, text=r7[3], height=1, width=2, command=lambda: self.processPuzzle(self.button57))
                self.button57.grid(row=6, column=3, sticky=N+E+S+W)
                self.masterList.append(self.button57)
                self.button58 = Button(master, text=r7[4], height=1, width=2, command=lambda: self.processPuzzle(self.button58))
                self.button58.grid(row=6, column=4, sticky=N+E+S+W)
                self.masterList.append(self.button58)
                self.button59 = Button(master, text=r7[5], height=1, width=2, command=lambda: self.processPuzzle(self.button59))
                self.button59.grid(row=6, column=5, sticky=N+E+S+W)
                self.masterList.append(self.button59)
                self.button60 = Button(master, text=r7[6], height=1, width=2, command=lambda: self.processPuzzle(self.button60))
                self.button60.grid(row=6, column=6, sticky=N+E+S+W)
                self.masterList.append(self.button60)
                self.button61 = Button(master, text=r7[7], height=1, width=2, command=lambda: self.processPuzzle(self.button61))
                self.button61.grid(row=6, column=7, sticky=N+E+S+W)
                self.masterList.append(self.button61)
                self.button62 = Button(master, text=r7[8], height=1, width=2, command=lambda: self.processPuzzle(self.button62))
                self.button62.grid(row=6, column=8, sticky=N+E+S+W)
                self.masterList.append(self.button62)

                # row 7 (buttons 63-71)
                self.button63 = Button(master, text=r8[0], height=1, width=2, command=lambda: self.processPuzzle(self.button63))
                self.button63.grid(row=7, column=0, sticky=N+E+S+W, padx=(20,0))
                self.masterList.append(self.button63)
                self.button64 = Button(master, text=r8[1], height=1, width=2, command=lambda: self.processPuzzle(self.button64))
                self.button64.grid(row=7, column=1, sticky=N+E+S+W)
                self.masterList.append(self.button64)
                self.button65 = Button(master, text=r8[2], height=1, width=2, command=lambda: self.processPuzzle(self.button65))
                self.button65.grid(row=7, column=2, sticky=N+E+S+W)
                self.masterList.append(self.button65)
                self.button66 = Button(master, text=r8[3], height=1, width=2, command=lambda: self.processPuzzle(self.button66))
                self.button66.grid(row=7, column=3, sticky=N+E+S+W)
                self.masterList.append(self.button66)
                self.button67 = Button(master, text=r8[4], height=1, width=2, command=lambda: self.processPuzzle(self.button67))
                self.button67.grid(row=7, column=4, sticky=N+E+S+W)
                self.masterList.append(self.button67)
                self.button68 = Button(master, text=r8[5], height=1, width=2, command=lambda: self.processPuzzle(self.button68))
                self.button68.grid(row=7, column=5, sticky=N+E+S+W)
                self.masterList.append(self.button68)
                self.button69 = Button(master, text=r8[6], height=1, width=2, command=lambda: self.processPuzzle(self.button69))
                self.button69.grid(row=7, column=6, sticky=N+E+S+W)
                self.masterList.append(self.button69)
                self.button70 = Button(master, text=r8[7], height=1, width=2, command=lambda: self.processPuzzle(self.button70))
                self.button70.grid(row=7, column=7, sticky=N+E+S+W)
                self.masterList.append(self.button70)
                self.button71 = Button(master, text=r8[8], height=1, width=2, command=lambda: self.processPuzzle(self.button71))
                self.button71.grid(row=7, column=8, sticky=N+E+S+W)
                self.masterList.append(self.button71)

                # row 8 (buttons 72-80)
                self.button72 = Button(master, text=r9[0], height=1, width=2, command=lambda: self.processPuzzle(self.button72))
                self.button72.grid(row=8, column=0, sticky=N+E+S+W, pady=(0,20), padx=(20,0))
                self.masterList.append(self.button72)
                self.button73 = Button(master, text=r9[1], height=1, width=2, command=lambda: self.processPuzzle(self.button73))
                self.button73.grid(row=8, column=1, sticky=N+E+S+W, pady=(0,20))
                self.masterList.append(self.button73)
                self.button74 = Button(master, text=r9[2], height=1, width=2, command=lambda: self.processPuzzle(self.button74))
                self.button74.grid(row=8, column=2, sticky=N+E+S+W, pady=(0,20))
                self.masterList.append(self.button74)
                self.button75 = Button(master, text=r9[3], height=1, width=2, command=lambda: self.processPuzzle(self.button75))
                self.button75.grid(row=8, column=3, sticky=N+E+S+W, pady=(0,20))
                self.masterList.append(self.button75)
                self.button76 = Button(master, text=r9[4], height=1, width=2, command=lambda: self.processPuzzle(self.button76))
                self.button76.grid(row=8, column=4, sticky=N+E+S+W, pady=(0,20))
                self.masterList.append(self.button76)
                self.button77 = Button(master, text=r9[5], height=1, width=2, command=lambda: self.processPuzzle(self.button77))
                self.button77.grid(row=8, column=5, sticky=N+E+S+W, pady=(0,20))
                self.masterList.append(self.button77)
                self.button78 = Button(master, text=r9[6], height=1, width=2, command=lambda: self.processPuzzle(self.button78))
                self.button78.grid(row=8, column=6, sticky=N+E+S+W, pady=(0,20))
                self.masterList.append(self.button78)
                self.button79 = Button(master, text=r9[7], height=1, width=2, command=lambda: self.processPuzzle(self.button79))
                self.button79.grid(row=8, column=7, sticky=N+E+S+W, pady=(0,20))
                self.masterList.append(self.button79)
                self.button80 = Button(master, text=r9[8], height=1, width=2, command=lambda: self.processPuzzle(self.button80))
                self.button80.grid(row=8, column=8, sticky=N+E+S+W, pady=(0,20))
                self.masterList.append(self.button80)

                # numpad buttons placed in 3x3 grid on right of interface
                self.numpad1 = Button(master, text="1", height=1, width=2, command=lambda: self.processNumpad(self.numpad1))
                self.numpad1.grid(row=5, column=9, padx=(50,0))
                self.numpad2 = Button(master, text="2", height=1, width=2, command=lambda: self.processNumpad(self.numpad2))
                self.numpad2.grid(row=5, column=10)
                self.numpad3 = Button(master, text="3", height=1, width=2, command=lambda: self.processNumpad(self.numpad3))
                self.numpad3.grid(row=5, column=11, padx=(0,20))
                self.numpad4 = Button(master, text="4", height=1, width=2, command=lambda: self.processNumpad(self.numpad4))
                self.numpad4.grid(row=4, column=9, padx=(50,0))
                self.numpad5 = Button(master, text="5", height=1, width=2, command=lambda: self.processNumpad(self.numpad5))
                self.numpad5.grid(row=4, column=10)
                self.numpad6 = Button(master, text="6", height=1, width=2, command=lambda: self.processNumpad(self.numpad6))
                self.numpad6.grid(row=4, column=11, padx=(0,20))
                self.numpad7 = Button(master, text="7", height=1, width=2, command=lambda: self.processNumpad(self.numpad7))
                self.numpad7.grid(row=3, column=9, padx=(50,0))
                self.numpad8 = Button(master, text="8", height=1, width=2, command=lambda: self.processNumpad(self.numpad8))
                self.numpad8.grid(row=3, column=10)
                self.numpad9 = Button(master, text="9", height=1, width=2, command=lambda: self.processNumpad(self.numpad9))
                self.numpad9.grid(row=3, column=11, padx=(0,20))
                self.numpadClear = Button(master, text="Clear", height=1, width=2, command=lambda: self.processNumpad(self.numpadClear))
                self.numpadClear.grid(row=6, column = 10, columnspan=2, sticky=W+E, padx=(0,20))

                # button for requesting puzzle check
                self.checkButton = Button(master, text="Check", height=1, width=2, command=lambda: self.checkPuzzle())
                self.checkButton.grid(row=0, column=10, columnspan=2, sticky=W+E, padx=(0,20), pady=(20,0))
                        
        # process function for puzzle buttons, allows user to select a box to edit
        def processPuzzle(self, pButton):
                global defaultColor
                if self.selectedButton == None:
                        pass
                else:
                        self.selectedButton.config(bg=defaultColor)
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

        # sets buttons with puzzle clues in them to disabled
        # prevents user from changing numbers pre-set by the puzzle
        def disableClueButtons(self):
                for b in self.masterList:
                        if (b['text'] == ""):
                                pass
                        else:
                                b.config(state="disabled")

        # checks to see if the users answer to the puzzle is correct
        def checkPuzzle(self):
                global DEBUG
                # creates a new list for the player's current board
                # will change the list every time the player tries to check the puzzle
                currentSolution = []
                # the entire loop is in a try-except statement because it will give you a value error if one of the inputs is blank
                # the error occurs because you cant change '' into an integer, so python doesn't like that
                try:
                        for b in self.masterList:
                                currentSolution.append(int(b['text']))
                        if DEBUG == True:
                                print currentSolution
                        # checks to see if the user's solution is matched to the master solution
                        if currentSolution == solution:
                                self.labelStatus.config(text="You win!")
                                self.victoryPopup()
                        else:
                                self.labelStatus.config(text="Incorrect solution")
                # this is the messaged displayed if the user does not have all the values filled out
                except ValueError:
                        self.labelStatus.config(text="Incomplete puzzle")

        # creates popup window if user wins
        def victoryPopup(self):
                victory = Toplevel()
                victory.title("You Win")
                labelVictory = Label(victory, text="You win!", font=("TkDefaultFont",48))
                labelVictory.pack()

### Difficulty Function ###
# difficulty setter
def difficulty(d, r1, r2, r3, r4, r5, r6, r7, r8, r9):
        i = 0
        while (i <> d):
                # for which row to pick
                j = randint(1, 9)
                # for the index
                k = randint(0, 8)
                # selects the row
                if (j == 1):
                        # only if this element has not already been picked
                        if (r1[k] <> 0):
                                # sets that position equal to 0
                                # and increments counter because the number was removed
                                r1[k] = ''
                                i += 1
                if (j == 2):
                        # the same as for the 1st row
                        if (r2[k] <> 0):
                                r2[k] = ''
                                i += 1
                if (j == 3):
                        # the same as for the 1st row
                        if (r3[k] <> 0):
                                r3[k] = ''
                                i += 1
                if (j == 4):
                        # the same as for the 1st row
                        if (r4[k] <> 0):
                                r4[k] = ''
                                i += 1
                if (j == 5):
                        # the same as for the 1st row
                        if (r5[k] <> 0):
                                r5[k] = ''
                                i += 1
                if (j == 6):
                        # the same as for the 1st row
                        if (r6[k] <> 0):
                                r6[k] = ''
                                i += 1
                if (j == 7):
                        # the same as for the 1st row
                        if (r7[k] <> 0):
                                r7[k] = ''
                                i += 1
                if (j == 8):
                        # the same as for the 1st row
                        if (r8[k] <> 0):
                                r8[k] = ''
                                i += 1
                if (j == 9):
                        # the same as for the 1st row
                        if (r9[k] <> 0):
                                r9[k] = ''
                                i += 1
        return r1, r2, r3, r4, r5, r6, r7, r8, r9

### Main Program ###
# creates the title window
window = Tk()
window.title("Sudoku")
app = SudokuMenu(window)
window.mainloop()
difficulty(d, r1, r2, r3, r4, r5, r6, r7, r8, r9)
window = None
# creates the puzzle window
window = Tk()
window.title("Sudoku")
app = SudokuPuzzle(window)
app.disableClueButtons()
window.mainloop()

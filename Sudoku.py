from random import randint

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

################################################# calls the Sudoku function #####################################################
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
print r1
print r2
print r3
print r4
print r5
print r6
print r7
print r8
print r9

# creates the list of solutions, to checi puzzle against later
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

def chooseDifficulty():
    # gets difficulty level from user
    diff = str(raw_input("What level of difficulty would you like(Easy, Medium, Hard): "))
    # uses difficulty level to determine how many numbers will be taken out
    if (diff == "Easy"):
        d = randint(49, 55)
        return d
    elif (diff == "Medium"):
        d = randint(40, 48)
        return d
    elif (diff == "Hard"):
        d = randint(56, 64)
        return d
    else:
        chooseDifficulty()
        
d = chooseDifficulty()
# will pick a random row and index in that row, and replace that
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
            r1[k] = 0
            i += 1
    if (j == 2):
        # the same as for the 1st row
        if (r2[k] <> 0):
            r2[k] = 0
            i += 1
    if (j == 3):
        # the same as for the 1st row
        if (r3[k] <> 0):
            r3[k] = 0
            i += 1
    if (j == 4):
        # the same as for the 1st row
        if (r4[k] <> 0):
            r4[k] = 0
            i += 1
    if (j == 5):
        # the same as for the 1st row
        if (r5[k] <> 0):
            r5[k] = 0
            i += 1
    if (j == 6):
        # the same as for the 1st row
        if (r6[k] <> 0):
            r6[k] = 0
            i += 1
    if (j == 7):
        # the same as for the 1st row
        if (r7[k] <> 0):
            r7[k] = 0
            i += 1
    if (j == 8):
        # the same as for the 1st row
        if (r8[k] <> 0):
            r8[k] = 0
            i += 1
    if (j == 9):
        # the same as for the 1st row
        if (r9[k] <> 0):
            r9[k] = 0
            i += 1
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

        

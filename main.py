import pygame,sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((360,400))

pygame.display.set_caption('Bogogo the Sudoku Chimpo')

class Square(object):
    def __init__(self):
        self.value = 0
        self.box = 0
        self.row = 0
        self.column = 0
        self.notes = [1,2,3,4,5,6,7,8,9]

    def Post(self):
        """
        Used to easily show the index location inside the sudoku array
        """
        for i in range(81):
            if sudoku[i] == self:
                value = i
        return(value)


def Text(n,x,y):
    """
    Takes an integer and x, y cords and displays it on screen.
    """
    n = str(n)
    if n != '0':
        fontObj = pygame.font.Font('freesansbold.ttf', 30)
        lineA = fontObj.render(n, True, BLACK)
        textRectObjA = lineA.get_rect()
        textRectObjA.center = (x,y)
        DISPLAYSURF.blit(lineA, textRectObjA)

def Increase(ray,amount):
    """
    Increases each value in the given array by specified amount.
    Used for assigning box values.
    """
    newray = []
    for i in ray:
        newray.append(i + amount)
    return(newray)

def Save():
    """
    User inputs a new text file name and saves each square value into a text file.
    """
    out = ''
    for i in sudoku:
        out = out + str(i.value)
    valid = False

    while valid == False:
        fname = input('Please enter file name (incude ".txt"!)')
        extension = ''
        if len(fname) >5:
            x = -4
            for i in range(4):
                extension = extension + (fname[x])
                x += 1
            if extension == '.txt':
                valid = True
    fname = 'sudokus/' + fname
    file = open(fname,'w')
    file.write(out)
    file.close()

def Load():
    """
    User inputs file name and load specified Sudoku. Called by pressing Ctrl + S.
    """
    valid = False

    while valid == False:
        fname = input('Please enter file name (incude ".txt"!')
        extension = ''
        if len(fname) >5:
            x = -4
            for i in range(4):
                extension = extension + (fname[x])
                x += 1
            if extension == '.txt':
                valid = True
        print(fname)
    fname = 'sudokus/' + fname
    try:
        file = open(fname)
        values = file.readline()
        print(values)
        file.close()
    except:
        print('File Not Found!')

    for i in range(81):
        sudoku[i].value = int(values[i])
    print('Sudoku Loaded.')
    print(sudoku)



# Creates 81 Square objects and assigns x, y cords
sudoku =[]

x = 0
y = 0
for i in range(81):
    z = Square()
    z.x = x
    z.y = y
    if i < 19:
        print(i+1,x,y)
    sudoku.append(z)
    x += 40
    if 320 < x:
        x = 0
        y += 40

# Assign Row and Column values for each square.
x = 0
for i in range(9):
    for j in range(9):
        sudoku[x].column = j + 1
        sudoku[x].row = i + 1
        x += 1

# Assign Box value for square.
x = 0
boxcords =[1,1,1,2,2,2,3,3,3,]
for i in range(3):
    for i in range(3):
        y = 0

        for i in range(9):
            sudoku[x].box = boxcords[y]
            x += 1
            y += 1
    boxcords = Increase(boxcords,3)

# Define some values used in the loop, and set the FPS limit.
selected = 0

solve = False
ctrl = False


# Define some colors and load some pretty pictures.
BLACK=(  0,  0,  0)
GREEN=(182,255,  0)

block = pygame.image.load('square.png')
bar = pygame.image.load('bar.png')
whitebox = pygame.image.load('selected.png')

fpsClock = pygame.time.Clock()
FPS=60

# Main Program Loop.

while True:
#               Check for events:                                              #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            MX = pygame.mouse.get_pos()[0]
            MY = pygame.mouse.get_pos()[1]
# Click a Square to retrieve information
            for i in sudoku:
                if i.x <= MX and MX <= i.x + 40 and i.y <= MY and MY <= i.y + 40:
                    selected = i.Post()
                    print('Value:',i.value)
                    print(i.notes)
                    print('Box:',i.box)
                    print('Row:',i.row)
                    print('Column:',i.column)

            if 142 <= MX and MX <= 242 and 367 <= MY and MY <= 394:
                solve = True

        elif event.type== KEYDOWN:
            print(event.key)
# Delete Key
            if event.key == 127:
                for i in sudoku:
                    i.value = 0
                selected = 0

# Number Keys (Including Number Pad)
            if selected > 80:
                selected = 0
            if event.key == 256 or event.key ==48:
                sudoku[selected].value = 0
                selected += 1
            if event.key == 257 or event.key ==49:
                sudoku[selected].value = 1
                selected += 1
            if event.key == 258 or event.key ==50:
                sudoku[selected].value = 2
                selected += 1
            if event.key == 259 or event.key ==51:
                sudoku[selected].value = 3
                selected += 1
            if event.key == 260 or event.key ==52:
                sudoku[selected].value = 4
                selected += 1
            if event.key == 261 or event.key ==53:
                sudoku[selected].value = 5
                selected += 1
            if event.key == 262 or event.key ==54:
                sudoku[selected].value = 6
                selected += 1
            if event.key == 263 or event.key ==55:
                sudoku[selected].value = 7
                selected += 1
            if event.key == 264 or event.key ==56:
                sudoku[selected].value = 8
                selected += 1
            if event.key == 265 or event.key ==57:
                sudoku[selected].value = 9
                selected += 1

# Arrow Keys
            if event.key == 273:
                selected -= 9
            if event.key == 274:
                selected += 9
            if event.key == 276:
                selected -= 1
            if event.key == 275:
                selected += 1

# Ctrl Key
            if event.key == 306:
                ctrl = True
# S, L Keys
            if event.key == 115:
                if ctrl == True:
                    Save()

            if event.key == 108:
                if ctrl == True:
                    Load()
# Space Key
            if event.key == 36:
                solve = False

        elif event.type== KEYUP:
# Ctrl
            if event.key == 306:
                ctrl = False

#               Update Squares.
#
    if solve == True:
        for i in sudoku:
            if len(i.notes) == 1:
                i.value = i.notes[0]
            if i.value != 0:
# Checks to see if there is an error in the puzzle.
                i.notes = [i.value]
                for j in sudoku:
                    if i != j:
                        if i.value == j.value:
#  Prints out information about conflicting squares.
                            if i.row == j.row:
                                print(i.value, 'IN ROW:',i.row,'|', j.row)
                            if i.column == j.column:
                                print(i.value, 'IN Column:',i.column,'|', j.column)
                            if i.box == j.box:
                                print(i.value, 'IN BOX:',i.box,'|', j.box)

            for j in sudoku:
                if i != j:
                    if i.row == j.row or i.column == j.column or i.box == j.box:
                        for k in j.notes:
                            if k == i.value:
                                j.notes.remove(i.value)
##                    if i.box == j.box:
##                        if len(i.notes)==2:
##                            if i.notes == j.notes:
##                                for k in sudoku:
##                                    if i.box == k.box:
##                                        for l in k.notes:
##                                            if l == i.notes[0]:
##                                                k.notes.remove(i.notes[0])
##                                            if l == i.notes[1]:
##                                                k.notes.remove(i.notes[1])


    fpsClock.tick(FPS)

#               Display Screen:                                                #
    DISPLAYSURF.fill(GREEN)

# 9 x 9 Grid
    y = 0
    for i in range(9):
        x = 0
        for i in range(9):
            DISPLAYSURF.blit(block,(x,y))
            x += 40
        y += 40

# Solve button and selected square.
    DISPLAYSURF.blit(bar,(0,360))
    DISPLAYSURF.blit(whitebox,(sudoku[selected].x, sudoku[selected].y))

# Displays Number value of each square.
    x = 20
    y = 22
    for i in sudoku:
        Text(i.value,x,y)
        x += 40
        if 360 < x:
            y += 40
            x = 20

    pygame.display.update()


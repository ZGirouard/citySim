#citysim.py
#Written by Zach Girouard
import time
import numpy as np
import random
import os

#Declare variables
ESC = "\x1b"
turn = 0
structures = ['house', 'store', 'river', 'zoo', 'school']
coord_x, coord_y = 0, 0
revenue = 0
population = 0
zooExists = False
meteorStrike = False
stampedeRun = False
canBuild = True
size = 'x'

#Initial prompt. Get's user input for city size and creates a size by size array for that input.
print('Welcome to CitySim!')
time.sleep(0.5)
print('You will have 15 turns to attain the highest possible population and revenue you can!')
time.sleep(0.5)
while size.isdigit() == False:
    print()
    size = (input("Enter a city size (For best experience, a size of 15 or higher is recommended): "))

size = int(size)    
arr = np.full((size,size),'.')


#Prints a color array without brackets and commas
def printArray(size):
    os.system('cls')
    for x in range(size):
        for y in range(size):
            if arr[y,x] == '.':
                print(ESC + '[32;1m' + arr[y,x], end='')
            if arr[y,x] == 'Z':
                print(ESC + '[36;1m' + arr[y,x], end='')
            if arr[y,x] == 'H':
                print(ESC + '[35;1m' + arr[y,x], end='')
            if arr[y,x] == '~':
                print(ESC + '[34;1m' + arr[y,x], end='')
            if arr[y,x] == '$':
                print(ESC + '[33;1m' + arr[y,x], end='')
            if arr[y,x] == 'S':
                print(ESC + '[37;1m' + arr[y,x], end='')
            if arr[y,x] == 'X':
                print(ESC + '[31;1m' + arr[y,x], end='')
            if arr[y,x] == 'R':
                print(ESC + '[37;1m' + arr[y,x], end='')
            if arr[y,x] == '*':
                print(ESC + '[37m' + arr[y,x], end='')
        print(ESC + '[0m')

#Chooses a random structure for the user to build
def randStructure():
    global structure
    structure = random.randint(0,4)
    print("Your next structure is a:", structures[structure])
    print()

#Will call an individual function for each value of the random structure
def chooseStructure():
    if structure == 0:
        makeHouse()
    elif structure == 1:
        makeStore()
    elif structure == 2:
        makeRiver()
    elif structure == 3:
        makeZoo()
    elif structure == 4:
        makeSchool()
    
#Creates a 2 x 2 school in the city denoted with 'S' and updates revenue and population
def makeSchool():
    if ((coord_x + 1) >= size) or ((coord_y + 1) >= size):
        outOfBounds()

    elif (arr[coord_x, coord_y] == 'R') or (arr[coord_x, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x + 1, coord_y] == 'R') or (arr[coord_x, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x, coord_y + 1] == 'R') or (arr[coord_x, coord_y + 1] == '*'):
        disasterBuild()

    elif (arr[coord_x + 1, coord_y + 1] == 'R') or (arr[coord_x + 1, coord_y + 1] == '*'):
        disasterBuild()

    else:
        global revenue
        global population
        global turn
        revenue += 400
        population += 40
        
        if arr[coord_x, coord_y] == '.':
            arr[coord_x, coord_y] = 'S'
        else:
            arr[coord_x, coord_y] = 'X'
            revenue -= 50
            population -= 5

        if arr[coord_x + 1, coord_y] == '.':
            arr[coord_x + 1, coord_y] = 'S'
        else:
            arr[coord_x + 1, coord_y] = 'X'
            revenue -= 50
            population -= 5

        if arr[coord_x, coord_y + 1] == '.':
            arr[coord_x, coord_y + 1] = 'S'
        else:
            arr[coord_x, coord_y + 1] = 'X'
            revenue -= 50
            population -= 5

        if arr[coord_x + 1, coord_y + 1] == '.':
            arr[coord_x + 1, coord_y + 1] = 'S'
        else:
            arr[coord_x + 1, coord_y + 1] = 'X'
            revenue -= 50
            population -= 5

        time.sleep(0.5)
        turn += 1

#Creates a 2 x 2 house in the array denoted with 'H' and updates revenue and population
def makeHouse():
    if ((coord_x + 1) >= size) or ((coord_y + 1) >= size):
        outOfBounds()

    elif (arr[coord_x, coord_y] == 'R') or (arr[coord_x, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x + 1, coord_y] == 'R') or (arr[coord_x, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x, coord_y + 1] == 'R') or (arr[coord_x, coord_y + 1] == '*'):
        disasterBuild()

    elif (arr[coord_x + 1, coord_y + 1] == 'R') or (arr[coord_x + 1, coord_y + 1] == '*'):
        disasterBuild()

    else:
        global revenue
        global population
        global turn
        revenue += 100
        population += 100
      
        if arr[coord_x, coord_y] == '.':
            arr[coord_x, coord_y] = 'H'
        else:
            arr[coord_x, coord_y] = 'X'
            revenue -= 10
            population -= 10

        if arr[coord_x + 1, coord_y] == '.':
            arr[coord_x + 1, coord_y] = 'H'
        else:
            arr[coord_x + 1, coord_y] = 'X'
            revenue -= 10
            population -= 10

        if arr[coord_x, coord_y + 1] == '.':
            arr[coord_x, coord_y + 1] = 'H'
        else:
            arr[coord_x, coord_y + 1] = 'X'
            revenue -= 10
            population -= 10

        if arr[coord_x + 1, coord_y + 1] == '.':
            arr[coord_x + 1, coord_y + 1] = 'H'
        else:
            arr[coord_x + 1, coord_y + 1] = 'X'
            revenue -= 10
            population -= 10

        time.sleep(0.5)
        turn += 1

#Creates a 1 x 3 river on the array denoted with '~' and updates population
def makeRiver():
    if ((coord_x + 2) >= size) or (coord_y >= size):
        outOfBounds()

    elif (arr[coord_x, coord_y] == 'R') or (arr[coord_x, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x + 1, coord_y] == 'R') or (arr[coord_x, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x + 2, coord_y] == 'R') or (arr[coord_x + 2, coord_y] == '*'):
        disasterBuild()

    else:    
        global population
        global turn
        population += 50
        
        if arr[coord_x, coord_y] == '.':
            arr[coord_x, coord_y] = '~'
        else:
            arr[coord_x, coord_y] = 'X'
            population -= 10

        if arr[coord_x + 1, coord_y] == '.':
            arr[coord_x + 1, coord_y] = '~'
        else:
            arr[coord_x + 1, coord_y] = 'X'
            population -= 10

        if arr[coord_x + 2, coord_y] == '.':
            arr[coord_x + 2, coord_y] = '~'
        else:
            arr[coord_x + 1, coord_y + 1] = 'X'
            population -= 10

        time.sleep(0.5)
        turn += 1

#Creates a stored in the form of a 2 x 1 and a connected 1 x 1 denoted with '$' and upadtes population and revenue
def makeStore():
    if ((coord_x + 1) >= size) or ((coord_y + 1) >= size):
        outOfBounds()

    elif (arr[coord_x, coord_y] == 'R') or (arr[coord_x, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x + 1, coord_y] == 'R') or (arr[coord_x + 1, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x + 1, coord_y + 1] == 'R') or (arr[coord_x + 1, coord_y + 1] == '*'):
        disasterBuild()

    else:    
        global revenue
        global population
        global turn
        revenue += 600
        population += 75

        if arr[coord_x, coord_y] == '.':
            arr[coord_x, coord_y] = '$'
        else:
            arr[coord_x, coord_y] = 'X'
            revenue -= 150
            population -= 15

        if arr[coord_x + 1, coord_y] == '.':
            arr[coord_x + 1, coord_y] = '$'
        else:
            arr[coord_x + 1, coord_y] = 'X'
            revenue -= 150
            population -= 15

        if arr[coord_x + 1, coord_y + 1] == '.':
            arr[coord_x + 1, coord_y + 1] = '$'
        else:
            arr[coord_x + 1, coord_y + 1] = 'X'
            revenue -= 150
            population -= 15

        time.sleep(0.5)
        turn += 1

#Creates a 2 x 3 zoo denoted with 'Z' and updates population and revenue
def makeZoo():
    if ((coord_x + 2) >= size) or ((coord_y + 1) >= size):
        outOfBounds()
   
    elif (arr[coord_x, coord_y] == 'R') or (arr[coord_x, coord_y] == '*'):
        disasterBuild()
    
    elif (arr[coord_x + 1, coord_y] == 'R') or (arr[coord_x + 1, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x + 2, coord_y] == 'R') or (arr[coord_x + 2, coord_y] == '*'):
        disasterBuild()

    elif (arr[coord_x, coord_y + 1] == 'R') or (arr[coord_x, coord_y + 1] == '*'):
        disasterBuild()

    elif (arr[coord_x + 1, coord_y + 1] == 'R') or (arr[coord_x + 1, coord_y + 1] == '*'):
        disasterBuild()

    elif (arr[coord_x + 2, coord_y + 1] == 'R') or (arr[coord_x + 2, coord_y + 1] == '*'):
        disasterBuild()

    else:
        global revenue
        global population
        global zooExists
        global turn
        zooExists = True
        revenue += 550
        population += 25

        if arr[coord_x, coord_y] == '.':
            arr[coord_x, coord_y] = 'Z'
        else:
            arr[coord_x, coord_y] = 'X'
            revenue -= 75
            population -= 4

        if arr[coord_x + 1, coord_y] == '.':
            arr[coord_x + 1, coord_y] = 'Z'
        else:
            arr[coord_x + 1, coord_y] = 'X'
            revenue -= 75
            population -= 4

        if arr[coord_x + 2, coord_y] == '.':
            arr[coord_x + 2, coord_y] = 'Z'
        else:
            arr[coord_x + 2, coord_y] = 'X'
            revenue -= 75
            population -= 4

        if arr[coord_x, coord_y + 1] == '.':
            arr[coord_x, coord_y + 1] = 'Z'
        else:
            arr[coord_x, coord_y + 1] = 'X'
            revenue -= 75
            population -= 4

        if arr[coord_x + 1, coord_y + 1] == '.':
            arr[coord_x + 1, coord_y + 1] = 'Z'
        else:
            arr[coord_x + 1, coord_y + 1] = 'X'
            revenue -= 75
            population -= 4
        
        if arr[coord_x + 2, coord_y + 1] == '.':
            arr[coord_x + 2, coord_y + 1] = 'Z'
        else:
            arr[coord_x + 2, coord_y + 1] = 'X'
            revenue -= 75
            population -= 4

        time.sleep(0.5)
        turn += 1

#Prompts the user their placement is out of the city bounds
def outOfBounds():
    os.system('cls')
    print()
    print('Coordinates out of bounds for desired structure. Try again.')
    time.sleep(0.5)
    os.system('cls')

#Gives the user their current revenue and population
def cityStats():
    randStructure()
    global revenue
    global population
    print('Current Revenue: $' + str(revenue))
    print('Current Population: ' + str(population) + ' people.')

#Will call either the meteor or stampede function, will clear the array after the disaster, and will end the game after 15 turns
def disaster():
    global zooExists
    global meteorStrike
    global stampedeRun
    if turn == 5 and zooExists == True:
        stampede()
    if turn == 8 and stampedeRun == True:
        os.system('cls')
        print()
        print('The stampede has subsided.')
        time.sleep(1)
        for x in range(size):
            for y in range(size):
                if arr[y,x] == 'R':
                    arr[y,x] = '.'
                    time.sleep(0.1)
                    os.system('cls')
                    printArray(size)

        os.system('cls')
        printArray(size)

    if turn == 5 and zooExists == False:
        meteor()
    if turn == 8 and meteorStrike == True:
        print()
        print('The crator has been filled in.')
        time.sleep(1)
        os.system('cls')
        for x in range(size):
            for y in range(size):
                if arr[y,x] == '*':
                    arr[y,x] = '.'
                    time.sleep(0.1)
                    os.system('cls')
                    printArray(size)
    if turn == 15:
        printArray(size)
        print('Your final population is: ' + str(population) + ' people.')
        print('Your final revenue is: $' + str(revenue))
        exit()

#Will create a top-left to bottom-right animation of a stampede if the user has a zoo in their first 5 turns
def stampede():
   os.system('cls')
   print()
   print('A herd of rhino escape from your zoo and stampede across the city.')
   time.sleep(1)
   global stampedeRun
   stampedeRun = True
   for i in range(size - 1):
       arr[i, i] = 'R'
       time.sleep(0.1)
       arr[i + 1, i] = 'R'
       time.sleep(0.1)
       arr[i, i + 1] = 'R'
       time.sleep(0.1)
       os.system('cls')
       printArray(size)
   arr[size - 1, size - 1] = 'R'
   printArray(size)

#Will create a circular creator from a meteor if the user does not have a zoo in their first five turns
def meteor():
    os.system('cls')
    print()
    print('A meteor comes crashing in from the sky.')
    time.sleep(1)
    global meteorStrike
    meteorStrike = True
    global site
    site = random.randint(4, size - 5)
    for i in range(4):
        arr[site + i, site + i] = '*'
        arr[site + i, site] = '*'
        arr[site, site + i] = '*'
        arr[site - i, site] = '*'
        arr[site, site - i] = '*'
        arr[site - i, site - i] = '*'
        arr[site + i, site - i] = '*'
        arr[site - i, site + i] = '*'
        time.sleep(0.1)
        os.system('cls')
        printArray(size)

#Prompts the user they can't place a structure on top of the disaster
def disasterBuild():
    os.system('cls')
    print()
    print("The current disaster prevents you from building there.")
    time.sleep(1)
    os.system('cls')

#Active while the user is playing the game        
while turn < 15:
    printArray(size)
    cityStats()
    try:
        coord_y, coord_x = [int(i) for i in input("Pick a coordiante to build!" + "\n" + "[Format:Y X]" + "\n").split()]
    except:
        print("Not correct input.")
        continue
    chooseStructure()
    disaster()

#Clears color for the terminal at the end of the program
print(ESC + '[37m' + '\n')
print(ESC + '[0m' + '\n')

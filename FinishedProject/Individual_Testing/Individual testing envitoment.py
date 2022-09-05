from openpyxl import *


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
data = [1] #this is used as passing by ref dosent work with python

def combine(var1,var2):
    var1, var2= str(var1),str(var2)
    newVar = (var1+var2)
    NewVar = str(newVar)        #combines two varaibles into a singular word
    return NewVar

def nextletter(word,Nextpointer):
    array = list(word)
    array[0] = alphabet[Nextpointer]
    var = combine(array[0],array[1])

    data[0] += 1
    word = [var]

    print(word)
    return word


def nextNumber(word):
    array = list(word)
    temp = array[1]
    temp = int(temp) + 3
    array[1] = str(temp)
    nextPos = combine(array[0],array[1])
    print(nextPos)
    return nextPos

def everyupdate(player,Nextpointer):
    wb = load_workbook('Rocket_Database backup 14.12.21.xlsx')
    database = wb.active

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    Xpos = 'C6'
    Ypos = 'C7'
    Zpos = 'C8'

    Nextpointer = 1

    X = player.x
    Y = player.y
    Z = player.z

    if alphabet[Nextpointer] == 25:
        Nextpointer = 0

    database[Xpos] = X
    database[Ypos] = Y
    database[Zpos] = Z                            #adds the data to the databse which then gets ready to update
                                                  #the posistion to the next posistion
    Xpos = nextNumber(Xpos)
    Ypos = nextNumber(Ypos)
    Zpos = nextNumber(Zpos)

    wb.save('Rocket_Database backup 14.12.21.xlsx') # saves the changes
















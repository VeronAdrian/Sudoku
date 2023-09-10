#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adrian
#
# Created:     10/09/2023
# Copyright:   (c) Adrian 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

table = [[], [], [], [], [], [], [], [], []];

def loadTable():
    index = 0
    for i in range(1,82,1):
        table[index].append(0)
        if(len(table[index])==9):
            index+=1

def sudoku():
    for lin in table:
        for i in range(0,9,1):
            print(lin.count(i))

def validateLine(line):
    return;

def validateCol(col):
    return;

def main():
    loadTable()
    sudoku()
    pass

if __name__ == '__main__':
    main()
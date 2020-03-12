import base_game
import xlrd

'''The purpose of this file is to load a level from a given xlsx file and convert the contents of the file into a playable mario level
    We use the xlrd library and pull from base_game in order to accomplish this'''

#Define basic variables: Level is where we store the strings that comprise the level; path is the default file that will be loaded; workbook/worksheet are the working xlsx
#files that we will read from
level = []
path = "mario.xlsx"
fout = open('testing.txt', "w") #I test to make sure the level is stored into the list appropriately by outputting the contents of level into a separate txt file
workbook = xlrd.open_workbook(path)
workSheet = workbook.sheet_by_index(0)

#A nested for loop that creates the level.  Append a string at each new line of the xlsx file so that we can store the contents line by line, forming the level
for x in range(workSheet.nrows):
    level.append('')
    for y in range(workSheet.ncols):
        if(str(workSheet.cell(x, y).value) == ''):
            level[x] = level[x] + ' '
        elif(type(workSheet.cell(x, y).value) == float):
            level[x] = level[x] + str(int(workSheet.cell(x, y).value))
        else:
            level[x] = level[x] + str(workSheet.cell(x, y).value)


#Test code that writes the contents of the array to a separate txt file
for x in range(len(level)):
    for y in range(len(level[x])):
        fout.write(level[x][y])
    fout.write('\n')

fout.close()
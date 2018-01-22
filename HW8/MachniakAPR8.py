#############################################################################
### 1) HW 8: Making an Output File
### 2) Anthony Machniak
### 3) 11/2/17
### 4) This file will create a list and output a data file from that list
#############################################################################

def main():
    nameList = readFile()
    printNames(nameList)

    nameList.sort()
    printNames(nameList)

    newFile = open('sortedNames.txt', 'w')
    for name in nameList:
        newFile.write(name + '\n')
    
    searchFunction(nameList)
    newFile.close()


def readFile():
    file = open('names.txt', 'r')
    
    nameList = []
    name = file.readline()
    
    while name != '':
        name = name.rstrip('\n')
        nameList.append(name)
        name = file.readline()
    
    file.close()    
    return nameList
    

def printNames(nameList):
    for name in nameList:
        print(name)

    
def searchFunction(nameList):
    anotherSearch = 'Y'

    while anotherSearch == 'Y' or anotherSearch =='y':
        firstName = str(input('\n' + 'Please enter their first name: '))
        lastName = str(input('Please enter their last name: '))
        fullName = lastName + ', ' + firstName
        firstThenLast = firstName + ' ' + lastName

        if fullName in nameList:
            print(firstThenLast, 'was found in the list.')
            print(nameList.index(fullName))
            print('Just a reminder: Computer lists start at 0, not 1')
        else:
            print(firstThenLast, 'was not found in the list.')
    
        print('\n' + 'Did you want to look for another name?')
        print("Type in 'Y' or 'y' to continue.")
        anotherSearch = input("Type in any other key to quit. ")
        

main()
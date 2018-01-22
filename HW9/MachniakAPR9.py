#############################################################################
### 1) HW 8: Making an Output File
### 2) Anthony Machniak
### 3) 11/12/17
### 4) This program takes pet data and prints it for those who entered it.
#############################################################################

import petdata

def main():
    pets = makeList()

    print("Here is the data that you entered: ")
    
    for data in pets:
        print("Name: ", data.get_name())
        print("Type: ", data.get_pet_type())
        print("Age: ", data.get_age())
        print()

def makeList():
    petList = []

    numberOfEntries = int(input("How many pets are you entering data for? "))
    
    for count in range(1, numberOfEntries + 1):
        print("Pet number " + str(count) + ":")
        
        name = input("Enter the name of your pet: ")
        petType = input("Enter the type of pet they are: ")
        age = int(input("Enter their age: "))        
        print()
        
        pet = petdata.petData(name, petType, age)
        
        petList.append(pet)
        
    return petList


main()
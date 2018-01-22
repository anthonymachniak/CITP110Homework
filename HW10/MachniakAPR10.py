##################################################################################
#### 1) Homework 10
#### 2) Anthony Machniak
#### 3) 11/19/17
#### 4) A program that keeps track of worker information for the LCC Zoo
##################################################################################

import workerGenerator

def main():
    userInput = 'Y'
    workerList = []
    
    while userInput == 'Y' or userInput == 'y':
        print("What type of employee is this person?")
        print("1) Volunteer")
        print("2) Salary Employee")
        print("3) Hourly Employee")
        option = input("Input the number that matches the employment type: ")
        while option != '1' and option != '2' and option != '3':
            print("Error: you have entered an invalid option.")
            option = input("Please enter a valid employee type: ")
            print()

        name = input("Enter the employee's name: ")
        ID = input("Enter the employee's ID: ")
        residence = input("Enter the employee's residence: ")
        
        if option == '1':
            newWorker = workerGenerator.Person(name, ID, residence)
        elif option == '2':
            pay = float(input("Enter the employee's annual salary: "))
            newWorker = workerGenerator.SalaryWorker(name, ID, residence, pay)
        elif option == '3':
            pay = float(input("Enter the employee's hourly pay rate: "))
            shift = input("Enter the employee's shift: ")
            while shift != '1' and shift != '2' and shift != '3':
                print("Error: you have entered an invalid shift.")
                shift = input("Enter the employee's shift: ")
            newWorker = workerGenerator.HourlyWorker(name, ID, residence, pay, shift)
        
        workerList.append(newWorker)
        
        print()
        print("Do you want to input another employee?")
        userInput = input("Press 'Y' or 'y' to continue. ")
        print()
    
    printList(workerList)


def printList(workerList):
    for person in workerList:
        if isinstance(person, workerGenerator.SalaryWorker):
            workerGenerator.SalaryWorker.show_employee(person)
            workerGenerator.SalaryWorker.show_pay(person)
        elif isinstance(person, workerGenerator.HourlyWorker):
            workerGenerator.HourlyWorker.show_employee(person)
            workerGenerator.HourlyWorker.show_pay(person)
        elif isinstance(person, workerGenerator.Person):
            workerGenerator.Person.show_employee(person)
            workerGenerator.Person.show_pay(person)
        else:
            name = person.get_name()
            print(name, "doesn't have a valid employee type.")
        print()    

main()
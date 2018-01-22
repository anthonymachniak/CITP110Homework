#############################################################################
### 1) HW 7: CD & DVD Sales
### 2) Anthony Machniak
### 3) 10/27/17
### 4) This program will take a text file and move the information for sales
###    into a list to generate a report.
#############################################################################

def main():
    cdPrice = 16.50
    dvdPrice = 21.75
    inFile = open('disks.txt', 'r')

    name = inFile.seek(0)
    numberOfCustomers = 0
    cdCustomers = 0
    dvdCustomers = 0
    totalPayment = 0
    fileArray = []

    while name != '':
        name = inFile.readline()
        code = inFile.readline()
        numberOfSpindles = inFile.readline()
        
        name = name.rstrip('\n')
        code = code.rstrip('\n')
        
        try:
            numberOfSpindles = int(numberOfSpindles.rstrip('\n'))
        except:
            numberOfSpindles = ''
        
        if code == 'c' or code == 'C':
            paymentDue = cdPrice * numberOfSpindles
            paymentDueString = '$' + format(paymentDue, '.2f')
            cdCustomers += 1
        elif code == 'd' or code == 'D':
            paymentDue = dvdPrice * numberOfSpindles
            paymentDueString = '$' + format(paymentDue, '.2f')
            dvdCustomers += 1
        else:
            paymentDueString = 'Invalid Code'

        numberOfCustomers += 1
        fileList = [name, code, numberOfSpindles, paymentDueString]
        fileArray.append(fileList)
        
        if paymentDue != 'Invalid Code':
            totalPayment += paymentDue
        
    #while loop goes an extra round until name = ''
    fileArray.remove(['','','', 'Invalid Code'])
    inFile.close()
    
    printTable(fileArray)
    
    print("The total number of customers who bought CDs is: ", cdCustomers)
    print("The total number of customers who bought DVDs is: ", dvdCustomers)
    print("The total sales is: ", '$' + format(totalPayment, '.2f'))


def printTable(array):
    print("|       Name       | Code | Spindles |  Payment Due  |")
    
    for item in array:
        print("|", item[0]," " * (15-len(item[0])),"|",
              item[1], "   |",
              item[2], " " * (7-len(str(item[2]))), "|",
              item[3], " " * (12-len(str(item[3]))), "|")


main()
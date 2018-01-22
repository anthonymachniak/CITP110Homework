#############################################################
## 1) HW 3: Pay Calculator
## 2) Anthony Machniak
## 3) 9/17/17
## 4) Abstract: This program calculates pay, commission, gross pay, withholdings, and net pay.
##    Inputs: Employee Name, Sales Amount, and Hours Worked
##    Processes: Hourly Pay, Commission, Gross Pay, Withholdings, Net Pay
##    Outputs: Hourly Pay, Commission, Gross Pay, Withholdings, Net Pay
#############################################################

#Global Variables
hourly_pay_rate = 7.50
commission_rate = 0.05
withholding_rate = 0.25


def main():
    display_message()
    
    employee_name = input('Employee Name: ')
    
    #Error handling for if a non-float is used in the input (example: '$')
    while True:
        try:
            sales_amount = float(input('Employee Sales Amount: '))
            break
        except ValueError:
            print('Please enter only a number for the sales amount.')
    
    #Error handling for if a non-float is used in the input
    while True:
        try:
            hours_worked = float(input('Employee Hours Worked: '))
            break
        except ValueError:
            print('Please enter only a number for the hours worked.')
            
    hourly_pay = hours_worked * hourly_pay_rate
    
    commission = sales_amount * commission_rate
    
    gross_pay = hourly_pay + commission
    
    withholding = gross_pay * withholding_rate
    
    net_pay = gross_pay - withholding
    
    results = [hourly_pay, commission, gross_pay, withholding, net_pay]
    
    display_results(results)


def display_message():
    print('This program calculates the salesperson\'s pay.')
    print('Five values are displayed:')
    print('hourly pay, commission, gross pay, withholding, and net pay.\n')


def display_results(result_list):  
    results_str = ['hourly pay', 'commission', 'gross pay', 'withholding', 'net pay']
    list_position = 0
    
    for results in result_list:
        print('The', results_str[list_position], 'amount is: $', format(results, '.2f'))
        list_position = list_position + 1
    input()


main()
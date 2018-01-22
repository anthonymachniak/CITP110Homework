class Person:
    def __init__(self, name, ID, residence):
        self.__name = name
        self.__ID = ID
        self.__residence = residence
    
    def set_name(self, name):
        self.__name = name
    
    def set_ID(self, ID):
        self.__ID = ID
    
    def set_residence(self, residence):
        self.__residence = residence
        
    def get_name(self):
        return self.__name
    
    def get_ID(self):
        return self.__ID
    
    def get_residence(self):
        return self.__residence
    
    def show_employee(self):
        print("The employee's name is: ", self.__name)
        print("The employee's ID is: ", self.__ID)
        print("The employee's residence is: ", self.__residence)
    
    def show_pay(self):
        print("This person is an unpaid volunteer.")
    
    
class SalaryWorker(Person):
    def __init__(self, name, ID, residence, pay):
        Person.__init__(self, name, ID, residence)
        self.__pay = pay
    
    def show_pay(self):
        payPeriods = 26
        biWeeklyPay = float(self.__pay)/payPeriods
        
        print("Employee annual salary is $", format(self.__pay, '.2f'))
        print("Employee bi-weekly pay is $", format(biWeeklyPay, '.2f'))


class HourlyWorker(Person):
    def __init__(self, name, ID, residence, pay, shift):
        Person.__init__(self, name, ID, residence)
        self.__pay = pay
        self.__shift = shift
    
    def show_pay(self):
        shiftTwoPremium = 0.05
        shiftThreePremium = 0.10
        
        print("Employee's base rate is $", format(self.__pay, '.2f'))
        
        if self.__shift == '1':
            print("Employee does not get a premium for working first shift.")
        elif self.__shift == '2':
            premiumRate = (shiftTwoPremium * self.__pay) + self.__pay
            print("Employee gets a " + str(shiftTwoPremium*100) + "% premium per hour for working second shift.")
            print("Employee's adjusted pay is $", format(premiumRate, '.2f'))
        else:
            premiumRate = (shiftThreePremium * self.__pay) + self.__pay
            print("Employee gets a " + str(shiftThreePremium*100) + "% premium per hour for working third shift.")
            print("Employee's adjusted pay is $", format(premiumRate, '.2f'))

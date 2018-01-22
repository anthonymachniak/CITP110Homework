#############################################################################################
#### 1) HW 5: Car Sales
#### 2) Anthony Machniak
#### 3) 9/26/17
#### 4) This program will take the number of sales and sales amount to calculate sales data.
####    Sales data includes lowest sale, highest sale, and average sale.
#############################################################################################

salesperson_list = []

def main():

    input_salesperson = 'Y'
    total_salespeople = 0

    while input_salesperson == 'Y' or input_salesperson == 'y':
        process_sales_data()
        total_salespeople += 1
        input_salesperson = input("Is there another salesperson? Put 'Y' for yes and 'N' for no. ")
    
    if total_salespeople == 1:
        print("There was 1 salesperson processed.")
        print("Their name was: ")
        for name in salesperson_list:
            print(name)
    else:
        print("There were", total_salespeople, "salespeople processed.")
    
        salesperson_list.sort()
        print("Here are their names: ")
        for name in salesperson_list:
            print(name)


def process_sales_data():
    name = input("Enter the salesperson's name: ")
    salesperson_list.append(name)

    first_sale = sales_input()
    
    total_sales = first_sale
    highest_sale = first_sale
    lowest_sale = first_sale
    
    number_of_sales = int(input("How many sales did they make? "))
    for number_of_sales in range(2, number_of_sales + 1):
        
        current_sale = sales_input()
        
        total_sales += current_sale
        
        if current_sale > highest_sale:
            highest_sale = current_sale
        
        elif current_sale < lowest_sale:
            lowest_sale = current_sale
        
    average_sale = total_sales / number_of_sales
    
    print(name + "'s average sale was: $", format(average_sale, ".2f"))
    print(name + "'s highest sale was: $", format(highest_sale, ".2f"))
    print(name + "'s lowest sale was: $", format(lowest_sale, ".2f"))


def sales_input():
    while True:
        try:
            sale = float(input("Enter the dollar amount for their sale: "))
            sale = sales_range_error_handling(sale)
            return sale
        except ValueError:
            print("Error: That is not a number.")


def sales_range_error_handling(sale):
    while sale < 1 or sale > 25000:
        print("Error: the sale cannot be less than $1 or greater than $25000.")
        sale = float(input("Please enter a correct sale amount: "))
    return sale


main()
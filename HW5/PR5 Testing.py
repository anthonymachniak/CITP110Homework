def sales_input():
    while True:
        try:
            sale = float(input("Enter the dollar amount for their sale: "))
            sale = sales_range_error_handling(sale)
            return sale
        except ValueError:
            print("Error: That is not a number.")


def sales_range_error_handling(sale):
    while sale < 0 or sale > 25000:
        print("Error: the sale cannot be less than $0 or greater than $25000.")
        sale = float(input("Please enter a correct sale amount: "))
    return sale


print(sales_input())
#print(sales_range_error_handling(sale))

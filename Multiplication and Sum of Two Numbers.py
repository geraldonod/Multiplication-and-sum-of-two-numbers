#create user defined variable
def product_or_sum(num1, num2):
    product = num1 * num2

#create if-else statement for sum or product
    if product <= 1000:
        return product
    else:
        return num1 + num2 
    
#ask user for input
number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))

#print out result
result = product_or_sum(number1, number2)
print("Result:", result)
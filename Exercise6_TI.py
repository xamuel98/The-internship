''' This program prompts the user to choose between 
  computing the product and sum of 1 to n '''

# Prompt the user to enter a number
n = int(input("Enter a number: "))

# Prompt the user to choose an option
option = int(input("Enter 1 to compute product of 1 to n \nand 2 to compute sum of 1 to n: "))

if option == 1:
    product = 1
    for i in range(1, n + 1):
        product = product * i
    print("The product of 1 to" ,n ,"is ",product)
elif option == 2:
    sum = 0
    sum = (n * (n + 1)) / 2
    print("The sum of 1 to" ,n ,"is ",sum)
else:
    print("Invalid option chosen. Please enter a valid option !!!")
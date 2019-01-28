''' This program prints all prime numbers to n '''

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True 

def printPrimeNumber(numberOfPrime):
    NUMBER_OF_PRIMES_PER_LINE = 10
    count = 0
    number = 2
    while count < numberOfPrime:
        if isPrime(number):
            count += 1

            print(number, end = " ")
            if count % NUMBER_OF_PRIMES_PER_LINE == 0:
                print() # Jump to new line

        number += 1

def main():
    n = int(input("Enter the number of primes you want to print: "))
    print("The First", n, "Prime numbers are: ")
    printPrimeNumber(n)

main()
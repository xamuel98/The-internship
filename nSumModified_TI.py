''' This program prints only multiple of 3 or 5 in sum of 1 to n '''
n = int(input("Enter a number: "))
i = 0
while i < n:
    if (i % 3) != 0 and (i // 3) != 0:
        print(i)
    else:
        print("nah")
    i += 1
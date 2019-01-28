''' This Program prints a multiplication table up to 12 '''
print("\t\tMultiplication table")
print(" |  ", end = '')
for j in range(1, 13):
    print("  ", j, end = '')
print() # Jump to new line
print("---------------------------------------------------------------------")

# Display multiplication table
for i in range(1, 13):
    print(i, "|", end = '')
    for j in range(1, 13):
        # Display the product and align properly
        print(format(i * j, "4d"), end = '')
    print() # Jump to new line
# Prompt user to enter a string
username = str(input("Enter your username, username should be alice or bob: "))

''' Convert the username to lowercase letters and compare
    if the what the user entered correlates with  accepted string '''
    
if username.lower() == "alice" or username.lower() == "bob":
    print("Welcome to programming with python " + username)
else:
    print("Invalid username...")
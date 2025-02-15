import os

# Welcome message
print("Welcome to Dope A F bank. The home of your banking needs ")

######### Log into your bank########################

# Do you have an account?



start = input("Do you have an account. Please type Y for yes and N for No. ").capitalize().strip()
os.system("cls")
while True:
    # Register
    if start == "N":
        print("A new customer Great. You will not regret joining Dope A F.\n")
        inname = input("What is your user name ")
        inpin = int(input("What is your pin "))
        os.system("cls")
        start="Y"
        
    

    # login
    if start == "Y":
        print("OK lets Log into your Dope A F bank account \n")
        name = input("Please enter your user name ")
        pin = int(input("Please enter your pin "))
        os.system("cls")
    if pin == inpin and name ==inname:
        print(f"Welcome to your Dope A F account {name.capitalize()}")
        break

####################################################################








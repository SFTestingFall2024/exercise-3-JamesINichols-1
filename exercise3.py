# Juan Gonzalez (juango4)
# COP2002-0M1
# August 27, 2024
# Exercise 3: If statements
# This program determines the manufacturer for a NIC card provided a MAC address by the user.

def main():
    addresses=["00:00:17", "00:07:E9", "04:27:28",  # Valid hex addresses of the NIC cards
               "04:26:65", "04:33:89", "00:00:0C"]
    manufacturers=["Oracle", "Intel Corporation", "Microsoft Corporation",  # Manufacturers of the NIC cards
                   "Apple, Inc.", "Huawei Technologies Co., Ltd", "Cisco Systems, Inc"]

    # Program title with dashes
    print("MAC Manufacturer Program")
    print("------------------------\n")

    userInput=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")  # Prompt user for input

    checkingInput=True  # Flag to allow the while loop to run, eventually evaluates to False

    while checkingInput:
        if(userInput in addresses):     # Only lands in this if statement if user input exists within addresses
            print(f"For {userInput} the MAC manufacturer is {manufacturers[addresses.index(userInput)]}.")
            checkingInput=False    # Changes status of condition for while loop, allowing to break out
        else:
            print(f"For {userInput} the MAC manufacturer is Unknown.")
            checkingInput=False    # Changes status of condition for while loop, allowing to break out

if(__name__=="__main__"):
    main()
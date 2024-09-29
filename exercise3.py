# Tyler Santos (santost12)
# COP2002-OM1
# September 18, 2024
# Exercise 3: If statements
# Program to determine manufacturer for a NIC card


# Takes macInput string and looks up manufacturer.
def lookupMac(macInput):
    macInput = macInput.upper() # Convert to uppercase

    if macInput == "00:00:17":
        print(f"For {macInput} the MAC manufacturer is Oracle.")

    elif macInput == "00:07:E9":
        print(f"For {macInput} the MAC manufacturer is Intel.")

    elif macInput == "04:27:28":
        print(f"For {macInput} the MAC manufacturer is Microsoft Corporation.")

    elif macInput == "04:26:65":
        print(f"For {macInput} the MAC manufacturer is Apple, Inc.")

    elif macInput == "04:33:89":
        print(f"For {macInput} the MAC manufacturer is Huawei Technologies Co.,Ltd.")

    elif macInput == "00:00:0C":
        print(f"For {macInput} the MAC manufacturer is Cisco Systems, Inc.")

    else:
        print(f"For {macInput} the MAC manufacturer is Unknown.")


# Takes macInput string and checks if is 8 characters.
# Returns 0 for valid input.
def validateInputLen(macInput):
    if len(macInput) < 8:
        print("Error: Not enough characters entered.")
        return -1

    elif len(macInput) > 8:
        print("Error: Too many characters entered.")
        return -2 

    else:
        return 0


# Main function, where the user is prompted for input.
def main():
    print("MAC Manufacturer Program")
    print("------------------------\n")

    macInput = str(input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): "))

    # Require 8 characters
    while (validateInputLen(macInput) != 0):
        macInput = str(input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): "))

    lookupMac(macInput)


if (__name__=="__main__"):
    main()

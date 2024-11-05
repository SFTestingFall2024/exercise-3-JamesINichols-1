# Tyler Santos (santost12)
# COP2002-OM1
# September 18, 2024
# Exercise 3: If statements
# Program to determine manufacturer for a NIC card


# Takes macInput string and returns manufacturer as string.
def lookupMac(macInput):
    macInput = macInput.upper() # Convert to uppercase

    # Check input for these prefixes.
    # And if there's no match, return Unknown.
    if macInput == "00:00:17":
        return "Oracle"
    elif macInput == "00:07:E9":
        return "Intel Corporation"
    elif macInput == "04:27:28":
        return "Microsoft Corporation"
    elif macInput == "04:26:65":
        return "Apple, Inc."
    elif macInput == "04:33:89":
        return "Huawei Technologies Co.,Ltd."
    elif macInput == "00:00:0C":
        return "Cisco Systems, Inc."
    else:
        return "Unknown"


# Takes macInput string and checks if is 8 characters.
# Returns 0 for valid input.
def validateInputLen(macInput):

    # Eight characters exactly includes the colon.
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

    # Require 8 characters. Ask for input again if too many or too few.
    while (validateInputLen(macInput) != 0):
        macInput = str(input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): "))

    # Get manufacturer and then print.
    manufacturer = lookupMac(macInput)
    print(f"For {macInput} the MAC manufacturer is {manufacturer}")


if (__name__=="__main__"):
    main()

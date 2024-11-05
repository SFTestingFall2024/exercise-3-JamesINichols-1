# John Coffill (jscoffill)
# F24 COP2002.0M1
# 10/01/2024
# Exercise 3: If statements
# Determine manufacturer for a NIC card.

# Create Function


def main():
    
    # Program header


    print("MAC Manufacturer Program")

    print("------------------------")

    print("")

    # Get user input


    user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # Create variable to store company 


    company = "Unknown"

    # Check for each manufacturer 


    if user_input == "00:00:17":

        company = "Oracle"

    elif user_input == "00:07:E9":

        company = "Intel Corporation"

    elif user_input == "04:27:28":

        company = "Microsoft Corporation"

    elif user_input == "04:26:65":

        company = "Apple, Inc."

    elif user_input == "04:33:89":

        company = "Huawei Technologies Co., Ltd."

    elif user_input == "00:00:0C":

        company = "Cisco Systems, Inc."

    #Print Manufacturer


    print("For", user_input, "the MAC manufacturer is", company)

# Run the program


if __name__ == "__main__":

    main()

# Andrea Camaratta (A-Camaratta on Github)
# Course ID: COP2002.0M1
# Date Created: 9/23/2024
# Title: Exercise 3
# This program will provide a resource in which a user can input a MAC address and retrieve the manufactuer

# In this section we set up the title section
title_1 = "mac "
title_2 = "manufacturer program"
title_1 = title_1.upper()
title_2 = title_2.title()
introduction = (title_1+title_2)
print(introduction)

#we are going to print the dashes afterword
print(f"-"*26)

# We now define the main function of the program
def main():
    prompt = "\nEnter the first 6 hex values of the MAC address (format as XX:XX:XX): "
    hex_digits = input(prompt)

# Here we are defining the values of the manufacturer based upon the user's input in hex_digits
    if hex_digits == "00:00:17":
        manufacturer = "Oracle"
    elif hex_digits == "00:07:E9":
        manufacturer = "Intel Corporation"
    elif hex_digits == "04:27:28":
        manufacturer = "Microsoft Corporation"
    elif hex_digits == "04:26:65":
        manufacturer = "Apple, Inc."
    elif hex_digits == "04:33:89":
        manufacturer = "Huawei Technologies Co.,Ltd"
    elif hex_digits == "00:00:0C":
        manufacturer = "Cisco Systems, Inc"
    else:
        manufacturer = "not found"
    
    # Here we are attaching the values from the user input to print the result
    print(f"For {hex_digits} the MAC manufacturer is {manufacturer}.")


if(__name__ == "__main__"):
    main()
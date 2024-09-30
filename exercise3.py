# John Coffill (jscoffill)
# F24 COP2002.0M1
# 09/19/2024
# exercise3.py
# Determine manufacturer for a NIC card.

#Create Function


def main():
    
    # Manufacturer list


    manufacturer = {
        
        "00:00:17": "Oracle",

        "00:07:E9": "Intel Corporation",

        "04:27:28": "Microsoft Corporation",

        "04:26:65": "Apple, Inc.",

        "04:33:89": "Huawei Technologies Co.,Ltd",

        "00:00:0C": "Cisco Systems, Inc"
    }

    # Program header


    print("MAC Manufacturer Program")

    print("------------------------")

    print("")

    # Get user input


    user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # Check input format


    if (len(user_input) == 8 and 
        
        user_input[2] == ':' and 

        user_input[5] == ':'):
        
        # Check if all characters are valid hex


        valid = True

        for c in user_input:
            
            if c not in '0123456789ABCDEFabcdef:':
                
                valid = False

                break
        
        if valid:

            if user_input in manufacturer:
                
                company = manufacturer[user_input]

            else:
                
                company = "Unknown"
                
            print("For", user_input, "the MAC manufacturer is", company)

        else:
            
            print("<Not valid value or not found>")
   
# Run the program


if(__name__ == "__main__"):
    
    main()

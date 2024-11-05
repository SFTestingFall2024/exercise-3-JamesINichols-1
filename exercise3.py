# John Johnson
# COP2002.0M1
# September 22, 2024
# NIC Manufacturer Identifier
# the purpose of the program is to identify the manufacturer of a Network Interface Card (NIC) based on its hex code input.

def main():
    # Define the hex codes and corresponding manufacturers
    hex_codes = [
        "00:00:17", "00:07:E9", "04:27:28", "04:26:65", 
        "04:33:89", "00:00:0C"
    ]
    
    manufacturers = [
        "Oracle", "Intel Corporation", "Microsoft Corporation", 
        "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc"
    ]
    
    # Ask user for input
    user_input = input("Enter the first 6 hex digits (formatted as XX:XX:XX): ")
    
    # Initialize variable for the manufacturer
    manufacturer = "Unknown"
    
    # Check if the input is in the list of hex codes
    for i in range(len(hex_codes)):
        if hex_codes[i].lower() == user_input.lower():  # Case insensitive comparison
            manufacturer = manufacturers[i]
            break
    
    # Display the result
    print(f"Hex Digits: {user_input} \t Manufacturer: {manufacturer}")

# Call the main function
if __name__ == "__main__":
    main()

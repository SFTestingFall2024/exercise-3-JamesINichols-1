def get_manufacturer(mac_prefix):
    # Dictionary of MAC prefix to manufacturer
    mac_database = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co.,Ltd",
        "00:00:0C": "Cisco Systems, Inc",

        # Add more manufacturers as needed
    }
    
    # Check if the provided prefix exists in the database
    return mac_database.get(mac_prefix.upper(), "Unknown Manufacturer")

def main():
    # Ask user for input
    mac_input = input("Enter the first 6 hex digits of the MAC address (formatted as XX:XX:XX): ")

    # Validate the format
    if len(mac_input) == 8 and mac_input[2] == ':' and mac_input[5] == ':' and all(c in "0123456789ABCDEFabcdef:" for c in mac_input):
        manufacturer = get_manufacturer(mac_input)
        print(f"Manufacturer: {manufacturer}")
    else:
        print("Invalid format. Please use XX:XX:XX.")

if __name__ == "__main__":
    main()
    
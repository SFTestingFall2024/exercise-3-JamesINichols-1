# dictionary of manufacturers
manufacturers = {
    "00:00:17": "Oracle",
    "00:07:E9": "Intel Corporation",
    "04:27:28": "Microsoft Corporation",
    "04:26:65": "Apple, Inc.",
    "04:33:89": "Huawei Technologies Co.,Ltd",
    "00:00:0C": "Cisco Systems, Inc"
}

def get_manufacturer(oui):
    """Retrieve the manufacturer based on the OUI."""
    return manufacturers.get(oui.upper(), "Manufacturer not found")

def main():
    print("NIC Card Manufacturer Lookup")
    
    # Prompt user for input
    user_input = input("Enter the first 6 hex digits formatted as XX:XX:XX: ")

    # Validate the input format
    if (len(user_input) == 8 and
        user_input[2] == ':' and
        user_input[5] == ':' and
        all(c in '0123456789ABCDEFabcdef' for c in user_input.replace(':', ''))):
        
        manufacturer = get_manufacturer(user_input[:8])  # Extract the OUI
        print("\nResult:")
        print(f"Manufacturer: {manufacturer}")
    else:
        print("Invalid format. Please enter the OUI in the format XX:XX:XX.")

if __name__ == "__main__":
    main()
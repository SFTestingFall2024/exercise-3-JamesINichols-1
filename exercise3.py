#James Johnson f24 COP2002-0m1
#This program will ask the user to input a 6 digit hex number from a manufacturer and then tell the user who the manufacturer is.

def get_mac_manufacturer(mac):
    # Dictionary for hex values
    manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co.,Ltd",
        "00:00:0C": "Cisco Systems, Inc"
    }
    
    # Return the manufacturer or "Unknown" if manufacturer is not found
    return manufacturers.get(mac, "Unknown")

def main():
    print("           MAC Manufacturer Program")
    print("------------------------\n")

    # Prompt the user for the first 6 hex digits
    mac_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    
    # Get the manufacturer name
    manufacturer = get_mac_manufacturer(mac_input)
    
    # Displays the result to the user
    print(f"\nFor {mac_input} the MAC manufacturer is {manufacturer}.")

if __name__ == "__main__":
    main()

def main():
    # Prompt user for input
    mac_address = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    
    # Dictionary of MAC manufacturers
    manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co., Ltd",
        "00:00:0C": "Cisco Systems, Inc"
    }

    # Check if the input is in the dictionary
    if mac_address in manufacturers:
        manufacturer = manufacturers[mac_address]
    else:
        manufacturer = "Unknown"

    # Output results
    print("\nMAC Manufacturer Program")
    print("------------------------")
    print()
    print(f"For {mac_address} the MAC manufacturer is {manufacturer}.")

if __name__ == "__main__":
    main()

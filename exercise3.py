def main():
    # Dictionary to store MAC address prefixes and their manufacturers
    mac_manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co.,Ltd",
        "00:00:0C": "Cisco Systems, Inc"
    }

    # Print the title
    print("MAC Manufacturer Program")
    print("------------------------")
    print()

    # Get user input
    user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ").strip()

    # Determine the manufacturer or if it's unknown
    manufacturer = mac_manufacturers.get(user_input, "Unknown")

    # Print the result
    print(f"For {user_input} the MAC manufacturer is {manufacturer}.")

# Call the main function
if __name__ == "__main__":
    main()

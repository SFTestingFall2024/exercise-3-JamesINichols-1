def main():
    # List of hex digits and corresponding manufacturers
    hex_codes = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]
    manufacturers = [
        "Oracle",
        "Intel Corporation",
        "Microsoft Corporation",
        "Apple, Inc.",
        "Huawei Technologies Co.,Ltd",
        "Cisco Systems, Inc."
    ]

    # Ask user for input
    user_input = input("Please enter the first 6 hex digits (formatted as XX:XX:XX): ")

    # Search for the manufacturer
    if user_input in hex_codes:
        index = hex_codes.index(user_input)
        print(f"Hex Digits\tManufacturer\n{user_input}\t{manufacturers[index]}")
    else:
        print(f"Hex Digits\tManufacturer\n{user_input}\tUnknown")

# This is so that the main function runs only if this file is executed 
if __name__ == "__main__":
    main()

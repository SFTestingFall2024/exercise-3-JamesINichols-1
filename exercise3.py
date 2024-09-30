#ChristianMathieu
#COP2002.0M1
#September 22,2024
#NIC Manufacturer Identifier
#Identifies Manacturer using hex codes
print("Mac Manufacturer Identifier" + " " *2)
def main():
    # List of hex codes and their  manufacturers
    manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co.,Ltd",
        "00:00:0C": "Cisco Systems, Inc"
    }

    # Prompt user for input
    hex_digits = input("Enter the first 6 hex digits (formatted as XX:XX:XX): ")

    # Get the manufacturer, default to "Unknown" if not found
    manufacturer = manufacturers.get(hex_digits, "Unknown")

    # Output the result
    print("Hex Digits\tManufacturer")
    print(f"{hex_digits}\t{manufacturer}")

#  main function
if __name__ == "__main__":
    main()

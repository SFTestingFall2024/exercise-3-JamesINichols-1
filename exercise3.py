def get_manufacturer():
    manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co.,Ltd",
        "00:00:0C": "Cisco Systems, Inc"
    }

    hex_input = input("Enter the first 6 hex digits (XX:XX:XX): ").upper()

    if hex_input.count(':') == 2 and len(hex_input) == 8:
        print(f"Manufacturer: {manufacturers.get(hex_input, 'Unknown')}")
    else:
        print("Invalid input format. Please enter in XX:XX:XX format.")

if __name__ == "__main__":
    get_manufacturer()

def get_manufacturer(hex_digits):
    manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co.,Ltd",
        "00:00:0C": "Cisco Systems, Inc"
    }

    return manufacturers.get(hex_digits, "Unknown")

def main():
    print("           MAC Manufacturer Program")
    print("------------------------\n")
    
    hex_digits = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ").strip()

    manufacturer = get_manufacturer(hex_digits)
    
    print(f"For {hex_digits} the MAC manufacturer is {manufacturer}.")


if __name__ == "__main__":
    main()
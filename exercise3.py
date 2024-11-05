# Create opening message
opening_message = "MAC Manufacturer Program"
opening_message += "\n------------------------"
opening_message += "\n"
opening_message += "\nEnter the first 6 hex values of the MAC address (format as XX:XX:XX): "
# Establish user input
user_code = input(opening_message)

# Create 'manufacturer' dictionary
manufacturer = {
    '00:00:17': 'Oracle',
    '00:07:E9': 'Intel Corporation',
    '04:27:28': 'Microsoft Corporation',
    '04:26:65': 'Apple Inc.',
    '04:33:89': 'Huwaei Technologies Co., Ltd.',
    '00:00:0C': 'Cisco Systems, Inc.',
    '<Not valid value or not found>': 'Unknown' 
}

# If-statements for matching user-input to hexcodes
if user_code in manufacturer.keys():
    print(f"For {user_code}, the MAC manufacturer is {manufacturer[user_code]}")
else:
    print(f"For {user_code}, the MAC manufacturer is unknown") 
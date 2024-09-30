#Timothy Flores
#COP2002.0M1:Programming Logic
#09.22.24
#Exercise 3
#Program to determine the manufacturer of a NIC Card

#Dictionaries to include in list of Nic Cards to compare with user input
niccard_0= {"00:00:17": {"manufacturer": 'Oracle', "hex digits": "00:00:17"}}
niccard_1= {"00:07:E9": {"manufacturer": 'Intel Corporation', "hex digits": "00:07:E9"}}
niccard_2= {"04:27:28": {"manufacturer": 'Microsoft Corporation', "hex digits": "04:27:28"}}
niccard_3= {"04:26:65": {"manufacturer": 'Apple, Inc.', "hex digits": "04:26:65"}}
niccard_4= {"04:33:89": {"manufacturer": 'Huawei Technologies Co.,Ltd', "hex digits": "04:33:89"}}
niccard_5= {"00:00:0C": {"manufacturer": 'Cisco Systems, Inc', "hex digits": "00:00:0C"}}

#Variable list defined
niccards= [niccard_0,niccard_1,niccard_2,niccard_3,niccard_4,niccard_5]

#intro statement at start of program
print("MAC Manufacturer Program\n","------------------------\n\n")

#prompt to ask user for Hex Value
hex=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

#Loop through the Nic Card list to match user input
active=True
while active:
    if hex in niccards:
        print(f"For {hex}, the manufacturer is {niccards: [manufacturer]}.")
        active=False
    else:
        print("Sorry, that is not a valid Mac address, Try again please.")
        break
# Aron Rascan
# COP2002-0M1
# Sept. 19th, 2024
# Exercise 3
# Print correct Manufacturer based on user input MAC Address


# List or Array
hexvalue=["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]
manu=["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc"]

# Header print statement
print("MAC Manufacturer Program")
print("------------------------")
print()
print()

# User Input
userHex=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
if (userHex==hexvalue[0]):
    print(f"For {userHex} the MAC manufacturer is {manu[0]}.")

elif (userHex==hexvalue[1]):
    print(f"For {userHex} the MAC manufacturer is {manu[1]}.")

elif (userHex==hexvalue[2]):
    print(f"For {userHex} the MAC manufacturer is {manu[2]}.")

elif (userHex==hexvalue[3]):
    print(f"For {userHex} the MAC manufacturer is {manu[3]}.")

elif (userHex==hexvalue[4]):
    print(f"For {userHex} the MAC manufacturer is {manu[4]}.")

elif (userHex==hexvalue[5]):
    print(f"For {userHex} the MAC manufacturer is {manu[5]}.")

else:
    print(f"For {userHex} the MAC manufacturer is Unknown.")


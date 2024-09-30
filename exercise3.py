# Zane Vance
# COP2002.0M1: Program Logic
# Created 9/22/24
# Exercise 3: If statements
# Program will take user input to discern which manufacturer made an item from the first 6 hex values of the MAC address

print("MAC Manufacturer Program")
print("------------------------\n")

# Prints the top of the program. Number of dashes might be off.

hex = input("Enter the first 6 hex values  of the MAC address (format as XX:XX:XX): ")

# Prompts the user for the 6 hex values

if hex== "00:00:17" : manufacturer = "Oracle"
elif hex== "00:07:E9" : manufacturer = "Intel Corporation"
elif hex== "04:27:28" : manufacturer = "Microsoft Corporation"
elif hex== "04:26:65" : manufacturer = "Apple, Inc."
elif hex== "04:33:89" : manufacturer = "Huawei Technologies Co.,Ltd"
elif hex=="00:00:0C" : manufacturer = "Cisco Systems, Inc"
else : manufacturer = "Unknown"

# Compares the user-inputted hex value to the ones tied to given manufacturers

print(f"For " + hex +" the MAC manufacturer is "+ manufacturer+ ".")
#Aidan Riffee
#F24 COP2002.0M1: PROGRAM LOGIC
#9/21/24
#Exercise 3: If-statements
#This program requires user input in the form of hex digits and outputs
#the corresponding manufacturer.

def main():
#Dictionary that contains the hex codes and the corresponding manufacturer names

    hex_Manuf={
        '00:00:17':'Oracle',
        '00:07:E9':'Intel Corporation',
        '04:27:28':'Microsoft Corporation',
        '04:26:65':'Apple, Inc',
        '04:33:89':'Huawei Technologies Co.,Ltd',
        '00:00:0C':'Cisco Systems, Inc'}
#vars and user prompt

    output=False
    address=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    
#for loop to identify the proper manufacturer name based on the hex value

    for key, value in hex_Manuf.items():
        if address==key:
            print(f"For {key} the MAC manufacturer is {value}.")
            output=True
#final if-statement that responds "unknown" if user input matched no hex values

    if output==False:
        print("Unknown; Not valid value or not found.")
#function call

main()

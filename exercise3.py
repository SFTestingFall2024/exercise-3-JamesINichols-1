# SFC-COMP-RC
# COP2002.0M1
# September 20, 2024
# Exercise 3: If statements 
# This program uses a array of known MAC address to take to the user input first 6 hex values of a MAC address to return the manufacturer of a NIC

def main():

    # Known values to retrive data from, stored as arrays
    knownHex=["00:00:17","00:07:E9","04:27:28","04:26:65","04:33:89","00:00:0C"]
    manufactures=["Oracle","Intel Corporation","Microsoft Corporation","Apple, Inc.","Huawei Technologies Co.,Ltd","Cisco Systems, Inc"]

    # Display a title and Request the user's input stored as macInput
    macInput=input("MAC Manufactuer Program\n-----------------------\n\nEnter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    for i in range(len(knownHex)): # Loop for the number of items in the Array "knownHex"

        if( knownHex[i] == macInput): # Check if the user input matches a known hex value
            print(f"For {macInput} the MAC manufacturer is {manufactures[i]}") # Output the user's input and manufacturer of the NIC
            break

    else:
        print(f"For {macInput} the MAC manufacturer is Unkown") # If the input doesn't match a known MAC address, the output the user's input and Unkown.


# Call the main() function
if(__name__=="__main__"):
    main()
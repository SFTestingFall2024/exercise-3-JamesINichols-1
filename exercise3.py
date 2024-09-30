# Jason DeGroff (JasonDeGroff)
# COP2002-0M1
# September 22,2024
# MAC Manufacturer Program
# This program takes user input in the format of XX:XX:XX hex values on a NIC card and provides the manufacturer of the card.

def main():
    # Set list of MAC address and Manufactures. These are constants as they should not change during this program
    MAC_ADDRESSES = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C",]
    MANUFACTURERS = ["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.", "Hauwei Technologies Co.,Ltd", "Cisco Systems, Inc", "Unknown"]
    
    # Begins display of program and ask for user input
    print("MAC Manufacturer Program")
    print("------------------------\n")
    macAddress = input("Enter the first 6 hex vaules of the MAC address (format as XX:XX:XX): ")
    
    #here we use a while loop to go through the MAC_ADDRESSES. If the user input matches the address it leaves the loop, otherwise it itterates the index and trys the next index in the MAC_ADDRESSES list
    i = 0
    while i < len(MAC_ADDRESSES):
        if macAddress == MAC_ADDRESSES[i]:
            break
        i+=1
    
    #This prints the manufacture for the user input MAC ADDRESS
    print(f"For {macAddress} the MAC manufacturer is {MANUFACTURERS[i]}.")


    
if(__name__=="__main__"):
    main()
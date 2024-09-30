#Exercise 3: If Statements

#COP2002 0M1
#9/22/24
#This code asks the user for the first 6 hex digits formatted as XX:XX:XX and provides the manufacturer.

def main():

    hexcode = str(input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): "))

    hexcode1 = "00:00:17"
    hexcode2= "00:07:E9"
    hexcode3= "04:26:28"
    hexcode4 = "04:26:65"
    hexcode5 = "04:33:89"
    hexcode6 = "00:00:0C"

# If, elif and else statements check the equality of the hexcode entered.
# If the hexcode value is listed it prints the manufacturer.
# If the value entered is not one listed Manufacturer Unknown is printed.
    if hexcode == hexcode1:
        print ("For 00:00:17 the MAC manufacturer is Oracle.")

    elif hexcode == hexcode2:
        print ("For 00:07:E9 the MAC manufacturer is Intel Coperpration.")

    elif hexcode == hexcode3:
        print ("For 04:27:28 the MAC manufacturer is Microsoft Corporation.")


    elif hexcode == hexcode4:
        print ("For 04:26:65 the MAC manufacturer is Apple, Inc.")

    elif hexcode == hexcode5:
        print ("For 04:33:89 the MAC manufacturer is Huawei Technologies Co.,Ltd.")

    elif hexcode == hexcode6:
        print ("For 00:00:0C the MAC manufacturer is Cisco Systems, Inc.")

    else: print ("<Not valid value or not found> Manufacturer Unknown")

if(__name__=="__main__"):
    main()
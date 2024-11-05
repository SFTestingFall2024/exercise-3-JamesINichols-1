#Aidan Riffee
#F24 COP2002.0M1: PROGRAM LOGIC
#9/21/24
#Exercise 3: If-statements
#This program requires user input in the form of hex digits and outputs
#the corresponding manufacturer.

def main():

    print("MAC Manufacturer Program")
    print("-------------------------")
    
    #lists for the hex digits and the manufacturers

    hexDigits=['00:00:17', '00:07:E9', '04:27:28', '04:26:65', '04:33:89', '00:00:0C']
    manufacturers=['Oracle', 'Intel Corporation', 'Microsoft Corporation', 'Apple, Inc', 'Huawei Technologies Co.,Ltd', 'Cisco Systems, Inc', 'Unknown']
    
    #vars and user prompt
    index=0
    code=""
    address=input("\nEnter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    
    #for loop to identify the index of the input value in the list hexDigits

    for digit in hexDigits:
        if(digit==address):
            index=hexDigits.index(digit)
            code=digit
  
    #determines if the input value was recognizable
  
    if (code==""):
        print(f"\nFor {address} the MAC manufacturer is {manufacturers[-1]}.")
    else:
        print(f"\nFor {address} the MAC manufacturer is {manufacturers[index]}.")

#function call

if(main==main):
    main()

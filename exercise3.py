#SarahLudwig
#COP2002.0M1
#09/21/24
#Exercise 3 : If Statements
#This program allows a user to enter a MAC address and look up the manufacturer.

def main():
    
    #using lists to store MAC addresses as well as manufacturers
    hexDigits = ["00:00:17","00:07:E9","04:27:28","04:26:65","04:33:89","00:00:0C"]
    manufacturer = ["Oracle","Intel Corporation","Microsoft Corporation","Apple, Inc.","Huawei Technologies Co.,Ltd","Cisco Systems, Inc"]
    listLength = len(hexDigits)
    indexCheck = 0

    print("MAC manufacturer Program\n-------------------------\n")
    
    prompt = "Enter the first 6 hex values of the MAC Address (format as XX:XX:XX): "
    message = ""
    message = input(prompt)

    active = True
    
    #using a while loop to move through the list of hexDigits and once matched, pull the corresponding manufacturer at the correct index
    
    while active and indexCheck<=listLength:
        
        if hexDigits[indexCheck] == message:
            active = False
            print(f'\nFor {hexDigits[indexCheck]} the MAC manufacturer is {manufacturer[indexCheck]}')
        elif indexCheck == listLength-1:
            active = False
            print(f'\nFor {message} the MAC manufacturer is unknown')
        else:
            indexCheck+=1


if(__name__=="__main__"):
    main()



        
    
    
    
#Sebastian Ildefonso
#Professor Nichols
#COP2002.0M1
#9/22/24
#This program searches and gives MAC manufactueres based of a Hex code the user inputs


#Variables
codeHex = input("Enter the first 6 hex valuse of the MAC address (format as XX:XX:XX): ")

#Statements that search using user input
if(codeHex == "00:00:17"):
    print("The MAC manufacturer is Oracle.")
elif(codeHex == "00:07:E9"):
    print("The MAC manufacturer is Intel Corporation.")
elif(codeHex == "04:27:28"):
    print("The MAC manufacturer is Microsoft Corporation.")
elif(codeHex == "04:26:65"):
    print("The MAC manufacturer is Apple, Inc.")
elif(codeHex == "04:33:89"):
    print("The MAC manufacturer is Huawei Technologies Co.,Ltd.")
elif(codeHex == "00:00:0C"):
    print("The MAC manufacturer is Cisco Systems, Inc.")

else:
        print("Unknown")

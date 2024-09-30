# Emma Whitworth (EmmaBean004)
# COP2002-0T1
# September 22,2024
# MAC Finder
# Identifies the manufacturer of a given MAC

def main():
    # Indent code you write to go in here
    Hexlist = ["00:00:17",
               "00:07:E9",
               "04:27:28",
               "04:26:65",
               "04:33:89",
               "00:00:0C",
               "<Not valid value or not found>"]
    Manlist = ["Oracle",
                    "Intel Corporation",
                    "Microsoft Corporation",
                    "Apple,Inc.",
                    "Huawei Technologies Co.,Ltd",
                    "Cisco Systems, Inc",
                    "Unknown"]
    UserHex = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    n = 0
    while (n<6):
        if(UserHex==Hexlist[n]):
            print("For "+UserHex+" the MAC manufacturer is "+Manlist[n])
            break
        else:
            n+=1
    if (n>=6):
        print("For "+Hexlist[n]+" the MAC manufacturer is "+Manlist[n])
    
if(__name__=="__main__"):
    print("MAC Manufacturer Program \n")
    main()

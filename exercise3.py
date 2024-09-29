## Sebastian Brant
## F24 COP2002.0M1
## 9/22/24

def main():
    #Two lists, for hex codes and manufacturer
    hex_codes=["00:00:17","00:07:E9","04:27:28","04:26:65","04:33:89","00:00:0C"]
    manufacturer=["Oracle","Intel Corporation","Microsoft Corporation","Apple, Inc.","Huawei Technologies Co.,Ltd","Cisco Systems, Inc"]

    #Input for user, which then runs input through if, elif, else, checking the hex_codes list and printing the corresponding manufacturer
    print("MAC Manufacturer Program\n------------------------\n")
    hex_code_input=input("Enter the first 6 values of the MAC address (format as XX:XX:XX): ")
    if hex_code_input==hex_codes[0]:
        print(manufacturer[0])
    elif hex_code_input==hex_codes[1]:
        print(manufacturer[1])
    elif hex_code_input==hex_codes[2]:
        print(manufacturer[2])
    elif hex_code_input==hex_codes[3]:
        print(manufacturer[3])
    elif hex_code_input==hex_codes[4]:
        print(manufacturer[4])
    elif hex_code_input==hex_codes[5]:
        print(manufacturer[5])
    else:
        print("Unknown")

#Main function check
if __name__=="__main__":
    main()
# Name: Dalton Lundy
# Course ID: F24 COP2002.0M1
# Date Created: 9/22/24
# Program Title: Exercise 3
# Program Description: This program determines the manufacturer of a NIC card based on the first 6 hex digits of the MAC address.

def main():
    # List of manufacturers
    manufacturers = ["Oracle","Intel Corporation","Microsoft Corporation","Apple, Inc.","Huawei Technologies Co.,Ltd","Cisco Systems, Inc"]

    # Prompt the user for input
    user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # Determine the manufacturer using if statements
    if user_input == "00:00:17":
        manufacturer = manufacturers[0]
    elif user_input == "00:07:E9":
        manufacturer = manufacturers[1]
    elif user_input == "04:27:28":
        manufacturer = manufacturers[2]
    elif user_input == "04:26:65":
        manufacturer = manufacturers[3]
    elif user_input == "04:33:89":
        manufacturer = manufacturers[4]
    elif user_input == "00:00:0C":
        manufacturer = manufacturers[5]
    else:
        manufacturer = "Unknown"

    # Print the result
    print(f"\nFor {user_input} the MAC manufacturer is {manufacturer}.")


if(__name__=="__main__"):
    main()
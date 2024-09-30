# Jacob McCravy (JacobMcCravy)
# COP2002-0M1
# September 19, 2024
# Exercise 3: If statements
# This program takes the first 6 digits of a MAC address and outputs the manufacturer.

def main():

# Create two list that have matching index positions. ie. manList[x] == hexList[x]
    manList = [
    'Oracle.',
    'Intel Corporation.',
    'Microsoft Corporation.',
    'Apple, Inc.',
    'Huawei Technologies Co.,Ltd.',
    'Cisco Systems, Inc.',
    'unknown.']

    hexList = [
    '00:00:17',
    '00:07:E9',
    '04:27:28',
    '04:26:65',
    '04:33:89',
    '00:00:0C']


# creating variables for print statemnts
    outputFound = "The manufacturer is: "
    outputUnknown = "My apologies, this manufacturer is"


# Input statement that asks for first 6 characters of MAC address.
    hexInput = input("Please type the first 6 characters, including colons(XX:XX:XX): ")


# If elif statement that compares the values of hexInput to hexList[x] then outputs corresponding manList[x] value.
    if hexInput.upper() == hexList[0]:
        print(outputFound, manList[0])
    elif hexInput.upper() == hexList[1]:
        print(outputFound, manList[1])
    elif hexInput.upper() == hexList[2]:
        print(outputFound, manList[2])
    elif hexInput.upper() == hexList[3]:
        print(outputFound, manList[3])
    elif hexInput.upper() == hexList[4]:
        print(outputFound, manList[4])
    elif hexInput.upper() == hexList[5]:
        print(outputFound, manList[5])
    else:
        print(outputUnknown, manList[-1])



if(__name__=="__main__"):
    main()
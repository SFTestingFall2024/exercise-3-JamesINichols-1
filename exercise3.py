#Joseph Wright
#COP2002.0M1
#9/28/2024




print("MAC Manufacturer Program")
print("------------------------")
"Please enter your name:joseph Wright  "
print("Enter the first 6 hex valuse of the MAC address format as (xx.xxxx)")
hex=04.3389

#hex digits
a=00.0017
b=00.07E9
C=04.2728
D=04.2665
E=04.3389
F=00000
#manufactures
g=("Oracle")
h=("Intel corporation")
i=("Microsoft Corporation")
j=("Apple, inc.")
k=("Huawei Technologies Co.,Ltd")
l=("Cisco Sysytems, Inc")

if(hex==00.0017):
    print("For the hex digit 00:00:17 the Manufacturer for this  NIC card is Oracle")
elif(hex==00.07E9):
    print("For the hex digit 00:07:E9 the Manufacturer for this NIC card is Intel Corporation")
elif(hex==04.2728):
    print("For the hex digit 04:27:28 the Manufacturer for this NIC card is Microsoft Corporation")
elif(hex==04.2665):
    print("For the hex digit 04:26:65 the Manufacturer for this NIC card is Apple, Inc.")
elif(hex==04.3389):
    print("For the hex digit 04:33:89 the Manufacturer for this NIC card is Huawei Technologies Co.,Ltd")
elif(hex==00000):
    print("For the hex digit 00:00:0C the Manufacturer for this NIC card is Cisco Sysytems, Inc")
else:
    print("unknown Manufacturer")
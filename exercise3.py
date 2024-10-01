#Brody Burtis (Brody-Burtis)
#COP2002-0M1
#September 22, 2024
#exercise3
#To determine who the manufacturer for the NIC card is

#input statement that allows you to type in the NIC card to recieve information on who the manufactuerer is
NIC = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
#If elif statement that determines who the manufactuerer for the NIC card is, if unknown then gives an unknown number
if NIC == "00:00:17":
       print("For 00:00:17 the MAC manufacturer is Oracle.")
elif NIC == "00:07:E9":
       print("For 00:00:E9 the MAC manufacturer is Intel Corporation.")
elif NIC == "04:27:28":
       print("For 04:27:28 the MAC manufacturer is Microsoft Corporation.")
elif NIC == "04:26:65":
       print("For 04:27:28 the MAC manufacturer is Apple,Inc.")
elif NIC == ("04:33:89"):
       print("For 04:33:89 the MAC manufacturer is Huawei Technologies Co.,Ltd.")
elif NIC == "00:00:0C":
       print("For 00:00:0C the MAC manufacturer is Cisco Systems, Inc.")
else:
       print("Unknown")

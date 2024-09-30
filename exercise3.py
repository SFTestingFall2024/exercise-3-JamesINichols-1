def main():
     mac_manufacturers = {
         "00:00:17": "Oracle",
         "00:07:E9": "Intel Corporation",
         "04:27:28": "Microsoft Corporation",
         "04:26:65": "Apple, Inc.",
         "04:33:89": "Huawei Technologies Co.,ltd",
         "oo:00:0C": "Cisco Systems, Inc"
 
     }
     print("           MAC Manufacturer Program")
     print("------------------------")
     print()
     mac_prefix = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
     manufacturer = mac_manufacturers.get(mac_prefix, "Unknown")
     print(f"\nFor {mac_prefix} the MAC manufacturer is {manufacturer}.")
if(__name__=="__main__"):
     main()


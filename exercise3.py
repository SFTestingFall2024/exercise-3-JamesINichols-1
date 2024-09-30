Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     # Dictionary of known manufacturers
...     manufacturers = {
...         "00:00:17": "Oracle",
...         "00:07:E9": "Intel Corporation",
...         "04:27:28": "Microsoft Corporation",
...         "04:26:65": "Apple, Inc.",
...         "04:33:89": "Huawei Technologies Co.,Ltd",
...         "00:00:0C": "Cisco Systems, Inc."
...     }
... 
...     # Program header
...     print("MAC Manufacturer Program ------------------------\n")
... 
...     # User input
...     user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
... 
...     # Retrieve manufacturer or return 'Unknown'
...     manufacturer = manufacturers.get(user_input, "<Not valid value or not found>")
...     
...     # Output the result
...     print(f"For {user_input} the MAC manufacturer is {manufacturer}.")
... 
... if __name__ == "__main__":
...     main()

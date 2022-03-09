#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

# create a list of strings
vendors = vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "junmiper", "big_ip"]
# loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="")  # newline, print current vendor, and end without new line
    if x not in approvede_vendors:
        print(" - NOT AND APPROVED VENDOR!", end="")
print("\nOur loop has ended.")
           

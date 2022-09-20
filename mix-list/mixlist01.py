#!/usr/bin/env python3
'''Lab 15. Working with Lists'''

def main():
    
    # create a list with three values and assign to a variable
    my_list = ["192.168.0.5", 5060, "UP"]

    # print the list value at position 0
    print("The first item in the list (IP): " + my_list[0] )
    
    # print the list value at position positoion 1
    print("The second item in the list (port): " + str(my_list[1]) )

    # print the list value at position 3
    print("The last item in the list (state): " + my_list[2] )
    
    # Challenge 01 - given the list, display only the ip addresses on the screen
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

    # pritn usin an 'f-string'
    print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
if __name__ == "__main__":
    main()

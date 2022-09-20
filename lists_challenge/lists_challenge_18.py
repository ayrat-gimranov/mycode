#!/usr/bin/env python3
"""Lab 18. Lists Challenge"""

from random import choice

def main():
    
    wordbank = ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)
    num = input("Pick a number between 0 and 18\n Otherwise a random name will be chosen")
    if num.isdigit() and (num <= 18 and num >= 0):
        student_name = tlgstudents[num]
    else:
        student_name = random.choice(tlgstudents)
    
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")


if __name__ == "__main__":
    main()    

#!/usr/bin/python3

vampire_count = 0

with open("/home/student/mycode/sppoky-challenge/dracula.txt") as dracula_book:
    
    for line in dracula_book:
        if "vampire" in line.lower():
            vampire_count += 1


print("Vampire appears:", vampire_count)


#!/usr/bin/env python3
#username =rbhandari17@myseneca.ca
import sys

# Check for the correct number of arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assign the arguments to name and age
name = sys.argv[1]
age = sys.argv[2]

# Print the message
print(f"Hi {name}, you are {age} years old.")


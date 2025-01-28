#!/usr/bin/env python3

import sys

# Author: Your Full Name
# Author ID: Your Seneca ID
# Date Created: 2025/01/27

# Default timer value
timer = 3

if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Use the first argument as the timer

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")


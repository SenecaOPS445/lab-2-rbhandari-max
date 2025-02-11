#!/usr/bin/env python3

import sys

# Author: rojina bhandari
# Author ID: 143292233
# Date Created: 2025/02/11

# Default timer value
timer = 3

if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Use the first argument as the timer

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")


#!/usr/bin/env python3

import sys

# Author: Your rojina bhandari
# Author ID: 143292233
# Date Created: 2025/02/11

if len(sys.argv) < 2:
    print("Usage: ./lab2f.py <number>")
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")


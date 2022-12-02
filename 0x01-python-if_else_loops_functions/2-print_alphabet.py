#!/usr/bin/python3
num = 26

str = " "
x = ord('a') + num - 1
y = ord('a')

while (y <= x):
    str += chr(y)
    y += 1

print(f"{str}")

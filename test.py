import os
import shutil

# print('this is py')
# os.chdir('C:/')
# print(os.getcwd())

# look for all drives in the computer first
import string
from ctypes import windll
	
drives = []
bitmask = windll.kernel32.GetLogicalDrives()
for letter in string.ascii_uppercase:
    if bitmask & 1:
        drives.append(letter)
    bitmask >>= 1

print(drives)

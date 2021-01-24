# - to _
import os
files = os.listdir(".")

for filename in files:
    os.rename(filename, "_".join(filename.split(" ")))
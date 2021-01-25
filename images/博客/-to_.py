# - to _
import os
files = os.listdir(".")

for filename in files:
    os.rename(filename, "步骤_".join(filename.split("步骤")))

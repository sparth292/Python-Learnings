import os

directory = "/"

contents = os.listdir(directory)

print("Contents of the directory:", directory)
for item in contents:
    print(item)

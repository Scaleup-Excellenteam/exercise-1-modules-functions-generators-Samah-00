import os

dir_path = "./images"

# loop through all files in the directory
for file in os.listdir(dir_path):
    # for each file, check if its name starts with "deep"
    if file.startswith("deep"):
        print(file)

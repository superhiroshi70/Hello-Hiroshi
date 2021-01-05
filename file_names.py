import os
path = "C:\\Users\\hiroshi.okura"
files = os.listdir(path)

for f in files:
    if os.path.isfile(os.path.join(path, f)):
        print(f)

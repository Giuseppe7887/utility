import os


files = os.listdir()


i= 0
for file in files:
    if file != "rename.py" and not os.path.isdir(file):
        try:
            x = int(file.split(" ")[-1].split(".")[0])
            os.rename(file,f"{i}.png")
        except:
            pass
    i+=1

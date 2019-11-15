import os

totalSize = 0
folder = 'c:\\Users\\sudoh\\PythonScripts' # name of folder goes here

for filename in os.listdir(folder):
    if not os.path.isfile(os.path.join(folder, filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(folder, filename))

print(totalSize)

import os
from pyglet import image
print(os.getcwd())
directory = str(input("Please enter in the directory you wish to create a slideshow with, eg. user/desktop/folder: "))

while os.path.exists(directory) == False:
    directory = str(input("Invalid directory. Please try again: "))

for file in os.scandir(directory):
    if file.is_file():
        print(file.path)
    if file.endswith("jpeg"):
        pic = image.load(file)
        pic.blit(0,0,0)
    # if os.path.isfile(currentFile):
    #     print(currentFile)
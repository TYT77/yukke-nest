import glob
import os

folder = './images'
AddName = input('Input an additional name: ')

fileNames = glob.glob(os.path.join(folder, '*.png'))

for i, fileName in enumerate(fileNames):
    basename = os.path.basename(fileName)
    title, ext = os.path.splitext(basename)
    os.rename(fileName, os.path.join(folder, title + AddName + ext))
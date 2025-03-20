#!python3
#saves all possible crosspath combinations to a list, removing also duplicates
#cross paths are denoted with 3 number string sequences with first number being top path, second mid path and third bottom path

import os
import shutil

from PIL import Image


#sets working directory to whatever location this script is run from

NEW_RES = (1280, 720)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def scale_images():

    scaled_x = NEW_RES[0] / 1920
    scaled_y = NEW_RES[1] / 1080
    images = []

    paths = ['0-0-0']
    #Loops over 
    for n in range(0,6):
    #combinations of 0 crosspaths
        #0-0-x
        paths.append('0-0-'+str(n))
        #0-x-0
        paths.append('0-'+str(n)+'-0')
        #x-0-0
        paths.append(str(n)+'-0-0')

        #combinations of 1 to some crosspath
        #x-0-1
        paths.append(str(n)+'-0-1')
        #0-x-1
        paths.append('0-'+str(n)+'-1')
        #0-1-x
        paths.append('0-1-'+str(n))
        #x-1-0
        paths.append(str(n)+'-1-0')
        #1-x-x
        paths.append('1-'+str(n)+'-0')
        #1-0-x
        paths.append('1-0-'+str(n))

        #combinations of 2 to some crosspath
        #0-x-2
        paths.append('0-'+str(n)+'-2')
        #x-0-2
        paths.append(str(n)+'-0-2')
        #x-2-0
        paths.append(str(n)+'-2-0')
        #0-2-x
        paths.append('0-2-'+str(n))
        #2-x-0
        paths.append('2-'+str(n)+'-0')
        #2-0-x
        paths.append('2-0-'+str(n))

    #remove duplicates:
    # first turn 'paths' into dictionary with each paths element being key value
    # dictionary key values are unique so duplicates are removed. Values of this dictionary are None
    # then turn dictionary back to paths. Values of keys are ignored and paths returns all keys pathsed instead
    paths = list(dict.fromkeys(paths))
    paths.sort()

    #add all crosspaths to images
    images = paths

    #add round images
    for r in range(1, 101):
        images.append('r'+str(r)) 

    #add other images
    images.append('GoButton')
    images.append('sell_button')
    images.append('Victory')

    #scale all images and save them in desired resolution's folder
    os.chdir('..\\Images')
    if os.path.exists(str(NEW_RES[0])+'x'+str(NEW_RES[1])):
        print('Folder already exists, please delete it manually and run this script again.')
        return 
    os.mkdir(str(NEW_RES[0])+'x'+str(NEW_RES[1]))


    for im in images:
        os.chdir('Backups')

        temp = Image.open(im+'.png')
        os.chdir('..\\'+str(NEW_RES[0])+'x'+str(NEW_RES[1]))
        width, height = temp.size
        scaled = temp.resize((int(width * scaled_x), int(height * scaled_y)), resample = Image.Resampling.BOX)
        scaled.save(im+'.png')
    
        os.chdir('..\\')
    
scale_images()

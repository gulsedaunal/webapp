##!/usr/bin/python

import Config
import os
from fileInfo import FileInformation

def getImageList(directory, fileName):
    dirList = os.listdir(directory)
    imageList = []
    rImageName = ''

    for item in dirList:
        if item is not None and (item.lower().find('png') or item.lower().find('jpg')) and item.find(fileName) > -1:
            imageList.append(item)
            if item.lower().endswith('.jpg'):
                rImageName = item

    return imageList, rImageName

def getmp4List(directory):
    dirList = os.listdir(directory)
    rList = []
    imageList = []
    slowList = []
    #f = fileInfo


    for item in dirList:
        if item is not None and item.find('.mp4') > -1:
            if not item in rList:
                f = FileInformation()
                f.jpgFileList,\
                    f.jpgFileName = getImageList(directory + 'FRAMES/', item.replace('.mp4', ''))
                f.fileName = item.replace('.mp4', '')
                f.mp4FileName = item
                if len(imageList) > 0:
                    f.jpgFileName = imageList[0]
                rList.append(f)

    return rList


if __name__ == '__main__':
    values = getmp4List(Config.VIDEO_VIOLENT_FOLDER)
    for item in values:
        t = item
        print t.mp4FileName
        for i1 in t.jpgFileList:
            print '\t\t' + str(i1) + '\n'

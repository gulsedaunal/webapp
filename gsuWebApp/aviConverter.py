import cv2
import sys
import os

def convertVideoToImage(filename, fileNameFile, outputDirectory, numOfSecForSnapshot = 5):
    count = 1
    imgNum = 1
    vc = cv2.VideoCapture(filename)
    rval, frame = vc.read()
    if not rval:
        print 'Could not read file!'
        rval = False
    fileString = fileNameFile.split('.')[0]
    while rval:
        # Matematiksel olarak garanti veremem ama test ettiklerimde tam cikti.
        # Videolarin fps'inin 29 fps oldugunu varsayiyorum.
        if count % 25*numOfSecForSnapshot == 0:
            cv2.imwrite(outputDirectory + fileString + "%d.jpg" % imgNum,frame)
            imgNum += 1
        count += 1
        rval, frame = vc.read()
        cv2.waitKey(25)
    vc.release()
    print 'Done!'

if __name__ == '__main__':
    # filename = sys.argv[1]
    # outputDirectory = sys.argv[2]
    inputDirectory = '/home/ata/Desktop/seda/'
    filename = 'soccer.avi'
    outputDirectory = '/home/ata/Desktop/seda/'

    indir = '/home/ata/Desktop/seda/Gorseller/'
    for root, dirs, filenames in os.walk(indir):
        for dir in dirs:
            for root, dirs2, filenames2 in os.walk(indir + '/' + dir):
                for dir2 in dirs2:
                    #print indir + dir + '/' + dir2
                    for root,dirs3, filenames3 in os.walk(indir + dir + '/' + dir2):
                        for fn in filenames3:

                            #print indir+dir+'/'+dir2+'/'+fn
                            #print indir + dir+'/'+dir2
                            #convertVideoToImage(indir+dir+'/'+fn, fn, indir+dir, 1)
                            fileN = indir+dir+'/'+dir2+'/'+fn
                            outputDirectory = indir+dir+'/'+dir2+'/FRAMES/'
                            convertVideoToImage(fileN, fn, outputDirectory, 1)


    # absolute path of the file, output directory for images, num of seconds to take a snapshot
    #convertVideoToImage(inputDirectory + filename, filename, outputDirectory, 3)
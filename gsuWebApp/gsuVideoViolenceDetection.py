#!/usr/bin/python

from flask import Flask, request, session, render_template, \
    redirect, url_for, send_from_directory, send_file, current_app
import os
import pandas
import fileProcessing
from gsuWebApp import app
import fileInfo
import Config

#application = Flask(__name__)

from keras.models import load_model
import h5py
model = load_model('/home/ubuntu/Insight/mymodel.h5')

from PIL import Image
import os, os.path

def preprocess_input(x):
    x /= 255.
    x -= 0.5
    x *= 2.
    return x

from keras.preprocessing import image
import numpy as np

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video-violence-detection')
def vvd():
    nonviolentList = fileProcessing.getmp4List(Config.VIDEO_NON_VIOLENT_FOLDER)
    violentList = fileProcessing.getmp4List(Config.VIDEO_VIOLENT_FOLDER)


    return render_template('tmpGeneric.html', nvList = nonviolentList, vList = violentList)

@app.route('/video-violence-detection-detail')
def vvd_detail():
    nonviolentList = fileProcessing.getmp4List(Config.VIDEO_NON_VIOLENT_FOLDER)
    violentList = fileProcessing.getmp4List(Config.VIDEO_VIOLENT_FOLDER)
    if 'videoName' in request.args:
        videoName = request.args.get('videoName')
    imageList = []
    category = ''
    Npredictions = []
    Vprediction = [] 
    impath = ''

    for item in nonviolentList:
        if item.fileName == videoName:
            imageList = item.jpgFileList
            category = 'nonviolent'
	    impath = '/home/ubuntu/webapp/sedaweb/gsuWebApp/static/images/nonviolent/'	  
#  current_img = image.load_img(os.path.join('item', target_size=(299, 299))
          #  x = image.img_to_array(current_img)
          #  x = np.expand_dims(x, axis=0)
	  #  x = preprocess_input(x)
	  #  Npredictions.append(model.predict(x))

    for item1 in violentList:
        if item1.fileName == videoName:
            imageList = item1.jpgFileList
            category = 'violent'
	    impath = '/home/ubuntu/webapp/sedaweb/gsuWebApp/static/images/violent/'
    
    vidpath = os.path.join(impath,'FRAMES')
    print(vidpath)
    for i in imageList:
        current_img = image.load_img(os.path.join(vidpath,i), target_size=(299,299))
	x = image.img_to_array(current_img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)
	Npredictions.append(model.predict(x))
	
    probabilities = []
    probabilities = Npredictions
    # print str(len(imageList))
    return render_template('videoDetail.html', imageList=imageList, cat = category, prob=probabilities )

# if __name__ == '__main__':
#     #application.run(host='45.33.39.132', port=8080, debug=True)
#     application.run(debug=True)

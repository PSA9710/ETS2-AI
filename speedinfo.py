import cv2
import os
import numpy as np
import imageprocessing
from PIL import Image
import Global

def train():
    img=[]
    labels=[]
    speedRecognizer = cv2.face.LBPHFaceRecognizer_create()
    for filename in os.listdir(os.getcwd()+"/speeds"):
        image=cv2.imread(os.getcwd()+"/speeds/"+filename,cv2.IMREAD_GRAYSCALE)
        img.append(image)
        labels.append( int(filename.rsplit( ".", 1 )[ 0 ] ))
    speedRecognizer.train(img, np.array(labels))
    print('Training was succesful')
    speedRecognizer.write('speeds.spd')
    return speedRecognizer

def load():
    if os.path.exists('speeds.spd'):
        speedRecognizer = cv2.face.LBPHFaceRecognizer_create()
        speedRecognizer.read('speeds.spd')
        print('Speed detector loaded succesfully')
        Global.speed_recognizer=speedRecognizer
    else:
        Global.speed_recognizer= train()
    return
def train_speedlimit():
    img=[]
    labels=[]
    speedRecognizer = cv2.face.LBPHFaceRecognizer_create()
    for filename in os.listdir(os.getcwd()+"/speedlimits"):
        image=cv2.imread(os.getcwd()+"/speedlimits/"+filename,cv2.IMREAD_GRAYSCALE)
        img.append(image)
        labels.append( int(filename.rsplit( ".", 1 )[ 0 ] ))
    speedRecognizer.train(img, np.array(labels))
    print('Training speedlimiter was succesful')
    speedRecognizer.write('speedlimits.spd')
    Global.speed_limit_recognizer= speedRecognizer
    return

def load_speedlimit():
    if os.path.exists('speedlimits.spd'):
        speedRecognizer = cv2.face.LBPHFaceRecognizer_create()
        speedRecognizer.read('speedlimits.spd')
        print('Speed limit detector loaded succesfully')
        Global.speed_limit_recognizer=speedRecognizer
    else:
        train_speedlimit()
    return

""" def adjust_speed(img,region,speedrecognizer):
    img=imageprocessing.get_subimage(img,region)
    value=speedrecognizer.predict(img)
    print('You are crusing at {}'.format(value))
    return  """

def test():
    print('You are crusing at {} in a {} limit zone'.format(Global.speed_current,Global.speed_limit))
    return 
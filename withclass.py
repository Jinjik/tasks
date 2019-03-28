import cv2
import time
import os
from myclass import smart
from myclass import serv

#declaring variables
haarpath = '/home/pi/Documents/haarcascade_frontalface_default.xml'
sshkey = '/home/pi/Documents/sshkey1'
dirpath = '/home/pi/Documents/' #path to dir
imgname = ''
url = 'http://192.168.33.186/getUser/'
sshkey = '/home/pi/Documents/sshkey1'

faceDetect = cv2.CascadeClassifier(haarpath)#path to xmlfile
cam = cv2.VideoCapture(0)

#connect to server
serv.sercon('vm-smcoff', 'root', 'smart', sshkey)

while (True):
    print('loop')
    ret, img = cam.read()
    faces = faceDetect.detectMultiScale(
        img,
        scaleFactor = 1.2,
        minNeighbors = 2,
        minSize =(200,200)
        )
    #if catch image
    if (ret == True):
        #catch face
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0), 2)#catch face
            Data = time.strftime("%d.%b.%y - %H:%M:%S", time.localtime())
            imgname = Data +'.jpg'
            imgpath = dirpath + imgname #path until img
            serverpath = '/root/logic/history/data/' + imgpath
            cv2.imwrite(imgpath , img)
            cam.release()
            print(Data)
            d = {
                "url":Data
                }
            print(d)
            if imgname == '': #no face
                print('no face')
            else: #catch face
                serv.put(imgpath, serverpath)#transfering file to server
                print(smart.rs(url, d))
                os.remove(imgpath)#delete img
                cam = cv2.VideoCapture(0)
                time.sleep(5)
        
serv.close()
cam.release()
cv2.destroyAllWindows()

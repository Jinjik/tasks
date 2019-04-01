import json
import cv2
import time
import os
import paramiko
import requests

#description variables
haarpath = '/home/pi/Documents/haarcascade_frontalface_default.xml'
sshkey = '/home/pi/Documents/sshkey1'
dirpath = '/home/pi/Documents/' #path to dir
serverpath = '/root/logic/history/data/'
imgname = ''
url = 'http://www.hostname.org/getUser/'

faceDetect = cv2.CascadeClassifier(haarpath)
cam = cv2.VideoCapture(0) #turning on camera

#connect to server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('', username='', password='',key_filename=sshkey)
ftp = ssh.open_sftp()

while (True):
    ret, img = cam.read()
    faces = faceDetect.detectMultiScale(
        img,
        scaleFactor = 1.2,
        minNeighbors = 2,
        minSize =(180,180)
        )
    #if catch image
    if (ret == True):
        #catching face
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0), 2)#catch face
            Data = time.strftime("%d.%b.%y - %H:%M:%S", time.localtime())
            imgname = Data +'.jpg'
            imgpath = dirpath + imgname #path until img
            cv2.imwrite(imgpath , img)
            cam.release()
            print(Data)
            d = {
                "url":Data
                }
            print(d)
            if imgname == '': #no face
                print('no face')
            else: #caught face
                ftp.put(imgpath,serverpath+imgname)#transfering file to server
                r = requests.post(url, data=json.dumps(d))
                res = r.json()
                if 'name' in res.keys(): #key 'name' in res
                    print('Привет,' + res['name'].replace('_',' '))
                else:#no key 'name' in res
                    print("Ошибка распознования")
                os.remove(imgpath)#delete img
                cam = cv2.VideoCapture(0)
                time.sleep(5)
        
ftp.close()
cam.release()
cv2.destroyAllWindows()

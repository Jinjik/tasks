import json
import cv2
import time
import os
import paramiko
import requests

#declaring variables
haarpath = '/home/pi/Documents/haarcascade_frontalface_default.xml'
sshkey = '/home/pi/Documents/sshkey1'
dirpath = '/home/pi/Documents/' #path to dir
serverpath = '/root/logic/history/data/'
imgname = ''
url = 'http://192.168.33.186/getUser/'
print('var')#test
faceDetect = cv2.CascadeClassifier(haarpath)#path to xmlfile 
cam = cv2.VideoCapture(0) #turn on camera
print('cam')#test
#connect to server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('vm-smcoff', username='root', password='smart',key_filename=sshkey)
ftp = ssh.open_sftp()
print('ssh')#test
while (cam.isOpened()):
    print('here1')
    ret, img = cam.read()
    faces = faceDetect.detectMultiScale(
        img,
        scaleFactor = 1.2,
        minNeighbors = 2,
        minSize =(180,180)
        )
    print('here2')#test
    #if catch image
    if (ret == True):
        #catch face
        print('here3')#test
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
            else: #catch face
                print('here5')#test
                ftp.put(imgpath,serverpath+imgname)#transfering file to server
                r = requests.post(url, data=json.dumps(d))
                res = r.json()
                print('here6')#test
                if 'name' in res.keys(): #key 'name' in var res
                    print('Hello,' + res['name'].replace('_',' '))
                else:#no key 'name'
                    print("Кто ты кожанный ублюдок?")
                os.remove(imgpath)#delete img
            cam = cv2.VideoCapture(0)
            time.sleep(5)
            print('here7')#test
        
ftp.close()
cam.release()
cv2.destroyAllWindows()



import json
import cv2
import time
import os
import paramiko
import requests

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('vm-smcoff', username='root', password='smart',key_filename='/home/pi/Documents/sshkey1')
ftp = ssh.open_sftp()
c = 0

headers = {
    'Content-type':'application/json',
    'Accept':'text/plain',
    'Content-Encoding':'utf-8'}
data = [
    ('some_more_field', 'some_field_data')
    ]
while (cam.isOpened()):
    print('here')
    ret, img = cam.read()
    faces = faceDetect.detectMultiScale(
        img,
        scaleFactor = 1.2,
        minNeighbors = 2,
        minSize =(20,20)
        )
    if (ret == True):
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0), 2)
            Data = time.strftime("%d.%b.%y - %H:%M:%S", time.localtime())
            global imgname
            imgname = ''
            imgname = Data +'.jpg'
            cv2.imwrite(imgname , img)
            cam.release()
            c+=1
            print(Data)
            d = {
                "url":Data
                }
            print(d)
            if imgname == '':
                continue
            else:
                ftp.put('/home/pi/Documents/'+imgname,'/root/logic/history/data/'+imgname)
                url1 = 'http://192.168.33.186/getUser/'
                r = requests.post(url1, data=json.dumps(d))
                res = r.json()
                if 'name' in res.keys():
                    print('Hello,' + res['name'].replace('_',' '))
                else:
                    print("Кто ты кожанный ублюдок?")
                path = os.path.join(os.path.abspath(os.path.dirname('/home/pi/Documents/')), imgname)
                os.remove(path)
        if c == 1:
            cam = cv2.VideoCapture(0)
            c = 0
            time.sleep(10)
            continue
        

ftp.close()


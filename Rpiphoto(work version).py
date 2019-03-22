import json
import cv2
import time
import os
import paramiko
import socket
import requests

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('vm-smcoff', username='root', password='smart',key_filename='/home/pi/Documents/sshkey1')
ftp = ssh.open_sftp()

sampleNum = 0


while (True):
    ret, img = cam.read()
    faces = faceDetect.detectMultiScale(
        img,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize =(200,200)
        )
    for (x, y, w, h) in faces:
        sampleNum += 1
        Data = time.strftime("%d.%b.%y - %H:%M:%S", time.localtime())
        imgname = Data +'.jpg'
        imgname2 = Data
        cv2.imwrite(Data + ".jpg" , img[y:y + h, x:x + w])
        cv2.rectangle(img, (x,y), (x + w, y + h), (255,0,0),2)
        cv2.waitKey(100)
    if (sampleNum == 1):
        ftp.put('/home/pi/Documents/'+imgname,'/root/logic/history/data/'+imgname)
        url = 'http://192.168.33.186/getUser/' + imgname2
        r = requests.post(url)
        print(json.loads(r))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), imgname)
        os.remove(path)
        time.sleep(5)
        sampleNum = 0
        continue

ftp.close()
cam.release()
cv2.destroyAllWindows()

import numpy as np
import cv2
import time
import os
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('vm-smcoff', username='root', password='smart',key_filename='/home/pi/Documents/sshkey1')
ftp = ssh.open_sftp()
Data = time.strftime("%d.%b.%y - %H:%M:%S", time.localtime())
imgname = Data+'.jpg'
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), imgname)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sampleNum = 0
cam = cv2.VideoCapture(0)

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
        cv2.imwrite(Data + ".jpg" , img[y:y + h, x:x + w])
        cv2.rectangle(img, (x,y), (x + w, y + h), (255,0,0),2)
        cv2.waitKey(100)
        cv2.imshow("Face", img)
        cv2.waitKey(1)
    if (sampleNum == 1):
        time.sleep(3)
    elif (sampleNum == 2):
        ftp.put('/home/pi/Documents/'+imgname,'/root/SCM_Project/foto/'+imgname)
        time.sleep(30)
        os.remove(path)
        sampleNum = 0
    
ftp.close()
cam.release()
cv2.destroyAllWindows()

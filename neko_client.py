import requests
import time
import threading
import logging
from yaspin import yaspin
import random
from ytlv import *
class use_neko:
    def __init__(self):
        self.link="http://127.0.0.1:5000/neko"
        self.control_q2=0
        self.control_q3=False
        self.control_code=0
        self.status_code=False
        self.server_count=0
    def control(self):
        q1=input("請輸入連結網址(link)")
        q2=input("請輸入黃金潮(數字)")
        self.control_q2=q2
        q3=input("請輸入是否啟用極限模式(yes/no)")
        if q1 != None:
            self.link=q1
        if q3=="yes":
            self.control_q3=True
            print("祝你好運")
        elif q3=="no":
            self.control_q3=False
            print("O K !")
        else:
            print("你說啥?")

        with yaspin(text="加載配置中", color="yellow") as spinner:
            if self.control_q3==True:
                lv=islive()
                lv.lvgetproxy()
            time.sleep(1)
            spinner.ok("✅ ")
            time_start = time.time()            
            self.neko_count(time_start)
            
            

    def neko_count(self,time_start):
        while True:
            time_end = time.time()
            losttime=time_end-time_start
            lostminute=int(losttime/60)
            if lostminute<=5 and self.status_code==False :
                self.start(1)
            elif lostminute>=5 and lostminute<=10 and self.status_code==False:
                self.control_code=1
                self.start(2)
                
    def start(self,control):
        print(f"start:{control}")        
        time.sleep(1)
        if control==1:
            self.control_code=0
            threading.Thread(target=self.server01,  args=()).start()
        if control==2:
            self.control_code=0
            threading.Thread(target=self.server02,  args=()).start()
        if control==3:
            self.control_code=0
            threading.Thread(target=self.server03,  args=()).start()
        if control==4:
            self.control_code=0
            threading.Thread(target=self.server04,  args=()).start()

    def server01(self):
        print("start server01")
        while True:
            r = requests.get(self.link)
            rt=random.randint(1,2)
            self.status_code=True
            if r.status_code!=200:
                print("失去訂單")
            if self.control_code==1:
                self.status_code=False
                print("break server01")
                break
            time.sleep(rt)

    def server02(self):
        print("start server02")
        while True:
            r = requests.get(self.link)
            self.status_code=True
            if r.status_code!=200:
                print("失去訂單")
            if self.control_code==1:
                self.status_code=False
                print("break server02")
                break
            time.sleep(1)

    def server03(self):
        while True:
            r = requests.get(self.link)
            self.status_code=True
            if r.status_code!=200:
                print("失去訂單")
            if self.control_code==1:
                self.status_code=False
                break
            

    def server04(self):
        while True:
            r = requests.get(self.link)
            self.status_code=True
            if r.status_code!=200:
                print("失去訂單")
            if self.control_code==1:
                self.status_code=False
                break
            
            
    

if __name__ == '__main__':
    time_start = time.time()
    neko=use_neko()
    # neko.control()
    # neko.neko_count(time_start)
    neko.control()


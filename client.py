import  grequests
import uuid
import threading
import os
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





class show():


    def __init__(self,mod):

        self.mod = mod
        self.windows()
        

    def windows(self,count,success,fail):
        self.clean()
        print(fr'''
        -------------------------------------------------
        |  目前狀態: {self.mod}                                    |
        |  目前次數: {count}                                    | 
        |  成功: {success}                                       |
        |  失敗: {fail}                                       |
        ------------------------------------------------
        ''')

    def clean(self):
        os.system('cls')

class neko():


    def setUp(self):
        return

class base64():

    def __init__(self):
        self.url = None
        self.power = None
        self.long = None
        self.count = 0
        self.success = 0
        self.fail = 0
        self.ws = show("base64")


    def setUp(self):
        self.url = input("請輸入網址")
        self.power = input("請輸入強度1~100")
        self.long = input("請輸入長度1~20")
        self.start()
        

    def start(self):
        while True:
            for i in range(self.power):
                self.send()


    def send(self):
        links = []
        answer = []
        for i in range(int(self.long)):
            randomthing=str(uuid.uuid4())
            randomthing=randomthing.encode('utf8')
            outdata = base64.b64encode(randomthing)
            links.append(f"{self.url}/base64?base64={outdata}")
            answer.append(randomthing)

        reqs = (grequests.get(link) for link in links)
        responses = grequests.imap(reqs,grequests.Pool(len(links)))
        self.response(responses,answer)

    def update(self):
        self.ws.windows(self.count,self.success,self.fail)


    def response(self,response,answer):
        now = 0
        for i in response:
            if i.text == answer[now]:
                print(f"第{self.count}次成功")
                self.count += 1
                self.success += 1
                now += 1
                self.update()
            else:
                print(f"第{self.count}次失敗")
                self.count += 1
                self.fail += 1
                now += 1
                self.update()



if __name__ == '__main__':
    mod = input("請輸入模式 base64/neko")
    if mod == "neko":
        nekoo = neko()
        nekoo.setUp()

    elif mod == "base64":
        b64 = base64()
        b64.setUp()
    else:
        print("輸入錯誤")
    















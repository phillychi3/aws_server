import socket
import time
import threading
import base64
import random



class shopping:

    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 6666
        self.istop=False
    def start(self):
        print("start")
        threading.Thread(target=self.crazy_shopping,  args=()).start()


    def stop(self):
	# 記得要設計停止無限迴圈的開關。
        self.isstop = True
        print('STOP carzy shopping')

    def send(self):
        r=random.randint(1,50)
        f = open('shop.txt','rb')
        k = f.readlines()
        thing=(k[r])
        outdata = base64.b64encode(thing)        
        print('send: ' + outdata.decode())
        # try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        s.send(outdata)
        # except:
        #     print("can't connect server LOL")
        start = time.process_time()
        while True:
            indata = s.recv(1024)
            end = time.process_time()
            if len(indata) == 0: # connection closed
                s.close()
                print('server closed connection.')
                break
            if start-end>1:
                s.close()
                print("false")
                break
            print('recv: ' + indata.decode())

    def crazy_shopping(self):
        while(not self.istop):
            lol=shopping()
            lol.send()
            time.sleep(0.1)


run=shopping()
run.start()



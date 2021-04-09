import requests
import time
import threading




class use_neko:
    def __init__(self):
        self.link="http://127.0.0.1:5000/neko"


    def neko_count(time_start):
        while True:
            time_end = time.time()
            losttime=time_start-time_end
            


    def start(self):
        print("start")
        threading.Thread(target=self.go,  args=()).start()

    def go(self):
        while True:
            r = requests.get(self.link)
            print(r)


if __name__ == '__main__':
    time_start = time.time()
    neko=use_neko()
    neko.neko_count(time_start)


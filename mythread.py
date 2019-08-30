from threading import Thread

class MyThread(Thread):
    def run(self):
        for j in range(10000):
            print(j,"from",self.getName())


for i in range(16):
    MyThread().start()
import threading

from threading import Thread
import time

class Mythread(Thread):

    def run(self):
        for i in range(5):
            time.sleep(2)
            print(i,"child Thread")

t1 = Mythread()
t1.start()
t1.join()


t2 = Mythread()
t2.start()
t2.join()
from  threading import Thread

class Mythread(Thread):

    def __init__(self,eid,ename):
        Thread.__init__(self)
        self.eid = eid
        self.ename = ename

    def run (self):
        print(self.eid,self.ename)


t = Mythread(101,"name one")
t.start()

t = Mythread(102,"name two")
t.start()
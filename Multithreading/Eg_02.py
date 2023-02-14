import threading

t1 = threading.Thread()
t1.name = "new thread"
print(t1.name)

t2 = threading.Thread()
t2.name = " new thread 2"
print(t2.name)

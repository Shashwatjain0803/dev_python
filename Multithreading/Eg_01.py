import threading

t = threading.current_thread().name
print(t) #Mainthread

t = threading.main_thread().name
print(t)

if threading.current_thread() == threading.main_thread():
    print("main method executed")
else:
    print("some other threading")
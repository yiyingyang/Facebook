import threading, time

class MyThread(threading.Thread):
    def run(self):
        global num
        global lock
        time.sleep(1)
        if lock.acquire(): 
            num = num + 1
            msg = self.name + 'set num to' + str(num)
            print(msg)
            time.sleep(4)
            lock.release()
        
num = 0    
lock = threading.Lock()

def main():
    for _ in range(5):
        t = MyThread()
        t.start()
main()



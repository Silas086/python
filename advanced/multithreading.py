import time
import threading
number = 100
#a继承threading.Thread类时会自动运行其父类的run()（abstract方法),所以需要重写run()
class a(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def consume(self):
        global number       
        for i in range(100):
            if number>0:
                number -= 1
                print(f"{self.name}:{number}")
                time.sleep(0.1)
    def run(self):
        self.consume()

#创建线程
t1=a("t1")
t2=a("t2")

t1.start()
t2.start()
print(threading.active_count())
#结束线程
t1.join()
t2.join()
print(f"最终结果: number = {number}")

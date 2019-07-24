
import threading
import time
def fun1(a, b):
  c = a + b
  time.sleep(2)
  print(c)
thread1 = threading.Thread(target = fun1, args = (12, 10))
thread1.start()
print(2)
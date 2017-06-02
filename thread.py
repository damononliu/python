import threading
import time

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, id):
		super(MyThread, self).__init__()
		self.id = id
	
	def run(self):
		x = 0
		time.sleep(10)
		print self.id

if __name__ == '__main__':
	t1 = MyThread(999)
	t1.setDaemon(True)
	t1.start()
	#t1.join()
	for i in range(5):
		print i
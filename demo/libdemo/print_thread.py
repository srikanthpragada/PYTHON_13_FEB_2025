import threading
from threading import Thread

print('In Main Thread!')

class PrintThread(Thread):
    def run(self):
        for n in range(1, 26):
            print(f'Print {n}')


pt = PrintThread()
pt.start()

for n in range(1, 26):
    print(f'Main {n}')

print('End of Main')

import multiprocessing
from time import sleep,ctime


class ClockProcess(multiprocessing.Process):
    '''
    :param multiprocessing:
    :return:
    '''

    def __init__(self,interval):
        super().__init__()
        self.interval=interval

    def run(self):
        while True:
            print("this time is %s" %ctime())
            sleep(self.interval)

if __name__=='__main__':
    p=ClockProcess(3)
    p.start()


    while True:
        print('sleeping...')
        sleep(1)
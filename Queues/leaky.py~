from collections import deque
import threading, time
class LeakyBucket:
    '''the leaky bucket throttling the bit rate'''

    def __init__(self, node, bitsPerSec, measIntv, LBtype):
        self.node = node
        self.bitsPerSec = bitsPerSec  #the rate limit
        self.measIntv = measIntv      #the measure interval, tokens will become full at the beginning of each interval
        self.LBtype = LBtype          #the type of the bucket  
        self.lastTime = 0             #the start time of the last measure interval
        self.bitsDone = 0             #the bits that have been transmitted
        self.BDLock = threading.Lock() #the lock for the bits sent
        self.packDQ = deque()          #the packet Q 
        self.maxToken = bitsPerSec*float(measIntv)  #the max token (bits)
        self.token = self.maxToken      #the current token
        self.condition = threading.Condition()  #sync lock


    def packIn(self, msg):
        '''Insert a packet'''
        self.condition.acquire()
        self.packDQ.append(msg)
        self.condition.notify()
        self.condition.release()

    def keepPoping(self):
        '''keep poping new pack'''
        self.lastTime = time.time()   #record the start time
        while True:
            timeNow = time.time() 
            if  timeNow - self.lastTime > self.measIntv:     
                #new intv, need to reset token
                self.token = self.maxToken
                self.lastTime = timeNow
            self.condition.acquire()
            if self.packDQ: # the queue is not empty
                pack = list(self.packDQ)[0]
                packLen = len(pack[2])*8
                if  packLen > self.token:   #no enough token?
                    #self.packDQ.popleft()
                    self.condition.release()
                    time.sleep(max(self.lastTime+self.measIntv-time.time(),0)) #wait for enough token
                else:              #enough token, can send out the packet
                    self.packDQ.popleft()
                    self.condition.release()
                    self.changeBitsDone(packLen)
                    self.token = self.token - packLen #consume token
            else:
                self.condition.wait()
                self.condition.release()

    def begin(self):
        '''begin the leakybucket'''
        aThread = threading.Thread(target = self.keepPoping, args = [])
        aThread.start()


    def getBitsDone(self):
        '''get and reset bitsDone, for testing'''
        self.BDLock.acquire()
        reV = self.bitsDone
        self.bitsDone = 0
        self.BDLock.release()
        return reV

    def changeBitsDone(self,length):
        '''change bitsDone, for testing'''
        self.BDLock.acquire()
        self.bitsDone += length
        self.BDLock.release()

    def measure(self, intv):
        '''measure the throughput of the leaky bucket'''
        while True:
            bitsDone = self.getBitsDone()
            rate = bitsDone / float(intv*1024)
            print 'rate: %.2f' % rate
            time.sleep(intv)

    def startMeasure(self, intv):
        '''start measure the rate'''
        #print 'here'
        aThread = threading.Thread(target = self.measure, args = [intv])
        aThread.start()        

#===============================
def main():
    pack = 1000*'a'
    msg = ('192.168.1.1', 16000, pack)
    print 'here'
    LB = LeakyBucket(None, 500*1024, 1, 'reg')
    LB.begin()
    LB.startMeasure(10)
    numMsg = 0

    while numMsg < 10000:
        LB.packIn(msg)
        #print 'pack in'
        numMsg += 1

if __name__ == '__main__':
    main()

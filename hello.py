#!/usr/bin/python
from time import sleep

def SecondsSinceDockerStarted():
    i=0
    while True:
        print "seconds since docker start %d" % (i)
        sleep(1)
        i=i+1
        
if __name__=="__main__":
    SecondsSinceDockerStarted()
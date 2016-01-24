# -*- coding:utf-8 -*-
import settings
import datetime
import glob
import os


if settings.DEBUG:
    #clean other log
    logs = glob.glob(settings.LOG_PATH + "/*.log")
    for log in logs:
        if log[-10:] <> "server.log":
            os.remove(log)



logfile = settings.LOG_PATH + "/"+ datetime.datetime.now().isoformat() + ".log"
logf = open(logfile,'w+')
logbase = open(settings.LOG_PATH + "/server.log",'a+')



def writelog(logstr,debuglevel):
    now = datetime.datetime.now().isoformat() 
    if debuglevel == 1:
        logbase.write("[%s] %s \n" %(now, logstr))
        logbase.flush()
    elif debuglevel >= settings.LOG_LEVEL:
            logf.write("[%s] %s \n" %(now, logstr))
            logf.flush()

def writebaselog(logstr):
    writelog(logstr,1)

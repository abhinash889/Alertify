# @Author: ganeshkumarm
# @Date:   2016-11-19T19:20:11+05:30
# @Last modified by:   ganeshkumarm
# @Last modified time: 2016-11-19T19:20:45+05:30

#Built in modules
import os
import sys
import time
import subprocess
import datetime

#Used defined module
import exception

class Notify(object):
    def __init__(self):
        self.title = 'Notification From Notify'

    def counter(self, notify_time):
        s = 59
        m = notify_time - 1
        while s >= 00:
            if m == -1:
                print "Completed"
                print "Bye"
                return
            os.system('clear')
            print "Notify"
            print "Notification in %d minutes %d seconds ..." % (m, s)
            time.sleep(1)
            s -= 1
            if s == 0:
                s = 59
                m -= 1

    def sleep_time(self, notify_time):
        try:
            time.sleep(notify_time  * 60)
        except Exception, e:
            print e

    def sendNotification(self, message, start_time):
        try:
            end_time = datetime.datetime.now()
            diff_time_in_delta = end_time - start_time
            diff_time_in_mins = divmod(diff_time_in_delta.days * 86400 + diff_time_in_delta.seconds, 60)
            diff_time_msg = ' (Set ' + str(diff_time_in_mins[0]) + ' minutes ' + str(diff_time_in_mins[1]) + ' seconds ago)'
            os.system('notify-send "'+self.title+diff_time_msg+'" "'+message+'"')
        except Exception, e:
            print e

if __name__ == "__main__":
        try:
            counter_flag = True
            notify = Notify()
            notify_time = sys.argv[1]

            if not notify_time.isdigit():
                try:
                    raise exception.InvalidArgument("Time parameter must be a positive integer value")
                except exception.InvalidArgument, e:
                    print e.args
                    print "Exiting ...."
                    sys.exit()
            notify_time = int(sys.argv[1])

            if sys.argv[len(sys.argv) - 1] == '--no-counter':
                message = ' '.join([sys.argv[i] for i in range(2, len(sys.argv) - 1)])
                counter_flag = False
            else:
                message = ' '.join([sys.argv[i] for i in range(2, len(sys.argv))])
            start_time = datetime.datetime.now()

            if counter_flag:
                notify.counter(notify_time)
            else:
                    notify.sleep_time(notify_time)
                    
            notify.sendNotification(message, start_time)
        except KeyboardInterrupt:
            print "\nQuitting ..."
            print "Bye"
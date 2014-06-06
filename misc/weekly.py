#-*- coding: UTF-8 -*-

import os, os.path
import os.path, time
import datetime


if __name__ == '__main__':

    import os
    from os.path import join, getsize
    time_stamps = {}
    for root, dirs, files in os.walk('E:\Dropbox\weekly'):
        print files
        print root, "consumes",
        print sum(getsize(join(root, name)) for name in files),
        for dir in dirs:
            print root
            print 'dir:{}'.format(join(root,dir))
        for name in files:
            #print type(name)
            #print 'file:{}'.format(join(root,name.decode("gb2312")))
            #print name.encode('gb2312')
            print name.decode("gb2312")
            full_path = join(root,name.decode("gb2312"))
            print full_path
            if full_path.lower().endswith(('.doc','docx')):
                time2 = os.path.getmtime(full_path)
                print "last modified: %s" % time.ctime(time2)
                time_stamps[full_path] = time2
            #print name.encode('utf-8')
            #print name.decode('utf-8')
            #print name.decode('utf-8')
        print "bytes in", len(files), "non-directory files"
    print time_stamps
    print '************'
    #print max(time_stamps)
    import operator
    latest_weekly = max(time_stamps.iteritems(), key=operator.itemgetter(1))[0]

    src = 'E:\Dropbox\weekly\y2014\王旭平周报_20140425.doc'.decode('utf-8')
    time1 = os.path.getmtime(src)
    print "last modified: %s" % time.ctime(time1)
    print "created: %s" % time.ctime(os.path.getctime(src))

    src2 = 'E:\Dropbox\weekly\y2014\王旭平周报_20140530.doc'.decode('utf-8')
    time2 = os.path.getmtime(src2)
    print "last modified: %s" % time.ctime(os.path.getmtime(src2))
    print "created: %s" % time.ctime(os.path.getctime(src2))

    print time2>time1
    today = datetime.date.today().strftime("%Y%m%d")

    #print "last modified2: %s" % time.ctime(os.path.getmtime(src2))
    import shutil
    import os.path
    current_file = 'E:\Dropbox\weekly\y2014\weekly_'+today+'.doc'
    print current_file
    if os.path.isfile(current_file):
        os.remove(current_file)

    shutil.copy2(latest_weekly,current_file)







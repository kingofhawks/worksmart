import json

def get_bugs():
    base_url = 'http://192.168.153.214:9997/redmine/issues.json?project_id=wxkcsj&offset=0&limit=100&sort=id:desc'
    import requests
    r = requests.get(base_url+'&status_id=*')
    #print r.status_code
    #print r.encoding
    #print type(r.text)
    #print r.text.encode('utf-8')
    d = json.loads(r.text.encode('utf-8'))
    total_bugs = int(d['total_count'])
    print 'total bugs:{}'.format(total_bugs)
    #print len(d['issues'])
    r = requests.get(base_url+'&status_id=closed')
    d = json.loads(r.text.encode('utf-8'))
    closed_bugs = int(d['total_count'])
    print 'closed bugs:{}'.format(closed_bugs)
    #print len(d['issues'])
    percentage = closed_bugs*1.0/total_bugs
    print 'fix percentage:{}'.format(percentage)
    r = requests.get(base_url+'&status_id=open')
    d = json.loads(r.text.encode('utf-8'))
    print 'open bugs:{}'.format(d['total_count'])
    #print len(d['issues'])
    import arrow

    return {'total':total_bugs,'closed':closed_bugs,'percentage':percentage,'open':d['total_count'],'date':arrow.now().datetime}


if __name__ == '__main__':
    bug = get_bugs()
    print bug



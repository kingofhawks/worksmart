__author__ = 'user'
with open("ztz2014_sz.txt") as f:
    content = f.readlines()
    total = 0.0
    for line in content:
        value = float(line.strip())
        # print value
        if value >2001200:
            print '*'*10
            print value
        elif value > float(1000000):
            print value
            value = value/10000
            # print value
        total+=value
    print '*'*30
    print total


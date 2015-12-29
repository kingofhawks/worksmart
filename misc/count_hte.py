__author__ = 'user'
with open("hte2015_dx.txt") as f:
    content = f.readlines()
    total = 0.0
    for line in content:
        value = float(line.strip())
        # print value
        if value > float(10000):
            print value
            value = value/10000
            print value
        total+=value
    print '*'*30
    print total


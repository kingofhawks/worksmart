#-*- coding: UTF-8 -*-
# int('14,597'.replace(',', ''))
with open("2015jzgc_dx.txt") as f:
    content = f.readlines()
    total_hte = 0.0
    total_ztz = 0.0
    total_area = 0
    amount = 0
    for line in content:
        # print line.strip()
        words = line.split("\t")
        # print words
        number = words[0]
        # print number
        hte = float(words[5])
        ztz = float(words[6])
        scale = words[2]
        unit = words[4]
        if unit.find('平方米') != -1 and len(words[3])>0:
            area = float(words[3])
            total_area += area
            # print '****area{}'.format(area)
        else:
            area = 0
        company = ''
        # area = 0.0
        if company.find('江苏国泰新点软件有限公司') != -1:
            print words
            continue
        # print 'hte:{} ztz:{} scale:{}'.format(hte, ztz, scale)
        # temp = scale.split("|")
        # # print 'haha:{}'.format(scale.find('平方米'))
        # if len(temp) == 2 and scale.find('平方米') != -1:
        #     temp2 = temp[1].split('平方米')
        #     # print temp2
        #     # print temp2.replace('平方米', '')
        #     try:
        #         area = float(temp2[0].replace(',', ''))
        #         # area = int(temp2[0].replace(',', ''))
        #         total_area += area
        #     except ValueError as e:
        #         print e

        #
        # else:
        #     area = 0

            # print ' total_are:{}'.format(total_area)
        # print scale.find('小型')
        if ztz > 100000:
            print 'hah****{}'.format(ztz)
        if hte > 10000:
            print '***large hte:{} ztz:{} scale:{} area:{}'.format(hte, ztz, scale, area)
            hte = hte/10000
        if scale.find('小型') != -1 and area > 100000:
            print '*** small hte:{} ztz:{} scale:{} area:{}'.format(hte, ztz, scale, area)
        if scale.find('小型') != -1 and ztz > 1000000:
            print '*** small but large ztz {}'.format(ztz)
            ztz = ztz/10000
        elif ztz > 10000000:
            print '***** too large***{}'.format(ztz)
            ztz = ztz/10000
        elif ztz > 500000 and hte < 100:
            print '*** medium large hte:{} ztz:{} scale:{} area:{}'.format(hte, ztz, scale, area)
            ztz = ztz/10000
        total_hte += hte
        total_ztz += ztz
        amount += 1
        # print 'ztz:{} total:{}'.format(ztz, total_ztz)

    print 'total_hte:{} total_ztz:{}  total_area:{} amount:{}'.format(total_hte, total_ztz, total_area, amount)



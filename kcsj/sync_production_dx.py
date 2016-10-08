# -*- coding:utf-8 -*-
import pyodbc


def get_area(scale):
    area = 0
    temp = scale.split("|")
    if len(temp) == 2 and scale.find(u'平方米') != -1:
        temp2 = temp[1].split(u'平方米')
        try:
            area = float(temp2[0].replace(',', ''))
        except ValueError as e:
            print e
    return area

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.153.189;PORT=1433;DADABASE=Epoint_WXKCSJ;UID=sa;PWD=wxjsj^20150326')
cursor = cnxn.cursor()

cursor.execute("select * from Epoint_WXKCSJ.dbo.ZZHY_DXSQB where SHDate>='2016-09-01' and SHDate<'2016-10-01'  order by SHDate desc")
# SELECT * FROM Epoint_WXKCSJ.dbo.ZZHY_DXSQB order by operatedate desc
# row = cursor.fetchone()
# print row
# print row[1]
rows = cursor.fetchall()
result = {}
for row in rows:
    print row[78], row[73], row[82], row[83], row[84]
    industry = row[78]
    if result.get(industry):
        value = result.get(industry)
        result.update({industry: {'count': value['count']+1, 'htje': row[82]+value['htje'],
                                  'investment': row[83]+value['investment'],
                                  'area': row[73]+value['area']}})
        # print industry, result.get(industry)
    else:
        result.update({industry: {'count': 1, 'htje': row[82], 'investment': row[83], 'area': row[73]}})

for industry in result:
    print industry, result.get(industry)



import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.153.196;PORT=1433;DADABASE=WXJS_XYPJ;UID=sa_wx;PWD=wxzjj!123123')
cursor = conn.cursor()


def get_good_info(corp_code, good_type):
    good_score = 0
    # TODO 区分勘察设计
    sql = "select * from WXJS_XYPJ.dbo.CorpGoodCreditInfo where Status=30 and offdate>'2018-09-30' and CorpName='{}' and GoodName in ('{}')".format(corp_code, good_type)
    print(sql)
    cursor.execute(sql)
    rows = cursor.fetchall()
    # 科技创新分开两部分分别计算并加起来
    kjcx1 = 0
    kjcx2 = 0
    # 社会责任分开两部分分别计算并加起来
    shzr1 = 0
    shzr2 = 0
    for row in rows:
        # print(row)
        score = float(row[39])
        bh = row[40]
        good_score += score
        if bh == '4-6' or bh == '4-7' or bh == '4-8' or bh == '4-9':
            kjcx1 += score
            if kjcx1 >= 3:
                kjcx1 = 3
        elif bh == '4-10':
            kjcx2 += score
            if kjcx2 >= 3:
                kjcx2 = 3
        elif bh == '4-13':
            shzr1 += score
            if shzr1 >= 3:
                shzr1 = 3
        elif '社会责任' in good_type:
            shzr2 += score

    if '科技创新' in good_type:
        good_score = kjcx1+kjcx2
    elif '社会责任' in good_type:
        good_score = shzr1+shzr2

    if '争先创优' in good_type and good_score >= 10:
        good_score = 10
    elif '科技创新' in good_type and good_score >= 5:
        good_score = 5
    elif '社会责任' in good_type and good_score >= 5:
        good_score = 5

    print('kjcx1:{} kjcx2:{} shzr1:{} shzr2:{} score:{} row:{} good_type:{}'.format(kjcx1, kjcx2, shzr1, shzr2, good_score, len(rows), good_type))
    return good_score


def get_bad_info(corp_code, zz_type):
    bad_score = 0
    # SQL must with dbName.dbo.table
    if zz_type == 'sj':
        cursor.execute("select * from WXJS_XYPJ.dbo.CorpBadCreditInfo where Status=30 and sjname='{}'".format(corp_code))
    else:
        cursor.execute(
            "select * from WXJS_XYPJ.dbo.CorpBadCreditInfo where Status=30 and kcname='{}'".format(corp_code))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return bad_score


def get_bad_standard():
    cursor.execute("select * from WXJS_XYPJ.dbo.blxw_sonbh")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def get_project():
    pass


def get_score(corp_name):
    # get_bad_standard()
    good_score = get_good_info(corp_name, '''争先创优','争先创优（最高得分不超过10分）''')
    good_score = good_score + get_good_info(corp_name, '''科技创新','科技创新（最高得分不超过5分）''')
    good_score = good_score + get_good_info(corp_name, '''社会责任', '社会责任（最高得分不超过5分）''')
    bad_score = get_bad_info(corp_name, 'sj')
    score = 100 + good_score - bad_score
    print(score)
    return score


def get_scores(corp_names):
    result = []
    for corp_name in corp_names:
        result.append(get_score(corp_name))
    return result


corp_names = []
corp_names.append('无锡市政设计研究院有限公司')
corp_names.append('江苏中设集团股份有限公司')
corp_names.append('江苏中锐华东建筑设计研究院有限公司')
corp_names.append('无锡市园林设计研究院有限公司')
corp_names.append('无锡市建筑设计研究院有限责任公司')
corp_names.append('江苏省科佳工程设计有限公司')
corp_names.append('美尚生态景观股份有限公司')
corp_names.append('无锡水文工程地质勘察院')
corp_names.append('南京南大岩土工程技术有限公司')
scores = get_scores(corp_names)
print(scores)


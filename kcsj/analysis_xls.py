# -*- coding:utf-8 -*-
#从规模及等级分析面积
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


#清洗总投资数据
def transform_total(total):
    if total > 100000000:
        return total/10000
    else:
        return total

print get_area(u'大型|65000.00平方米')
print get_area(u'中型|4300.00平方米（跨度23米）')

from openpyxl.writer.excel import ExcelWriter
import pandas as pd
# use row 2 as column labels
df = pd.read_excel("201610883424_kc_ht.xls", header=1)
# print df
print df.columns
# select DF by index(columns)
# df = df[[u'合同备案编号', u'项目名称', u'企业名称', u'合同价格（万元）', u'总投资（万元）', u'规模及等级']]
# print df
# second way to select DF by index
df = df.loc[:, [u'合同备案编号', u'项目名称', u'企业名称', u'备案通过时间', u'合同价格（万元）', u'总投资（万元）', u'规模及等级']]
# df[[u'合同价格（万元）', u'总投资（万元）']] = df[[u'合同价格（万元）', u'总投资（万元）']].astype(float)
# print df
# print df[u"合同价格（万元）"].sum()
# ignore rows by specific column value
df = df[df[u'企业名称'] != u'江苏国泰新点软件有限公司']
# print df
# df = df[df[u'合同备案编号'] == '']
# print df
# print df[u"合同价格（万元）"].sum()
print pd.isnull(df)
# see http://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-of-certain-column-is-nan
# drop all rows that have any NaN values
# print df.dropna(how='any')
# drop rows only if NaN in specific column
df = df.dropna(subset=[u'合同备案编号'])
# print df

# 根据备案时间过滤
df = df[(df[u'备案通过时间']>'2015-12-31') & (df[u'备案通过时间'] <= '2016-03-31')]
# 新增面积栏位，根据规模及等级分析得来
df[u'面积'] = df[u'规模及等级'].apply(get_area)
df[u'总投资（万元）'] = df[u'总投资（万元）'].apply(transform_total)
print df
print '项目数 {}'.format(len(df))
print '合同价格 {}'.format(df[u"合同价格（万元）"].sum())
print '总投资 {}'.format(df[u"总投资（万元）"].sum())
print '总面积 {}'.format(df[u"面积"].sum())



# writer = ExcelWriter('output.xlsx')
# df.to_excel(writer, u'工程勘察设计项目合同备案汇总表')
# writer.save()
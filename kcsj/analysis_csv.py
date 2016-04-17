# -*- coding:utf-8 -*-
from openpyxl.writer.excel import ExcelWriter
import pandas as pd
# use row 2 as column labels
df = pd.read_csv("kcsj_2016.txt")
print df
print df.columns
# select DF by index(columns)
# df = df[[u'合同备案编号', u'项目名称', u'企业名称', u'合同价格（万元）', u'总投资（万元）', u'规模及等级']]
# print df
# second way to select DF by index
df = df.loc[:, [u'合同备案编号', u'项目名称', u'企业名称', u'合同价格（万元）', u'总投资（万元）', u'规模及等级']]
# df[[u'合同价格（万元）', u'总投资（万元）']] = df[[u'合同价格（万元）', u'总投资（万元）']].astype(float)
# print df
# print df[u"合同价格（万元）"].sum()
# ignore rows by specific column value
df = df[df[u'企业名称'] != u'江苏国泰新点软件有限公司']
# print df
# df = df[df[u'合同备案编号'] == '']
# print df
print df[u"合同价格（万元）"].sum()
print pd.isnull(df)
# see http://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-of-certain-column-is-nan
# drop all rows that have any NaN values
# print df.dropna(how='any')
# drop rows only if NaN in specific column
df = df.dropna(subset=[u'合同备案编号'])
print df

writer = ExcelWriter('output.xlsx')
df.to_excel(writer, u'工程勘察设计项目合同备案汇总表')
writer.save()
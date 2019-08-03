# -*- coding:utf-8 -*-
import pandas as pd
# read multiple sheets to map of DataFrame
sheet_to_df_map = pd.read_excel("第四批.xls", None)
for sheet in sheet_to_df_map:
    df = sheet_to_df_map[sheet]
    # print(df)
    # print(df.columns)
    # select DF by index(columns)
    df = df[[u'人员姓名', u'证件号码', u'注册单位']]
    # print(df)
    # df['is_duplicate'] = df.duplicated({u'证件号码'})
    # 找出姓名和身份证号重复的
    df = df[df.duplicated([u'人员姓名', u'证件号码'])]
    if len(df) > 0:
        print('sheet name:{}'.format(sheet))
        print(df)
    # print('sheet name:{}'.format(sheet))
    # print(df)
    # print(df)
    # print(df[[u'人员姓名']])
    # print(df.index.values)
# print(df.index.values)
# print(df[u'人员姓名'])
# select DF by index(columns)
# df = df[[u'人员姓名', u'证件号码', u'注册单位']]

# print(df)
# second way to select DF by index
# df = df.loc[:, [u'人员姓名', u'证件号码', u'注册单位',]]
# # df[[u'合同价格（万元）', u'总投资（万元）']] = df[[u'合同价格（万元）', u'总投资（万元）']].astype(float)
# print(df)
# # print df[u"合同价格（万元）"].sum()
# # ignore rows by specific column value
# df = df[df[u'企业名称'] != u'江苏国泰新点软件有限公司']
# # print df
# # df = df[df[u'合同备案编号'] == '']
# # print df
# # print df[u"合同价格（万元）"].sum()
# print(pd.isnull(df))
# # see http://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-of-certain-column-is-nan
# # drop all rows that have any NaN values
# # print df.dropna(how='any')
# # drop rows only if NaN in specific column
# df = df.dropna(subset=[u'合同备案编号'])
# print df

# 根据备案时间过滤
# df = df[(df[u'备案通过时间']>'2015-12-31') & (df[u'备案通过时间'] <= '2016-03-31')]

# writer = ExcelWriter('output.xlsx')
# df.to_excel(writer, u'工程勘察设计项目合同备案汇总表')
# writer.save()
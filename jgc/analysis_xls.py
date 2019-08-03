# -*- coding:utf-8 -*-
import pandas as pd
import glob
result_columns = [u'人员姓名', u'证件号码', u'注册单位', u'文件', 'sheet']
data = pd.DataFrame(columns=result_columns)

# file folder to parse
path = r'D:\workspace\worksmart\jgc\files'
file_names = glob.glob(path + "/*.*")
print(file_names)

for file_name in file_names:
    # read multiple sheets of one file to map of DataFrame
    sheet_to_df_map = pd.read_excel(file_name, None, converters={u'证件号码': str})
    for sheet in sheet_to_df_map:
        df = sheet_to_df_map[sheet]
        # print(df)
        print('fileName:{} sheet:{}'.format(file_name, sheet))
        print(df.columns)
        # select DF by index(columns)
        # columns = [u'人员姓名', u'身份证', u'注册单位']
        columns = []
        if u'人员姓名' in df.columns:
            columns.append(u'人员姓名')
        elif u'姓名' in df.columns:
            columns.append(u'姓名')

        if u'身份证' in df.columns:
            columns.append(u'身份证')
        elif u'证件号码' in df.columns:
            columns.append(u'证件号码')

        if u'所在企业名称' in df.columns:
            columns.append(u'所在企业名称')
        elif u'注册单位' in df.columns:
            columns.append(u'注册单位')
        print(columns)
        if len(columns) == 0:
            continue
        df = df[columns]
        import os
        # get file name rather than full path
        df[u'文件'] = os.path.basename(file_name)
        df['sheet'] = sheet
        print(df)
        # concat not like pd.merge which is like join operation
        data = pd.concat([data, df], ignore_index=True)
        # print(data)
        # print(df)
        # df['is_duplicate'] = df.duplicated({u'证件号码'})
        # 找出姓名和身份证号重复的
        # df = df[df.duplicated([u'人员姓名', u'证件号码'])]
        # if len(df) > 0:
        #     print('sheet name:{}'.format(sheet))
        #     print(df)
        # print('sheet name:{}'.format(sheet))
        # print(df)
        # print(df)
        # print(df[[u'人员姓名']])
        # print(df.index.values)
print('*'*15)
# filter NA value by column
data = data.dropna(subset=[u'人员姓名', u'证件号码'])
print(data)
print('*'*100)
# 找出姓名和身份证号重复的
data = data[data.duplicated([u'人员姓名', u'证件号码'])]
print(data)

writer = pd.ExcelWriter('重复人员.xlsx')
data.to_excel(writer, u'重复人员')
writer.save()
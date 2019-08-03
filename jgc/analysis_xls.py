# -*- coding:utf-8 -*-
import pandas as pd
import glob
import os
columns = [u'人员姓名', u'证件号码', u'注册单位']
result_columns = columns+[u'文件', 'sheet']
# print(result_columns)
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
        print(df)
        print('fileName:{} sheet:{}'.format(file_name, sheet))
        print(df.columns)
        # select DF by index(columns)

        # columns = []
        # if u'人员姓名' in df.columns:
        #     columns.append(u'人员姓名')
        # elif u'姓名' in df.columns:
        #     columns.append(u'姓名')
        #
        # if u'身份证' in df.columns:
        #     columns.append(u'身份证')
        # elif u'身份证号' in df.columns:
        #     columns.append(u'身份证号')
        # elif u'证件号码' in df.columns:
        #     columns.append(u'证件号码')
        #
        # if u'所在企业名称' in df.columns:
        #     columns.append(u'所在企业名称')
        # elif u'注册单位' in df.columns:
        #     columns.append(u'注册单位')
        # print(columns)
        # if len(columns) == 0:
        #     continue
        # check whether file format is correct
        invalid_data = False
        for column in columns:
            if column not in df.columns:
                invalid_data = True
                break
        print(invalid_data)
        if invalid_data:
            continue
        df = df[columns]

        # get file name rather than full path
        df[u'文件'] = os.path.basename(file_name)
        df['sheet'] = sheet
        # print(df)
        # concat not like pd.merge which is like join operation
        data = pd.concat([data, df], ignore_index=True)
print('*'*15)
data = data[result_columns]
print(data)
# filter NA value by column
data = data.dropna(subset=[u'人员姓名', u'证件号码'])
print(data)
print('*'*100)
# 找出姓名和身份证号重复的
data = data[data.duplicated([u'人员姓名', u'证件号码'])]
# print(data)
# re-order by columns
data = data[result_columns]
data = data.sort_values(by=[u'文件', 'sheet', u'人员姓名'], ascending=True)
print(data)

writer = pd.ExcelWriter('重复人员.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name=u'重复人员')

# adjust column width or format
workbook = writer.book
worksheet = writer.sheets[u'重复人员']
# Columns B width set to 10.
worksheet.set_column(u'B:B', 10)
# Columns C-H width set to 30
worksheet.set_column(u'C:F', 30)

writer.save()
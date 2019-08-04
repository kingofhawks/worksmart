# -*- coding:utf-8 -*-
import pandas as pd
import glob
import os

if __name__ == '__main__':
    columns = [u'人员姓名', u'证件号码', u'注册单位']
    duplicated_columns = [u'人员姓名', u'证件号码']
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

            # check whether file format is correct
            invalid_data = False
            for column in columns:
                if column not in df.columns:
                    invalid_data = True
                    break
            if invalid_data:
                continue

            # select DF by index(columns)
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
    data = data.dropna(subset=duplicated_columns)
    print(data)
    print('*'*100)
    # 找出姓名和身份证号重复的,keep=False会返回所有的重复项
    data = data[data.duplicated(duplicated_columns, keep=False)]
    # print(data)
    # re-order by columns
    data = data[result_columns]
    # sort by multiple columns
    data = data.sort_values(by=[u'人员姓名', u'文件', 'sheet' ], ascending=True)
    print(data)

    writer = pd.ExcelWriter('重复人员.xlsx', engine='xlsxwriter')
    # write DF to excel without index
    data.to_excel(writer, sheet_name=u'重复人员', index=False)

    # adjust column width or format
    workbook = writer.book
    worksheet = writer.sheets[u'重复人员']
    # Columns A width set to 10.
    worksheet.set_column(u'A:A', 10)
    # Columns B-E width set to 30
    worksheet.set_column(u'B:E', 30)

    writer.save()
import pyodbc
import pandas as pd
print(pyodbc.drivers())
conn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};SERVER=localhost;PORT=3306;DADABASE=uportal;UID=root;PWD=lazio_2000')
cursor = conn.cursor()


def get_bad_info(tcp_id):
    # SQL must with dbName.table
    cursor.execute("select * from uportal.t_center_travelapply where id='{}'".format(tcp_id))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    sql = "select * from uportal.T_CENTER_OAATTACHMENT where refId='{}'".format(tcp_id)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        path = row[3]
        print(path)
        full_path ='D:/oa_attachment/tcp'+path
        print(full_path)
        import xlrd
        book = xlrd.open_workbook(full_path)
        print("The number of worksheets is {0}".format(book.nsheets))
        print("Worksheet name(s): {0}".format(book.sheet_names()))
        sh = book.sheet_by_index(0)
        print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
        for rx in range(sh.nrows):
            print(sh.row(rx))
        df = pd.read_excel(full_path)
        print(df)


get_bad_info('UT201811262049475319')
import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.153.189;PORT=1433;DADABASE=Epoint_WXKCSJ;UID=sa;PWD=wxjsj^20150326')
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM Epoint_WXKCSJ.dbo.HT_BA_Tab where htjg>100000 order by operatedate desc")
# SELECT * FROM Epoint_WXKCSJ.dbo.ZZHY_DXSQB order by operatedate desc
row = cursor.fetchone()
print row
print row[1]


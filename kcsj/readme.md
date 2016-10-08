无锡市勘察设计数据统计模块
@Deprecated
1. 登陆勘察设计系统->合同备案->备案列表，选择"备案通过时间"，"已盖章"项目导出
2. python analysis_xls.py
如果是单项资质核验(导出Excel后要转成csv格式，否则read_excel报错)
3. python analysis_xls_dx.py


Please use this method for statistics:
4. sync from production MS SQL Server(pip install pyodbc)    
python sync_production.py
python sync_production_dx.py
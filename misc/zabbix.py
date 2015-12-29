from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://192.168.153.254/zabbix")
zapi.login("Admin", "zabbix")
print "Connected to Zabbix API Version %s" % zapi.api_version()

for h in zapi.host.get(output="extend"):
    print h['hostid']
    print h
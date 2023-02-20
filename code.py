import prestodb
conn=prestodb.dbapi.connect(
    host='localhost',
    port=8080,
    user='root',
    catalog='hive',
    schema='default',
)
cur = conn.cursor()
cur.execute('show tables')
rows = cur.fetchall()
print(rows)

import prestodb
conn=prestodb.dbapi.connect(
    host='localhost',
    port=8080,
    user='root',
    catalog='hive',
    schema='default',
)
cur = conn.cursor()
cur.execute('select * from hep')
rows = cur.fetchall()
print(rows)




SELECT
  mysql.default.HistogramBin(MET_pt, 0, 2000, 100) AS x,
  COUNT(*) AS y
FROM hep
GROUP BY mysql.default.HistogramBin(MET_pt, 0, 2000, 100)
ORDER BY x;
import prestodb

def exec_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)

if __name__ == "__main__":
    conn=prestodb.dbapi.connect(
        host='localhost',
        port=8080,
        user='root',
        catalog='hive',
        schema='default',
    )   

    # drop exisiting table and create a new one
    with open('create_table.sql', 'r') as f:
        create_table_sql = f.read()
    exec_query(conn, create_table_sql)
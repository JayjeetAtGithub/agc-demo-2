import sys
import time

import prestodb


def exec_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)


if __name__ == "__main__":
    conn = prestodb.dbapi.connect(
        host='localhost',
        port=8080,
        user='root',
        catalog='hive',
        schema='default',
    )

    if len(sys.argv) == 2 and sys.argv[1] == 'create':
        # drop exisiting table
        exec_query(conn, 'DROP TABLE IF EXISTS hep')

        #  create a new one
        with open('create_table.sql', 'r') as f:
            create_table_sql = f.read()
        exec_query(conn, create_table_sql)
        
        # create the common function
        with open('create_function.sql', 'r') as f:
            create_function_sql = f.read()
        exec_query(conn, create_function_sql)

    if len(sys.argv) == 3 and sys.argv[1] == 'query':
        with open(f'queries/{sys.argv[2]}.sql', 'r') as f:
            query_sql = f.read()
        
        s = time.time()
        exec_query(conn, query_sql)
        e = time.time()
        print(f'Elapsed time: {e-s}')

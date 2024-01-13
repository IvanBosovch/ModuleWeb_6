import sqlite3

def execute_query(sql: str) -> list:
    with open(sql, 'r') as f:
        sql = f.read()


    with sqlite3.connect('Hogwatrs.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    print(execute_query('query_1.sql'))
import pg8000

class databaseAPI:
    def __init__(self):
        self.conn = pg8000.connect(
            database="postgres",
            user="postgres",
            password="password",
            host="localhost",
            port=5432
        )

    def get_rows(self, table_name):
        cur = self.conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        rows = cur.fetchone()[0]
        return rows

    def get_names(self, table_name):
        cur = self.conn.cursor()
        cur.execute(f"SELECT first_name, last_name FROM {table_name}")
        names = cur.fetchall()
        return names

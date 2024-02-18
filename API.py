import psycopg2

class databaseAPI:
    def __init__(self, username, password):
        self.conn = psycopg2.connect(
            database="postgres",
            user=username,
            password=password,
            host="localhost",
            port=5432
        )

    def get_rows(self, table_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT COUNT(*) FROM {table_name}")
            rows = cur.fetchone()[0]
            return rows
        except psycopg2.errors.InsufficientPrivilege:
            return None
        except Exception as e:
            print(e)
            return None

    def get_names(self, table_name):
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT first_name, last_name FROM {table_name}")
            names = cur.fetchall()
            return names
        except psycopg2.errors.InsufficientPrivilege:
            return None
        except Exception as e:
            print(e)
            return None

    def check_credentials(self, username, password):
        try:
            conn = psycopg2.connect(
                database="postgres",
                user=username,
                password=password,
                host="localhost",
                port=5432
            )
            conn.close()
            return True
        except:
            return False
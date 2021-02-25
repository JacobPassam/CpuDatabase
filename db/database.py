from sqlite3 import Cursor, connect

DATABASE_FILE = "cpu.db"
TABLE_NAME = "CPUStore"


class DatabaseHandler:

    def __init__(self):
        self.conn = connect(DATABASE_FILE)

    def new_cursor(self):
        return self.conn.cursor()

    def create_table(self, cursor: Cursor):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                       Id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Name TEXT NOT NULL,
                       ClockSpeed REAL NOT NULL,
                       Cores INTEGER NOT NULL,
                       CacheSize INTEGER NOT NULL,
                       Price REAL NOT NULL)
                       """)

        cursor.close()

    def commit(self):
        self.conn.commit()

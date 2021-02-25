from db.database import DatabaseHandler, TABLE_NAME
from cpu.cpu import Cpu


class CpuController:

    def __init__(self, databaseHandler: DatabaseHandler):
        self.databaseHandler = databaseHandler

    def get_all_cpus(self):
        cursor = self.databaseHandler.new_cursor()

        cursor.execute(f"SELECT * FROM {TABLE_NAME};")

        cpus = []
        for row in cursor.fetchall():
            cpu = Cpu(cpu_id=row[0], name=row[1], clock_speed=row[2], cores=row[3], cache_size=row[4], price=row[5])
            cpus.append(cpu)

        cursor.close()

        return cpus

    def get_by_id(self, cpuId: int):
        cursor = self.databaseHandler.new_cursor()

        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE Id = {cpuId};")

        row = cursor.fetchone()
        if row is None:
            return None

        cpu = Cpu(cpu_id=row[0], name=row[1], clock_speed=row[2], cores=row[3], cache_size=row[4], price=row[5])

        cursor.close()

        return cpu

    def add_cpu(self, cpu: Cpu):
        cursor = self.databaseHandler.new_cursor()

        cursor.execute(f"""
            INSERT INTO {TABLE_NAME} (Name, ClockSpeed, Cores, CacheSize, Price) VALUES (?, ?, ?, ?, ?)
        """, (cpu.name, cpu.clock_speed, cpu.cores, cpu.cache_size, cpu.price))

        cursor.close()
        self.databaseHandler.commit()

    def update_cpu(self, update: dict, db_filter: dict):
        sql = f"UPDATE {TABLE_NAME} SET "

        for key, value in update.items():
            if isinstance(value, str):
                sql += f"{key} = \"{value}\", "
            else:
                sql += f"{key} = {value}, "

        sql = sql[:-2]

        sql += " WHERE "
        for key, value in db_filter.items():
            if isinstance(value, str):
                sql += f"{key} = \"{value}\" AND "
            else:
                sql += f"{key} = {value} AND "

        sql = sql[:-5] + ";"

        cursor = self.databaseHandler.new_cursor()
        cursor.execute(sql)
        cursor.close()

        self.databaseHandler.commit()

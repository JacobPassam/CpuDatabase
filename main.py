from controller.cpuController import CpuController
from db.database import DatabaseHandler
from menu import mainMenu

database_handler = DatabaseHandler()
database_handler.create_table(database_handler.new_cursor())

cpuController = CpuController(database_handler)

while True:
    mainMenu.do_menu(cpuController)

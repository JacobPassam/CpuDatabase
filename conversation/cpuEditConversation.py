from conversation.conversationItem import ConversationItem
from cpu.cpu import Cpu
from util import menuUtil
from controller.cpuController import CpuController

CPU_FIELDS = {"Id": int, "Name": str, "ClockSpeed": float, "Cores": int, "CacheSize": int, "Price": float}


def cpu_edit_flow(cpuController: CpuController):
    id_c = ConversationItem("ID of the CPU you wish to edit", int)

    cpu_id = id_c.do_input()
    cpu_current: Cpu = cpuController.get_by_id(cpu_id)

    while cpu_current is None:
        print("That CPU ID is not valid.")

        cpu_id = id_c.do_input()
        cpu_current = cpuController.get_by_id(cpu_id)

    db_filter = {"Id": cpu_id}

    fields = []

    field = ConversationItem("field you wish to edit", str).do_input()

    while field not in CPU_FIELDS.keys():
        print("That field is not valid. (" + get_fields_string() + ")")
        field = ConversationItem("field you wish to edit", str).do_input()

    fields.append(field)

    menu_options = ["Add another field", "Carry on", "Exit"]
    while True:
        menuUtil.send_menu(menu_options)

        opt = menuUtil.receive_option(len(menu_options))
        if opt == 1:
            field = ConversationItem("field you wish to edit", str).do_input()

            while field not in CPU_FIELDS.keys():
                print("That field is not valid. (" + get_fields_string() + ")")
                field = ConversationItem("field you wish to edit", str).do_input()

            fields.append(field)
        elif opt == 2:
            break
        elif opt == 3:
            return

    updates = {}

    for field in fields:
        val = ConversationItem("value for field " + field, CPU_FIELDS[field]).do_input()
        updates[field] = val

    print("Original CPU: " + cpu_current.get_as_string())
    cpuController.update_cpu(updates, db_filter)

    cpu_new = cpuController.get_by_id(cpu_id)
    print("Updated CPU: " + cpu_new.get_as_string())


def get_fields_string():
    s = ""
    for field in CPU_FIELDS.keys():
        s += field + ", "

    return s[:-2]

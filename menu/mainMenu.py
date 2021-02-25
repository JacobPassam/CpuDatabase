from util import menuUtil
from controller.cpuController import CpuController
from conversation import cpuCreationConversation, cpuEditConversation

MENU_OPTIONS = ["View CPUs", "Update CPUs", "Add a CPU", "Quit"]  # Constant representing main menu options.


# Method to output the main menu. Loop is controlled by main.
def do_menu(cpuController: CpuController):
    menuUtil.send_menu(MENU_OPTIONS)
    option = menuUtil.receive_option(len(MENU_OPTIONS))  # Receive validated menu option.

    print()
    if option == 1:

        print("Viewing all CPUs...")
        for cpu in cpuController.get_all_cpus():
            print(cpu.get_as_string())

    elif option == 2:
        # Update CPU
        cpuEditConversation.cpu_edit_flow(cpuController)

    elif option == 3:
        # Add a CPU

        cpu = cpuCreationConversation.cpu_creation_flow()
        cpuController.add_cpu(cpu)
        print("Added your CPU: " + cpu.get_as_string())

        pass

    elif option == 4:
        # Exit
        print('Bye!')

        exit()

    print()

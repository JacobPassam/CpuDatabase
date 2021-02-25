from conversation.conversationItem import ConversationItem
from cpu.cpu import Cpu


def cpu_creation_flow():
    name = ConversationItem("name", str).do_input()
    clock_speed = ConversationItem("clock speed", float).do_input()
    cores = ConversationItem("cores", int).do_input()
    cache_size = ConversationItem("cache size", int).do_input()
    price = ConversationItem("price", float).do_input()

    return Cpu(name, clock_speed, cores, cache_size, price)

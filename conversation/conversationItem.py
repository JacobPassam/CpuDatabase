class ConversationItem:

    def __init__(self, uiName: str, itemType: type):
        self.uiName = uiName
        self.itemType = itemType

    def do_input(self):
        v = input(f"Enter the {self.uiName}: ")

        valid = False

        while not valid:
            try:
                self.itemType(v)
                valid = True
            except ValueError:
                v = input(f"That is not the correct type. Enter the {self.uiName}: ")

        return v

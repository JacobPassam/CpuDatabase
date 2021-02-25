# Send menu based on an array of menu options.
def send_menu(arr):
    for opt in arr:
        index = arr.index(opt)
        index += 1

        print(str(index) + ". " + opt)


# Input the requested option and validate it.
def receive_option(length):
    opt = input('Enter your desired option: ')
    opt = validate_input(opt, length)

    return opt


# Validates the input. Loops infinitely until the input is valid.
def validate_input(opt, length):
    while not is_number(opt):
        opt = input('That is not a number, please try again: ')

    opt = int(opt)
    while opt < 0 or opt > length:

        opt = input('That is not a valid option (1-' + str(length) + '). Please try again: ')
        while not is_number(opt):
            opt = input('That is not a number, please try again: ')

        opt = int(opt)

    return opt


# Returns whether or not a given String is a number.
def is_number(opt):
    try:
        int(opt)
        return True
    except ValueError:
        return False
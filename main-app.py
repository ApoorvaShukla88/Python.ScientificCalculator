from calculator import Basic

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def displayResult(x: float):
    print(x, "\n")


def perform_main_menu():
    menu_input = (int(input('You\'re using the ARP Calculator\n Enter 1 for Basic Functions\n Enter 2 for Advanced Functions\n Enter '
                            '3 for Scientific Functions ')))
    questionmap = {
            1: basic_func(),
            2: secondaryfunc(),
            3: sciencefunc()
        }
    if menu_input in questionmap:
        menu_choice = questionmap[menu_input]
        return menu_choice
    if menu_input not in questionmap:
        print("That's not gonna work, try again")
        perform_main_menu()

def basic_func():
    basic_input = (input('Enter \'A\' for +\nEnter \'S\' for - \nEnter \'M\' for * \nEnter \'D\' for or /\n'))
    basic_map = {
        'A': Basic.A(),
        'S': Basic.S(),
        'M': Basic.M(),
        'D': Basic.D()
    }
    basic_choice = basic_map[basic_input]
    return basic_choice

def secondaryfunc():
    secondary_input = (input('+, - , * , or /'))
    secondary_map = {
        '+': Secondary.add,
        '-': Secondary.sub,
        '*': Secondary.mult,
        '/': Secondary.div
    }
    secondary_choice = secondary_map[secondary_input]
    return secondary_choice

def sciencefunc():
    science_input = (input('+, - , * , or /'))
    science_map = {
        '+': science.add,
        '-': science.sub,
        '*': science.mult,
        '/': science.div
    }
    science_choice = science_map[science_input]
    return science_choice









#
#
# def performCalcLoop(c
#
# alc):


#     while True:


#         choice = input("Choose 'A' for Addition 'S' for Subtraction 'M' for Multiplication 'D' for Division ")
#
#         if choice == 'q':
#             print(0)  # user types q to quit calulator.
#         elif choice == input():
#             a, b = getTwoNumbers()
#             displayResult(calc.self(a, b))
#         else:
#             print("That is not a valid input.")


# main start
def main():
    perform_main_menu()
    # calc = Calculator()
    # performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()

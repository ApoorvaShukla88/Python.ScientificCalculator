from calculator import Basic, Intermediate


def perform_main_menu():
    menu_input = (int(input('You\'re using the ARP Calculator\n Enter 1 for Core Functions\n Enter 2 for Scientific Functions\n')))
    # print(menu_input)
    questionmap = {
            1: basic_func,
            2: sciencefunc,
        }
    if menu_input in questionmap:
        menu_choice = questionmap[menu_input]
        return menu_choice()
    if menu_input not in questionmap:
        print("That's not gonna work, try again")
        perform_main_menu()

def basic_func():
    basic_input = (input("Enter 'A' for +\nEnter 'S' for - \nEnter 'M' for * \nEnter 'D' for /\n"))
    basic_map = {
        'A': Basic.a,
        'S': Basic.s,
        'M': Basic.m,
        'D': Basic.d,
    }
    if basic_input in basic_map:
        # arg_self = self
        arg_one = int(input('enter arg 1 '))
        arg_two = int(input('enter arg 2 '))
        basic_choice = basic_map[basic_input]
        print(basic_choice((), arg_one, arg_two))
    if basic_input not in basic_map:
        print("That's not gonna work, try again")
        perform_main_menu()
        # basic_choice = basic_map[basic_input]
        # print(basic_choice(arg_one, arg_two))


def sciencefunc():
    science_input = input(" 1 for square\n 2 for square root\n 3 for exponential\n 4 for sine\n 5 for cosine\n 6 for"
                          " tangent\n 7 for arcosine\n 8 for arctan\n")

    # global switch_display
    science_map = {
    '1': Intermediate.square,
    '2': Intermediate.squareroot,
    '3': Intermediate.exponential,
    '4': Intermediate.sine,
    '5': Intermediate.cosine,
    '6': Intermediate.tang,
    '7': Intermediate.acosine,
    '8': Intermediate.atang,
}
    if science_input not in science_map:
        print("That's not gonna work, try again")
        sciencefunc()
    if science_input == '3' in science_map:
        arg_one = int(input('enter arg 1 '))
        arg_two = int(input('enter arg 2 '))
        science_choice = science_map[science_input]
        sci_ans = science_choice((), arg_one, arg_two)
    else:
        arg_one = int(input('enter arg 1 '))
        science_choice = science_map[science_input]
        sci_ans = int(science_choice((), arg_one))
        display_mode(sci_ans)


def display_mode(sci_ans):

    display_input = input(
        "Display Mode options enter:\n 1 for binary\n 2 for octagonal\n 3 for hexadecimal\n 0 for decimal\n")

    display_map = {'1': bin, '2': oct, '3': hex, '0': float, }
    if display_input not in display_map:
        print("That's not gonna work, try again")
        display_mode(sci_ans)
    else:
        display_choice = display_map[display_input]
        print(display_choice(sci_ans))







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

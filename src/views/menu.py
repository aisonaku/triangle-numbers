from consolemenu import *
from consolemenu.items import *

from controllers.triangle_numbers_actions_controller import TriangleNumbersActionsController

class Menu:
    def __init__(self):
        self.screen = Screen()

    def initialize(self):
        menu = ConsoleMenu("Main Menu", "", self.screen)
        first_option = FunctionItem("Show all divisors for the triangle number ", self.first_option_action, menu=menu)
        second_option = FunctionItem("Find the first triangle number with over N number of divisors", self.second_option_action, menu=menu)


        # Add all the items to the root menu
        menu.append_item(first_option)
        menu.append_item(second_option)

        # Show the menu
        menu.start()
        menu.join()

    def first_option_action(self):
        n = int(self.screen.input("Give the ordinal of triangle number?\n"))
        if n < 1:
            print("Ordinal should be a natural number\n")
            return
        controller = TriangleNumbersActionsController()
        controller.print_all_nth_number_divisors(n)

    def second_option_action(self):
        n = int(self.screen.input("Give minimum number of divisors triangle number should have?\n"))
        if n < 2:
            print("There are no triangle numbers with less than 2 divisors\n")
            return
        controller = TriangleNumbersActionsController()
        controller.print_num_with_divisors_count(n)

from consolemenu import *
from consolemenu.items import *

from controllers.triangle_numbers_actions_controller import TriangleNumbersActionsController

class Menu:
    def __init__(self):
        self.screen = Screen()

    def initialize(self):
        menu = ConsoleMenu("Main Menu", "", self.screen)
        function_item = FunctionItem("Show all divisors for the triangle number ", self.first_option_action, menu=menu)

        # Add all the items to the root menu
        menu.append_item(function_item)

        # Show the menu
        menu.start()
        menu.join()

    def first_option_action(self):
        n = self.screen.input("Give the ordinal of triangle number\n")
        controller = TriangleNumbersActionsController()
        controller.print_all_nth_number_divisors(int(n))


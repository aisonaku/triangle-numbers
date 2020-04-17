import os
from models.file import File

class OutputController:
    def __init__(self, results_dir="results"):
        self.results_dir = results_dir

    def output_result(self, num, divisors, option, additional_data):
        self._create_dir_if_not_exists(self.results_dir)
        if option == 1:
            result_string = self._construct_string(num, divisors)
            print(result_string)
            self.print_to_file(result_string, "%s/Divisors and sum of %sth term.txt" % (self.results_dir, str(additional_data)))
        elif option == 2:
            result_string = self._construct_string(num, divisors)
            print("The triangle number is %s and divisors are %s" % (num, ', '.join(map(str, divisors))))
            self.print_to_file(result_string, "%s/The first triangle number %s.txt" % (self.results_dir, str(additional_data)))
        else:
            print("Can't format output for option %s\n" % str(option))

    def _create_dir_if_not_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def print_to_file(self, string, filename):
        file = File(filename)
        file.print_string(string)

    def _construct_string(self, num, divisors) -> str:
        return str(num) + ": " + ', '.join(map(str, divisors)) + "\n"

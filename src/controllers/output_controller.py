from models.file import File

class OutputController:
    def output_result(self, num, divisors, option, additional_data):
        if option == 1:
            result_string = self._construct_string(num, divisors)
            print(result_string)
            self.print_to_file(result_string, "Divisors and sum of %sth term.txt" % str(additional_data))
        elif option == 2:
            result_string = self._construct_string(num, divisors)
            print("The triangle number is %s and divisors are %s" % (num, ', '.join(map(str, divisors))))
            self.print_to_file(result_string, "The first triangle number %s.txt" % str(additional_data))
        else:
            print("Can't format output for option %s\n" % str(option))

    def print_to_file(self, string, filename):
        file = File(filename)
        file.print_string(string)

    def _construct_string(self, num, divisors) -> str:
        return str(num) + ": " + ', '.join(map(str, divisors)) + "\n"

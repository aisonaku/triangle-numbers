class File:
    def __init__(self, name):
        self.name = name

    def print_string(self, string):
        f = open(self.name, 'w')
        f.write(string)
        f.close()

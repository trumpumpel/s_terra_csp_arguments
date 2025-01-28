class CommandLineUtility:

    def __init__(self, name):
        self.name = name

    def run(self, command, *args):
        raise NotImplementedError("Subclasses should implement this method")

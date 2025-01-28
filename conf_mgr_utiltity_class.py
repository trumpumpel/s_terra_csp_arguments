from base_utility_class import CommandLineUtility


class ConfMgrUtility(CommandLineUtility):
    def __init__(self, name):
        super().__init__(name)
        self.config = {}

    def run(self, command, *args):
        if command == 'add':
            self.add(*args)
        elif command == 'modify':
            self.modify(*args)
        elif command == 'delete':
            self.delete(*args)
        elif command == 'show':
            return self.show(*args)
        else:
            return "Unknown command"

    def add(self, key, value):
        self.config[key] = value
        print(f"Added: {key} = {value}")

    def modify(self, key, value):
        if key in self.config:
            self.config[key] = value
            print(f"Modified: {key} = {value}")
        else:
            print(f"Key {key} not found")

    def delete(self, key):
        if key in self.config:
            del self.config[key]
            print(f"Deleted: {key}")
        else:
            print(f"Key {key} not found")

    def show(self, *args):
        if '--all' in args or '-a' in args:
            return str(self.config)
        else:
            for key in args:
                if key in self.config:
                    print(f"{key} = {self.config[key]}")
                else:
                    print(f"Key {key} not found")

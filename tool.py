import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: <command> [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "run":
        verbose = False
        output_file = None

        # Обрабатываем опции
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "-v" or sys.argv[i] == "--verbose":
                verbose = True
            elif sys.argv[i] == "-o" or sys.argv[i] == "--output":
                if i + 1 < len(sys.argv):
                    output_file = sys.argv[i + 1]
                    i += 1
                else:
                    print("Error: missing value for output option.")
                    sys.exit(1)
            else:
                print(f"Unknown option: {sys.argv[i]}")
                sys.exit(1)
            i += 1

        # Логика выполнения команды
        if verbose:
            print("Verbose mode enabled.")
        if output_file:
            print(f"Output will be saved to {output_file}.")
        else:
            print("No output file specified.")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

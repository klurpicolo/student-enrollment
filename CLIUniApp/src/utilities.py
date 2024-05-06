from typing import Literal


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_colored(color_code: str, *values: object, sep: str | None = " ",
                  end: str | None = "\n", flush: Literal[False] = False):
    print(color_code, end="")
    print(*values, sep=sep, end=end, flush=flush)
    print(bcolors.ENDC, end="")


def print_red(*values: object, sep: str | None = " ",
              end: str | None = "\n", flush: Literal[False] = False):
    print_colored(bcolors.FAIL, *values, sep=sep, end=end, flush=flush)


def print_green(*values: object, sep: str | None = " ",
                end: str | None = "\n", flush: Literal[False] = False):
    print_colored(bcolors.OKGREEN, *values, sep=sep, end=end, flush=flush)


def print_yellow(*values: object, sep: str | None = " ",
                 end: str | None = "\n", flush: Literal[False] = False):
    print_colored(bcolors.WARNING, *values, sep=sep, end=end, flush=flush)


def print_blue(*values: object, sep: str | None = " ",
               end: str | None = "\n", flush: Literal[False] = False):
    print_colored(bcolors.OKBLUE, *values, sep=sep, end=end, flush=flush)


if __name__ == "__main__":
    print_red("This will be printed in red.")
    print_green("This will be printed in green.")
    print_yellow("This will be printed in yellow.")
    print_blue("This will be printed in blue.")
    print("This will be printed in default color.")

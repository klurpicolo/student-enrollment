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


indent = "      "


def print_colored(color_code: str, *values: object, sep: str | None = " ",
                  end: str | None = "\n", flush: Literal[False] = False):
    print(color_code, end="")
    print(*values, sep=sep, end=end, flush=flush)
    print(bcolors.ENDC, end="")


def print_red(*values: object, sep: str | None = " ",
              end: str | None = "\n", flush: Literal[False] = False, is_indent: bool = True):
    if is_indent:
        if values:
            values = (indent + values[0],) + values[1:]
    print_colored(bcolors.FAIL, *values, sep=sep, end=end, flush=flush)


def print_green(*values: object, sep: str | None = " ",
                end: str | None = "\n", flush: Literal[False] = False, is_indent: bool = True):
    if is_indent:
        if values:
            values = (indent + values[0],) + values[1:]
    print_colored(bcolors.OKGREEN, *values, sep=sep, end=end, flush=flush)


def print_yellow(*values: object, sep: str | None = " ",
                 end: str | None = "\n", flush: Literal[False] = False, is_indent: bool = True):
    if is_indent:
        if values:
            values = (indent + values[0],) + values[1:]
    print_colored(bcolors.WARNING, *values, sep=sep, end=end, flush=flush)


def print_blue(*values: object, sep: str | None = " ",
               end: str | None = "\n", flush: Literal[False] = False, is_indent: bool = True):
    if is_indent:
        if values:
            values = (indent + values[0],) + values[1:]
    print_colored(bcolors.OKCYAN, *values, sep=sep, end=end, flush=flush)


def print_white(*values: object, sep: str | None = " ",
               end: str | None = "\n", flush: Literal[False] = False, is_indent: bool = True):
    if is_indent:
        if values:
            values = (indent + values[0],) + values[1:]
    print(*values, sep=sep, end=end, flush=flush)

def input_colored(prompt: str, color_code: str) -> str:
    print_colored(color_code, prompt, end="")
    user_input = input()
    return user_input


def input_red(prompt: str, is_indent: bool = True) -> str:
    if is_indent:
        prompt = indent + prompt
    return input_colored(prompt, bcolors.FAIL)


def input_green(prompt: str, is_indent: bool = True) -> str:
    if is_indent:
        prompt = indent + prompt
    return input_colored(prompt, bcolors.OKGREEN)


def input_yellow(prompt: str, is_indent: bool = True) -> str:
    if is_indent:
        prompt = indent + prompt
    return input_colored(prompt, bcolors.WARNING)


def input_blue(prompt: str, is_indent: bool = True) -> str:
    if is_indent:
        prompt = indent + prompt
    return input_colored(prompt, bcolors.OKCYAN)


def input_white(prompt: str, is_indent: bool = True) -> str:
    if is_indent:
        prompt = indent + prompt
    return input(prompt)


if __name__ == "__main__":
    red_input = input_red("This will be input in red: ")
    print_red(f'{red_input=}')
    yellow_input = input_yellow("This will be input in yellow: ")
    print_yellow(f'{yellow_input=}')
    green_input = input_green("This will be input in red: ")
    print_green(f'{green_input=}')
    blue_input = input_blue("This will be input in red: ")
    print_blue(f'{blue_input=}')
    white_input = input_white("This will be input in white: ")
    print_white(f'{white_input=}')

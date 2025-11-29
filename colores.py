def print_blue(s: str, end: str = '\n'):
    print(f'\033[34m{s}\033[0m', end=end)

def print_green(s: str, end: str = '\n'):
    print(f'\033[32m{s}\033[0m', end=end)

def print_yellow(s: str, end: str = '\n'):
    print(f'\033[33m{s}\033[0m', end=end)

def print_red(s: str, end: str = '\n'):
    print(f'\033[31m{s}\033[0m', end=end)

def print_magenta(s: str, end: str = '\n'):
    print(f'\033[35m{s}\033[0m', end=end)
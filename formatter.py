from os.path import isdir
from os import mkdir, system

def check_path() -> None:
    if not isdir("data"):
        mkdir("data")
    return

def load_set(name: str) -> list[dict]:
    file = open("data/" + name, "r").readlines()
    mode = "q"
    out = []
    for line in file:
        if line == "Q:\n":
            mode = "q"
            out.append({"q": "", "a": ""})
        elif line == "A:\n":
            mode = "a"
        else:
            out[-1][mode] = out[-1][mode] + line
    return out

def edit(name: str) -> None:
    system("vim data/" + name)

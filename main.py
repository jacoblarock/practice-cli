import formatter
from random import shuffle
from pathlib import Path
from os import listdir

def clear():
    print("\033[H", end="")
    print("\033[2J", end="")

if __name__ == "__main__":
    formatter.check_path()
    clear()
    # main loop
    while True:
        com = input("Practice or edit? p/e ")
        if com == "p":
            for file in listdir("data"):
                print(file.split("/")[-1])
            set_name = input("set name: ")
            cur_set = formatter.load_set(set_name)
            if input("shuffle? [y]/n ") != "n":
                shuffle(cur_set)
            clear()
            # practice loop
            i = 0
            side = "q"
            while True:
                print(cur_set[i][side])
                com = input(":")
                if side == "a":
                    clear()
                if com == "n" and i < len(cur_set) - 1:
                    side = "q"
                    clear()
                    i += 1
                elif com == "p" and i > 0:
                    side = "q"
                    clear()
                    i -= 1
                elif com == "" and side == "q":
                    side = "a"
                elif com == "" and side == "a" and i < len(cur_set) - 1:
                    side = "q"
                    clear()
                    i += 1
                else:
                    print("bad command")
        elif com == "e":
            set_name = input("set name: ")
            formatter.edit(set_name)
        elif com == "exit":
            break
        else:
            print("p, e or exit")

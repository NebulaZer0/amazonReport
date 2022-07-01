import sys
from os import name, system
from amazontools import amazonTools
from colorama import Fore


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def printMenu():
    print(Fore.LIGHTYELLOW_EX + "Options:")
    print(Fore.LIGHTCYAN_EX + f"{' ' * 5}a) " + Fore.CYAN + "Total Spent")
    print(Fore.LIGHTCYAN_EX + f"{' ' * 5}b) " + Fore.CYAN + "Average Spent Yearly")
    print(Fore.LIGHTCYAN_EX + f"{' ' * 5}c) " + Fore.CYAN + "Exit\n")


if "__main__" == __name__:
    args = sys.argv

    args.pop(0)

    if len(args) > 1:
        print(Fore.RED + "Error: Too Many Arguments! Exiting...")
        exit(0)
    else:
        report = amazonTools(args[0])
        view = ''

        while True:
            clear()
            print(Fore.LIGHTBLUE_EX + f"{'*' * 10} Amazon Report Tool {'*' * 10}\n")
            report.printFileInfo()
            printMenu()
            print(view)
            choice = input(Fore.CYAN + 'select:').lower()

            if choice == 'a':
                view = f"\n{Fore.CYAN} Total Spent: {Fore.GREEN} ${str(report.totalSpent())}\n"

            elif choice == 'b':
                view = f"\n{Fore.CYAN} Average Spent Per Year: {Fore.GREEN} ${str(report.averageSpent())}\n"
            elif choice == 'c':
                clear()
                exit(1)
            else:
                view = f"\n{Fore.RED} ERROR: Invalid Choice\n"

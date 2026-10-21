from colorama import Fore, Style
from termcolor import colored

def show_colors():
    print(Fore.GREEN + "Цей рядок виведено за допомогою colorama." + Style.RESET_ALL)
    print(colored("А цей рядок оформлено через termcolor.", "cyan"))

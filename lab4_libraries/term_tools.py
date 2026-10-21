from art import text2art
import pyfiglet

def show_art():
    print("ASCII-арт через art:")
    print(text2art("ALCHEMY", font="small"))
    print("ASCII-арт через pyfiglet:")
    print(pyfiglet.figlet_format("PYTHON", font="slant"))

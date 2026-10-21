import humanize
from datetime import timedelta

def show_humanized():
    print("Число у зручному форматі:", humanize.intcomma(1234567))
    print("Тривалість:", humanize.precisedelta(timedelta(hours=2, minutes=35, seconds=10)))

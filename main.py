from utils.titles import TITLE, TITLE_COLOR
from termcolor import cprint
from utils.checker import Checker

if __name__ == "__main__":

    cprint(TITLE, TITLE_COLOR)
    cprint(f'\nsubscribe to us : https://t.me/hodlmodeth', TITLE_COLOR)
    Checker().main()
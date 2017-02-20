#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import tqdm
import random

from text import *

TRYOUTS = 10000
ERASE_LINE = '\x1b[2K'

WELCOME_MSG = """
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-----------------------------------------------------------------------------
__        __   _                            __  __                       _
\ \      / /__| | ___ ___  _ __ ___   ___  |  \/  | __ _ _ __ __ _  ___ | |_
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |\/| |/ _` | '__/ _` |/ _ \| __|
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | |  | | (_| | | | (_| | (_) | |_
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_|  |_|\__,_|_|  \__, |\___/ \__|
                                                             |___/
-----------------------------------------------------------------------------
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

"""

WELCOME_TEXT = [
    "",
    "",
    ]

YOU_LOOSE = """
__   _____  _   _   _     ___   ___  ____  _____   _
\ \ / / _ \| | | | | |   / _ \ / _ \/ ___|| ____| | |
 \ V / | | | | | | | |  | | | | | | \___ \|  _|   | |
  | || |_| | |_| | | |__| |_| | |_| |___) | |___  |_|
  |_| \___/ \___/  |_____\___/ \___/|____/|_____| (_)
"""

WINNING_PHRASES = [
    "Bonne réponse...pour le moment",
    "Ca ira...pour cette fois",
    ]

QUESTIONS = {
    0: "Quel est la couleur du cheval blanc d'Henri IV ?",
    1: "Quel est le deuxième prénom de ton papa ?",
    }

ANSWERS = {
    0: "blanc",
    1: "alfred",
    }

OUI = [
    "oui",
    "yes",
    "yep",
    "ouep"
    ]

#=======================================================================

def print_slow(text, speed=0.04, skip=True):
    for letter in text:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(speed)
    if skip:
        print('')


def ellipsis():
    for ell in ['.', '..', '...', '.', '..', '...', '.']:
        print('{}\r'.format(ell), end='\r')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(ERASE_LINE)
    print('')


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

#==================================================

def welcome():
    # print(WELCOME_MSG)
    print_slow(WELCOME_MSG, speed=0.01)
    for sentence in WELCOME_TEXT:
        print_slow(sentence)

    res = input("Veux-tu tenter ta chance ?\n")
    if res.lower() not in OUI:
        sys.exit(2)


def ask_question(question_id):
    tries = 0
    clear_screen()
    print_slow(QUESTIONS[question_id])
    print('')
    while tries < TRYOUTS:
        res = input('Ta réponse : ')
        ellipsis()
        if res.lower() == ANSWERS[question_id]:
            print_slow(random.choice(WINNING_PHRASES))
            print('')
            return True
        else:
            tries += 1
            print_slow("Mauvaise réponse !!!")
            time.sleep(2)
            if tries == TRYOUTS:
                print_slow("Tes essais sont écoulés..")
                print('')
            else:
                print_slow("Il te reste {} essai(s)..".format(TRYOUTS-tries))
            print('')
    return False


def final():
    print('Déchiffrement en cours..')
    for _ in tqdm.tqdm(range(1000)):
        time.sleep(0.01)
    print('Déchiffrement terminé !')


def main():
    clear_screen()
    welcome()
    idx = 0
    has_won = True
    while has_won:
        has_won = ask_question(idx)
        idx += 1
        if idx == len(QUESTIONS):
            final()
            sys.exit(1)
        time.sleep(5)
    print(YOU_LOOSE)


if __name__ == '__main__':
    main()

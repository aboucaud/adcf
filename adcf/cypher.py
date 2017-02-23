#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

import os
import sys
import time
import tqdm
import random
import getpass

from adcf.text import *

USERNAME = ['agentz', 'agent z', 'agent_z', 'z']
PASSWORD = 'testatur'


def print_slow(text, speed=0.04, skip_lines=1):
    for letter in text:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(speed)
    if skip_lines > 0:
        print('\n' * (skip_lines - 1))


def ellipsis():
    ERASE_LINE = '\x1b[2K'
    for ell in ['.', '..', '...', '.', '..', '...', '.']:
        print('{}\r'.format(ell), end='\r')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(ERASE_LINE)
    print('')


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

#==================================================

def valid_entry():
    """
    Prompt a username and password
    """
    clear_screen()
    user = input("Identifiant: ")
    valid_user = user.lower() in USERNAME

    if not valid_user:
        print_slow('\nIdentifiant inconnu\n')
        time.sleep(2)
        return False

    pwd = getpass.getpass(prompt='Mot de passe: ')
    valid_pwd = pwd.lower() == PASSWORD

    if not valid_pwd:
        print_slow('\nMauvais mot de passe\n')
        time.sleep(2)
        return False

    return True


def decrypt():
    """
    Mock decryption process timer
    """
    clear_screen()
    print('Déchiffrement en cours..')
    for _ in tqdm.tqdm(range(1000)):
        time.sleep(0.01)
    print('Déchiffrement terminé !')
    time.sleep(2)


def welcome():
    """
    Welcome Logo and disclaimer + option menu
    """
    clear_screen()
    print_slow(LOGO, speed=0.01, skip_lines=2)

    print_slow('-' * 80, speed=0.01)
    print_slow(DISCLAIMER)
    print_slow('-' * 80, speed=0.01, skip_lines=2)

    choice = show_options(WELCOME_TEXT)

    return choice


def show_options(text):
    if text is not None:
        print_slow(text, skip_lines=1)

    print_slow(OPTIONS, speed=0.01, skip_lines=2)

    res = input("Entrez votre choix: ")

    time.sleep(1)

    return res


def main():
    start = False
    while not start:
        start = valid_entry()
    decrypt()
    choice = welcome()
    while True:
        clear_screen()
        if choice in '012':
            text = CHOICES[choice]
            choice = show_options(text)
        else:
            print_slow("Je n'ai pas compris votre choix..")
            time.sleep(2)
            clear_screen()
            choice = show_options(None)


if __name__ == '__main__':
    main()

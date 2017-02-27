# -*- coding: utf-8 -*-
from __future__ import unicode_literals

USERNAME = [
    'agents',
    'agent s',
    'agent_s',
    'agent-s',
    's'
    ]

PASSWORD = 'lipton'

LOGO = """
...............................................................................
.....................{[=================================]}.....................
.....................{[=      _    ____   ____ _____   =]}.....................
.....................{[=     / \  |  _ \ / ___|  ___|  =]}.....................
.....................{[=    / _ \ | | | | |   | |_     =]}.....................
.....................{[=   / ___ \| |_| | |___|  _|    =]}.....................
.....................{[=  /_/   \_\____/ \____|_|      =]}.....................
.....................{[=================================]}.....................
...............................................................................

"""

DISCLAIMER = """
    Toutes les informations suivantes sont strictement confidentielles et
    destinées uniquement aux membres de l'Agence.
    L'utilisation, la copie ou la divulgation non autorisée de ces informa-
    tions (en intégralité ou en partie) est formellement interdite et fera
    l'objet de poursuites pouvant mener à des sanctions exemplaires.
"""

NOT_UNDERSTOOD = """
  Je n'ai pas compris votre choix..
"""


OPTIONS = """
---

  0 - Menu principal
  1 - Agenda
  2 - Infos
"""

WELCOME_TEXT = """
  Bonjour Agent S,

  Vous trouverez ci-dessous votre agenda de la semaine.

  Les informations sur votre contact de secours s'y trouvent également.

  Heureux de vous revoir parmi nous !
"""

AGENDA = """

    Semaine du 20 au 26 Février
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    MARDI
    -----
    18h13 - TGV - Gare du Nord => London St Pancras

    MERCREDI
    --------
    10h00 - Linnean Society - Council Room, Piccadilly, Mayfair
    18h00 - The Mayflower Pub - 117 Rotherhithe St, Rotherhithe
    20h15 - Anchor Bankside Pub - 34 Park St, Southwark

    JEUDI
    -----
    09h00 - Royal Astronomical Society - Library, Piccadilly, Mayfair
    20h00 - 42A Cross St, Islington

    VENDREDI
    --------
    10h00 - Saint Espresso - 26 Pentoville Rd, Angel House
    16h01 - TGV - London St Pancras => Paris Gare du Nord

    SAMEDI
    ------
    17h30 - Grande allée du Jardin des Plantes au pied de l'arbre en fleurs
"""

INFOS = """
   "Le garçon mange le pain"
"""

CHOICES = {
    '0': WELCOME_TEXT,
    '1': AGENDA,
    '2': INFOS,
}

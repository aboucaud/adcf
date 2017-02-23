# -*- coding: utf-8 -*-
from __future__ import unicode_literals


LOGO = """
...............................................................................
..................{[=================================]}........................
..................{[=      _    ____   ____ _____   =]}........................
..................{[=     / \  |  _ \ / ___|  ___|  =]}........................
..................{[=    / _ \ | | | | |   | |_     =]}........................
..................{[=   / ___ \| |_| | |___|  _|    =]}........................
..................{[=  /_/   \_\____/ \____|_|      =]}........................
..................{[=================================]}........................
...............................................................................

"""

DISCLAIMER = """
    Toutes les informations suivantes sont strictement confidentielles et
    destinées uniquement aux membres de l'ADCF.
    L'utilisation, la copie ou la divulgation non autorisée de ces informa-
    tions (en intégralité ou en partie) est formellement interdite et fera
    l'objet de poursuites pouvant mener à des sanctions exemplaires.
"""

OPTIONS = """
0 - Menu principal
1 - Agenda
2 - Infos
"""

WELCOME_TEXT = """
  Bonjour Agent Z,

  Vous trouverez ci-dessous un agenda des missions de l'agence tenu à jour
  au cas où vous vous decideriez à reprendre du service.

  Les information sur votre contact de secours s'y trouvent également.

  Heureux de vous revoir parmi nous !
"""

AGENDA = """
...
"""

INFOS = """
...
"""

CHOICES = {
    '0': WELCOME_TEXT,
    '1': AGENDA,
    '2': INFOS,
}

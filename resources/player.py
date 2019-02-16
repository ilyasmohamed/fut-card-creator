from enum import Enum

from resources.languages_dictionary import languages_dict
from resources.language import Language
from resources.exceptions import InvalidPositionError, InvalidLanguageError


class Player:
    def __init__(self, name, pos, club, country, overall=99, pac=99, dri=99, sho=99, deff=99, pas=99, phy=99, language='EN'):
        self.name = name.upper()

        try:
            self.language = Language[language]
        except KeyError:
            raise InvalidLanguageError(f'Language ({language}) is not a valid language.')

        try:
            position = Enum('Position', languages_dict.get(language).get('positions'))
            self.position = position[pos.upper()]
        except KeyError:
            raise InvalidPositionError(f'Position ({pos}) is not available in language {language}.')

        self.club = club
        self.country = country.lower()

        self.overall = str(overall).zfill(2)
        self.pac = str(pac).zfill(2)
        self.dri = str(dri).zfill(2)
        self.sho = str(sho).zfill(2)
        self.deff = str(deff).zfill(2)
        self.pas = str(pas).zfill(2)
        self.phy = str(phy).zfill(2)

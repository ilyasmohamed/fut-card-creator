class InvalidCardCodeError(Exception):
    """Raised when an invalid card code is passed to the cardcreator"""
    pass


class InvalidCountryCodeError(Exception):
    """Raised when an invalid country code is passed to the cardcreator"""
    pass


class InvalidClubNumberError(Exception):
    """Raised when an invalid club number is passed to the cardcreator"""
    pass


class InvalidPositionError(Exception):
    """Raised when an invalid club number is passed to the cardcreator"""
    pass


class InvalidLanguageError(Exception):
    """Raised when an invalid language is passed to the cardcreator"""
    pass

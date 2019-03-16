from resources.dimensions.Fifa19StandardDimensions import Dimensions as fifa19_standard_dimensions
from resources.dimensions.Fifa19UclDimensions import Dimensions as fifa19_ucl_dimensions


class Card:
    def __init__(self, background_image_dir, font_colour_tuple, fonts_tuple, dimensions):
        self.background_image_dir = background_image_dir
        self.font_colour_tuple = font_colour_tuple
        self.fonts_tuple = fonts_tuple
        self.dimensions = dimensions

    def factory(card_type, background_image_dir, font_colour_tuple, fonts_tuple):
        if card_type == "FIFA19_UCL":
            return Fifa19ChampionsLeagueCard(background_image_dir, font_colour_tuple, fonts_tuple)
        else:
            return Fifa19StandardCard(background_image_dir, font_colour_tuple, fonts_tuple)

    factory = staticmethod(factory)


class Fifa19StandardCard(Card):
    def __init__(self, background_image_dir, font_colour_tuple, fonts_tuple):
        Card.__init__(self, background_image_dir, font_colour_tuple, fonts_tuple, fifa19_standard_dimensions())


class Fifa19ChampionsLeagueCard(Card):
    def __init__(self, background_image_dir, font_colour_tuple, fonts_tuple):
        Card.__init__(self, background_image_dir, font_colour_tuple, fonts_tuple, fifa19_ucl_dimensions())

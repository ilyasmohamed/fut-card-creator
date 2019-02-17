from PIL import ImageFont

DINProCond = "assets/19/fonts/DINPro-Cond.otf"
DINProCondMedium = "assets/19/fonts/DINPro-CondMedium.otf"
DINProCondBold = "assets/19/fonts/DINPro-CondBold.otf"

ChampionsRegular = "assets/19/fonts/Champions-Regular.otf"
ChampionsBold = "assets/19/fonts/Champions-Bold.ttf"


'''
FONTS_FORMAT = (Overall Font,
                Position Font,
                Name Font,
                Attribute value Font,
                Attribute label Font)
'''

dinpro_fonts = (ImageFont.truetype(DINProCondMedium, 120),
                ImageFont.truetype(DINProCond, 50),
                ImageFont.truetype(DINProCondBold, 70),
                ImageFont.truetype(DINProCondBold, 55),
                ImageFont.truetype(DINProCond, 50))

champions_fonts = (ImageFont.truetype(ChampionsRegular, 115),
                   ImageFont.truetype(ChampionsRegular, 50),
                   ImageFont.truetype(ChampionsRegular, 70),
                   ImageFont.truetype(ChampionsBold, 50),
                   ImageFont.truetype(ChampionsRegular, 50))

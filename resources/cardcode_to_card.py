from card import Card
from resources.colours import *
from resources.fonts import dinpro_fonts, champions_fonts


# dictionary which maps a card code to a card object
cardcode_to_card = {
    'COMMON_BRONZE': Card.factory('FIFA19_STD', 'assets/19/cards/common_bronze.png', (COMMON_BRONZE, COMMON_BRONZE), dinpro_fonts),
    'COMMON_SILVER': Card.factory('FIFA19_STD', 'assets/19/cards/common_silver.png', (COMMON_SILVER, COMMON_SILVER), dinpro_fonts),
    'COMMON_GOLD': Card.factory('FIFA19_STD', 'assets/19/cards/common_gold.png', (COMMON_GOLD, COMMON_GOLD), dinpro_fonts),

    'RARE_BRONZE': Card.factory('FIFA19_STD', 'assets/19/cards/rare_bronze.png', (RARE_BRONZE, RARE_BRONZE), dinpro_fonts),
    'RARE_SILVER': Card.factory('FIFA19_STD', 'assets/19/cards/rare_silver.png', (RARE_SILVER, RARE_SILVER), dinpro_fonts),
    'RARE_GOLD': Card.factory('FIFA19_STD', 'assets/19/cards/rare_gold.png', (RARE_GOLD, RARE_GOLD), dinpro_fonts),

    'IF_BRONZE': Card.factory('FIFA19_STD', 'assets/19/cards/if_bronze.png', (IF_BRONZE, IF_BRONZE), dinpro_fonts),
    'IF_SILVER': Card.factory('FIFA19_STD', 'assets/19/cards/if_silver.png', (IF_SILVER, IF_SILVER), dinpro_fonts),
    'IF_GOLD': Card.factory('FIFA19_STD', 'assets/19/cards/if_gold.png', (IF_GOLD, IF_GOLD), dinpro_fonts),

    'LEGEND': Card.factory('FIFA19_STD', 'assets/19/cards/legend.png', (LEGEND, LEGEND), dinpro_fonts),

    'MOTM': Card.factory('FIFA19_STD', 'assets/19/cards/motm.png', (WHISPER, WHISPER), dinpro_fonts),
    'FUTTIES': Card.factory('FIFA19_STD', 'assets/19/cards/futties.png', (WHISPER, WHISPER), dinpro_fonts),
    'PP': Card.factory('FIFA19_STD', 'assets/19/cards/pro_player.png', (WHISPER, WHISPER), dinpro_fonts),

    'RB': Card.factory('FIFA19_STD', 'assets/19/cards/record_breaker.png', (SPRING_BUD, SPRING_BUD), dinpro_fonts),

    'HERO': Card.factory('FIFA19_STD', 'assets/19/cards/hero.png', (PHOCA, PHOCA), dinpro_fonts),

    'HEADLINERS': Card.factory('FIFA19_STD', 'assets/19/cards/headliners.png', (WHISPER, WHISPER), dinpro_fonts),

    'TOTY': Card.factory('FIFA19_STD', 'assets/19/cards/toty.png', (PORTICA, PORTICA), dinpro_fonts),
    'TOTY_N': Card.factory('FIFA19_STD', 'assets/19/cards/toty_nominees.png', (PORTICA, PORTICA), dinpro_fonts),

    'EL': Card.factory('FIFA19_STD', 'assets/19/cards/europa_league.png', (TANGERINE, TANGERINE), dinpro_fonts),
    'EL_MOTM': Card.factory('FIFA19_STD', 'assets/19/cards/europa_league_motm.png', (WHITE_SMOKE, BLACK), dinpro_fonts),
    'EL_LIVE': Card.factory('FIFA19_STD', 'assets/19/cards/europa_league_live.png', (TANGERINE, TANGERINE), dinpro_fonts),
    'EL_SBC': Card.factory('FIFA19_STD', 'assets/19/cards/europa_league_sbc.png', (BLACK, BLACK), dinpro_fonts),
    'EL_TOTT': Card.factory('FIFA19_STD', 'assets/19/cards/europa_league_tott.png', (WHITE_SMOKE, WHITE_SMOKE), dinpro_fonts),

    'COMMON_UCL': Card.factory('FIFA19_UCL', 'assets/19/cards/ucl_common.png', (WHISPER, WHISPER), champions_fonts),
    'RARE_UCL': Card.factory('FIFA19_UCL', 'assets/19/cards/ucl_rare.png', (WHISPER, WHISPER), champions_fonts),
    'UCL_MOTM': Card.factory('FIFA19_UCL', 'assets/19/cards/ucl_motm.png', (WHISPER, WHISPER), champions_fonts),
    'UCL_LIVE': Card.factory('FIFA19_UCL', 'assets/19/cards/ucl_live.png', (WHISPER, WHISPER), champions_fonts),
    'UCL_SBC': Card.factory('FIFA19_UCL', 'assets/19/cards/ucl_sbc.png', (WHISPER, WHISPER), champions_fonts),
    'UCL_TOTT': Card.factory('FIFA19_UCL', 'assets/19/cards/ucl_tott.png', (WHISPER, WHISPER), champions_fonts)
}

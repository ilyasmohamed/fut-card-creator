from resources.colours import *
from resources.fonts import *

DINPRO_FONTS = (DINProCond, DINProCondMedium, DINProCondBold)
CHAMPIONS_FONTS = (ChampionsBold, ChampionsBold, ChampionsBold)

# value tuple will be in the form (img dir, (font colours tuple), (fonts tuple))
cardcode_to_resources = {
    'COMMON_BRONZE': ('assets/19/cards/common_bronze.png', (COMMON_BRONZE, COMMON_BRONZE), DINPRO_FONTS),
    'COMMON_SILVER': ('assets/19/cards/common_silver.png', (COMMON_SILVER, COMMON_SILVER), DINPRO_FONTS),
    'COMMON_GOLD': ('assets/19/cards/common_gold.png', (COMMON_GOLD, COMMON_GOLD), DINPRO_FONTS),

    'RARE_BRONZE': ('assets/19/cards/rare_bronze.png', (RARE_BRONZE, RARE_BRONZE), DINPRO_FONTS),
    'RARE_SILVER': ('assets/19/cards/rare_silver.png', (RARE_SILVER, RARE_SILVER), DINPRO_FONTS),
    'RARE_GOLD': ('assets/19/cards/rare_gold.png', (RARE_GOLD, RARE_GOLD), DINPRO_FONTS),

    'IF_BRONZE': ('assets/19/cards/if_bronze.png', (IF_BRONZE, IF_BRONZE), DINPRO_FONTS),
    'IF_SILVER': ('assets/19/cards/if_silver.png', (IF_SILVER, IF_SILVER), DINPRO_FONTS),
    'IF_GOLD': ('assets/19/cards/if_gold.png', (IF_GOLD, IF_GOLD), DINPRO_FONTS),

    'LEGEND': ('assets/19/cards/legend.png', (LEGEND, LEGEND), DINPRO_FONTS),

    'MOTM': ('assets/19/cards/motm.png', (WHISPER, WHISPER), DINPRO_FONTS),
    'FUTTIES': ('assets/19/cards/futties.png', (WHISPER, WHISPER), DINPRO_FONTS),
    'PP': ('assets/19/cards/pro_player.png', (WHISPER, WHISPER), DINPRO_FONTS),

    'RB': ('assets/19/cards/record_breaker.png', (SPRING_BUD, SPRING_BUD), DINPRO_FONTS),

    'HERO': ('assets/19/cards/hero.png', (PHOCA, PHOCA), DINPRO_FONTS),

    'HEADLINERS': ('assets/19/cards/headliners.png', (WHISPER, WHISPER), DINPRO_FONTS),

    'TOTY': ('assets/19/cards/toty.png', (PORTICA, PORTICA), DINPRO_FONTS),
    'TOTY_N': ('assets/19/cards/toty_nominees.png', (PORTICA, PORTICA), DINPRO_FONTS),

    'EL': ('assets/19/cards/europa_league.png', (TANGERINE, TANGERINE), DINPRO_FONTS),
    'EL_MOTM': ('assets/19/cards/europa_league_motm.png', (WHITE_SMOKE, BLACK), DINPRO_FONTS),
    'EL_LIVE': ('assets/19/cards/europa_league_live.png', (TANGERINE, TANGERINE), DINPRO_FONTS),
    'EL_SBC': ('assets/19/cards/europa_league_sbc.png', (BLACK, BLACK), DINPRO_FONTS),
    'EL_TOTT': ('assets/19/cards/europa_league_tott.png', (WHITE_SMOKE, WHITE_SMOKE), DINPRO_FONTS)

    # 'COMMON_UCL': ('assets/19/cards/ucl_nonrare.png', (WHISPER, WHISPER), CHAMPIONS_FONTS),
    # 'RARE_UCL': ('assets/19/cards/ucl_rare.png', (WHISPER, WHISPER), CHAMPIONS_FONTS),
    # 'UCL_MOTM': ('assets/19/cards/ucl_motm.png', (WHISPER, WHISPER), CHAMPIONS_FONTS),
    # 'UCL_SPECIAL1': ('assets/19/cards/ucl_special_1.png', (WHISPER, WHISPER), CHAMPIONS_FONTS),
    # 'UCL_SPECIAL2': ('assets/19/cards/ucl_special_2.png', (WHISPER, WHISPER), CHAMPIONS_FONTS),
    # 'UCL_SPECIAL3': ('assets/19/cards/ucl_special_3.png', (WHISPER, WHISPER), CHAMPIONS_FONTS)
}

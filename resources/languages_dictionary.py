# a dictionary which contains a dictionary for each language (key is language code) which
# contains the corresponding position abbreviations and card stat labels
languages_dict = {
    'EN': {
        'positions': ('GK',
                      'LB', 'LWB', 'CB', 'RB', 'RWB',
                      'LM', 'CDM', 'CM', 'CAM', 'RM',
                      'LW', 'RW',
                      'LF', 'CF', 'RF',
                      'ST'),
        'attribute_labels': ('PAC', 'DRI',
                             'SHO', 'DEF',
                             'PAS', 'PHY')
    },

    'FR': {
        'positions': ('G',
                      'DG', 'DC', 'DD',
                      'MG', 'MDC', 'MC', 'MOC', 'MD',
                      'AG', 'AD',
                      'AVG', 'AT', 'AVD',
                      'BU'),
        'attribute_labels': ('VIT', 'DRI',
                             'TIR', 'DÉF',
                             'PAS', 'PHY')
    },

    'ES': {
        'positions': ('POR',
                      'LTI', 'CAI', 'DFC', 'LTD', 'CAD',
                      'MI', 'MCD', 'MC', 'MCO', 'MD',
                      'EI', 'ED',
                      'SDI', 'MP', 'SDD',
                      'DC'
                      ),
        'attribute_labels': ('RIT', 'REG',
                             'TIR', 'DEF',
                             'PAS', 'FÍS')
    },

    'PT': {
        'positions': ('GOL',
                      'LE', 'ADE', 'ZAG', 'LD', 'ADD',
                      'ME', 'VOL', 'MC', 'MEI', 'MD',
                      'PE', 'PD',
                      'MAE', 'SA', 'MAD',
                      'ATA'
                      ),
        'attribute_labels': ('RIT', 'DRI',
                             'FIN', 'DEF',
                             'PAS', 'FIS')
    },

    'IT': {
        'positions': ('POR',
                      'TS', 'ASA', 'DC', 'TD', 'ADA',
                      'ES', 'CDC', 'CC', 'COC', 'ED',
                      'AS', 'AD',
                      'ATS', 'AT', 'ATD',
                      'ATT'),
        'attribute_labels': ('VEL', 'DRI',
                             'TIR', 'DIF',
                             'PAS', 'FIS')
    },

    'DE': {
        'positions': ('TW',
                      'LV', 'LAV', 'IV', 'RV', 'RAV',
                      'LM', 'ZDM', 'ZM', 'ZOM', 'RM',
                      'LF', 'RF',
                      'LAS', 'MS', 'RAS',
                      'ST'),
        'attribute_labels': ('TEM', 'DRI',
                             'SCH', 'DEF',
                             'PAS', 'PHY')
    }
}

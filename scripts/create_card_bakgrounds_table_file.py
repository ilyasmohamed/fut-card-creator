from resources.cardcode_to_card import cardcode_to_card


with open('output/card_backgrounds_table.txt', 'w') as writer:
    writer.write('| Card Name | Card Code | Card |\n')
    writer.write('| :---------: | :-----------: | :--: |\n')

    for card_code in cardcode_to_card:
        card = cardcode_to_card.get(card_code)

        card_background_dir = card.background_image_dir
        card_background_link = f'![{card_code}]({card_background_dir})'
        card_background_link = f'<img src="https://github.com/ilyasmohamed/fut-card-creator/blob/master/{card_background_dir}" width="20%">'

        card_name = card_background_dir.split('/')[-1]
        card_name = card_name[:-4].replace('_', ' ').title()

        writer.write(f'| {card_name} | {card_code} | {card_background_link} |\n')

writer.close()

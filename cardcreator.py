import os
from io import BytesIO

import requests
from PIL import Image, ImageDraw

from resources.cardcode_to_card import cardcode_to_card
from resources.exceptions import *
from resources.languages_dictionary import languages_dict


def render_card(player, card_code, player_image_url, status_id):
    card_obj = cardcode_to_card.get(card_code.upper())

    if card_obj is None:
        raise InvalidCardCodeError(f'Card code ({card_code}) is invalid.')

    card_background = card_obj.background_image_dir
    font_colour_top = card_obj.font_colour_tuple[0]
    font_colour_bottom = card_obj.font_colour_tuple[1]
    fonts_tuple = card_obj.fonts_tuple

    card_bg_img = Image.open(card_background).convert('RGBA')
    draw = ImageDraw.Draw(card_bg_img)

    # prepare fonts ready for use
    overall_font = fonts_tuple[0]
    position_font = fonts_tuple[1]
    name_font = fonts_tuple[2]
    attribute_value_font = fonts_tuple[3]
    attribute_label_font = fonts_tuple[4]

    w, h = draw.textsize(player.name, name_font)
    w2, h2 = draw.textsize(player.position.name, position_font)

    player_name_left_margin = (card_bg_img.width - w) / 2
    player_position_left_margin = card_obj.dimensions.left_margin + 50 - (w2 / 2)

    add_player_name_overall_and_position(draw, card_obj, font_colour_top, font_colour_bottom, player_name_left_margin,
                                         player_position_left_margin, player, name_font, overall_font, position_font)

    add_player_attributes_section(draw, card_obj, font_colour_bottom, player, attribute_value_font, attribute_label_font)

    add_separator_lines(draw, card_obj, font_colour_top, font_colour_bottom)

    if player_image_url is not None:
        temp_path = 'temp'
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)

        temp_filename = f'{status_id}.png'
        temp_file_path = os.path.join(temp_path, temp_filename)

        request = requests.get(player_image_url, stream=True)
        if request.status_code == 200:
            # read data from downloaded bytes and returns a PIL.Image.Image object
            i = Image.open(BytesIO(request.content))
            # Saves the image under the given filename
            i.save(temp_file_path)

        stamp_player_image(card_bg_img, card_obj, temp_file_path)

    stamp_country_flag_and_club_badge(card_bg_img, player)

    save_path = 'finished-fut-cards'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    save_filename = f'{status_id}.png'
    output_file_path = os.path.join(save_path, save_filename)
    card_bg_img.save(output_file_path)
    return output_file_path


def stamp_player_image(card_bg_img, card_obj, player_image_filename):
    player_img = Image.open(player_image_filename).convert('RGBA')
    player_img = player_img.resize((320, 320))

    card_bg_img.paste(player_img, (card_obj.dimensions.left_margin_player_image, card_bg_img.height - player_img.height - 383), player_img)


def stamp_country_flag_and_club_badge(card_obj, card_bg_img, player):
    try:
        country_flag_img = Image.open(f"assets/nations/png100px/{player.country}.png").convert('RGBA')
    except FileNotFoundError:
        raise InvalidCountryCodeError(f'Country code ({player.country}) is invalid.')

    country_flag_img_width = 166
    country_flag_img_height = 99
    country_flag_img_width = int(country_flag_img_width * 0.48)
    country_flag_img_height = int(country_flag_img_height * 0.48)
    country_flag_img = country_flag_img.resize((country_flag_img_width, country_flag_img_height))

    try:
        club_badge_img = Image.open(f"assets/clubs/{player.club}.png").convert('RGBA')
    except FileNotFoundError:
        raise InvalidClubNumberError(f'Club number ({player.club}) is invalid.')

    club_badge_img_width, club_badge_img_height = club_badge_img.size
    club_badge_img_width = int(club_badge_img_width * 0.55)
    club_badge_img_height = int(club_badge_img_height * 0.55)
    club_badge_img = club_badge_img.resize((club_badge_img_width, club_badge_img_height), Image.LANCZOS)

    # paste the country flag and club badge
    card_bg_img.paste(country_flag_img, (card_obj.dimensions.left_margin + 10, 272), country_flag_img)
    card_bg_img.paste(club_badge_img, (card_obj.dimensions.left_margin_club_badge, 350), club_badge_img)


def add_player_attributes_section(draw, card_obj, font_colour, player, attribute_value_font, attribute_label_font):
    language_code = player.language.name

    atr1_label = languages_dict.get(language_code).get('attribute_labels')[0]
    atr2_label = languages_dict.get(language_code).get('attribute_labels')[1]
    atr3_label = languages_dict.get(language_code).get('attribute_labels')[2]
    atr4_label = languages_dict.get(language_code).get('attribute_labels')[3]
    atr5_label = languages_dict.get(language_code).get('attribute_labels')[4]
    atr6_label = languages_dict.get(language_code).get('attribute_labels')[5]

    '''
    Draw the first column of stats and labels
    '''
    # PAC attr and label
    draw.text((card_obj.dimensions.left_margin_attr_value_col1, card_obj.dimensions.top_margin_stats_row_1_values), str(player.pac), fill=font_colour,
              font=attribute_value_font)
    draw.text((card_obj.dimensions.left_margin_attr_label_col1, card_obj.dimensions.top_margin_stats_row_1_labels), atr1_label, fill=font_colour, font=attribute_label_font)
    # SHO attr and label
    draw.text((card_obj.dimensions.left_margin_attr_value_col1, card_obj.dimensions.top_margin_stats_row_2_values), str(player.sho), fill=font_colour,
              font=attribute_value_font)
    draw.text((card_obj.dimensions.left_margin_attr_label_col1, card_obj.dimensions.top_margin_stats_row_2_labels), atr3_label, fill=font_colour, font=attribute_label_font)
    # PAS attr and label
    draw.text((card_obj.dimensions.left_margin_attr_value_col1, card_obj.dimensions.top_margin_stats_row_3_values), str(player.pas), fill=font_colour,
              font=attribute_value_font)
    draw.text((card_obj.dimensions.left_margin_attr_label_col1, card_obj.dimensions.top_margin_stats_row_3_labels), atr5_label, fill=font_colour, font=attribute_label_font)

    '''
    Draw the second column of stats and labels
    '''
    # DRI attr and label
    draw.text((card_obj.dimensions.left_margin_attr_value_col2, card_obj.dimensions.top_margin_stats_row_1_values), str(player.dri), fill=font_colour,
              font=attribute_value_font)
    draw.text((card_obj.dimensions.left_margin_attr_label_col2, card_obj.dimensions.top_margin_stats_row_1_labels), atr2_label, fill=font_colour, font=attribute_label_font)
    # DEF attr and label
    draw.text((card_obj.dimensions.left_margin_attr_value_col2, card_obj.dimensions.top_margin_stats_row_2_values), str(player.deff), fill=font_colour,
              font=attribute_value_font)
    draw.text((card_obj.dimensions.left_margin_attr_label_col2, card_obj.dimensions.top_margin_stats_row_2_labels), atr4_label, fill=font_colour, font=attribute_label_font)
    # PHY attr and label
    draw.text((card_obj.dimensions.left_margin_attr_value_col2, card_obj.dimensions.top_margin_stats_row_3_values), str(player.phy), fill=font_colour,
              font=attribute_value_font)
    draw.text((card_obj.dimensions.left_margin_attr_label_col2, card_obj.dimensions.top_margin_stats_row_3_labels), atr6_label, fill=font_colour, font=attribute_label_font)


def add_player_name_overall_and_position(draw, card_obj, font_colour_top, font_colour_bottom, player_name_left_margin, player_position_left_margin,
                                         player, namefont, overallfont, positionfont):
    # add player name
    draw.text((player_name_left_margin, card_obj.dimensions.top_margin_name), player.name.upper(), fill=font_colour_bottom, font=namefont)
    # add player overall rating
    draw.text((card_obj.dimensions.left_margin, card_obj.dimensions.top_margin_player_overall), str(player.overall), fill=font_colour_top, font=overallfont)
    # add player position
    draw.text((player_position_left_margin, card_obj.dimensions.top_margin_position), player.position.name, fill=font_colour_top, font=positionfont)


def add_separator_lines(draw, card_obj, font_colour_top, font_colour_bottom):
    LINE_WIDTH = 1

    # draw line under position
    draw.line((card_obj.dimensions.left_point_x_coordinate_line_under_position, card_obj.dimensions.top_margin_line_under_position,
               card_obj.dimensions.right_point_x_coordinate_line_under_position, card_obj.dimensions.top_margin_line_under_position),
              fill=font_colour_top, width=LINE_WIDTH)

    # draw line under country flag
    draw.line((card_obj.dimensions.left_point_x_coordinate_line_under_position, card_obj.dimensions.top_margin_line_under_country_flag,
               card_obj.dimensions.right_point_x_coordinate_line_under_position, card_obj.dimensions.top_margin_line_under_country_flag),
              fill=font_colour_top, width=LINE_WIDTH)

    # draw line under name
    draw.line((card_obj.dimensions.margin_line_under_name, card_obj.dimensions.top_margin_line_under_name,
               draw.im.size[0] - card_obj.dimensions.margin_line_under_name, card_obj.dimensions.top_margin_line_under_name),
              fill=font_colour_bottom, width=LINE_WIDTH)

    # draw line under stats
    draw.line((card_obj.dimensions.margin_line_under_stats, card_obj.dimensions.top_margin_line_under_stats,
               draw.im.size[0] - card_obj.dimensions.margin_line_under_stats, card_obj.dimensions.top_margin_line_under_stats),
              fill=font_colour_bottom, width=LINE_WIDTH)

    # draw vertical line between stats columns
    draw.line(((draw.im.size[0] / 2), card_obj.dimensions.top_margin_vertical_line_between_stats_columns,
               (draw.im.size[0] / 2), card_obj.dimensions.bottom_point_vertical_line_between_stats_columns),
              fill=font_colour_bottom, width=LINE_WIDTH)

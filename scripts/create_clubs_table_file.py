from os import listdir
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split(r'(\d+)', text)]


club_badge_imgs_list = listdir('../assets/clubs')
club_badge_imgs_list.sort(key=natural_keys)

with open('output/clubs_table.txt', 'w') as writer:
    writer.write('| Club Name | Club Code | Badge |\n')
    writer.write('| :-------: | :-------: | :----: |\n')

    for club in club_badge_imgs_list:
        club_code = club[:-4]
        club_badge_img_dir = f'assets/clubs/{club_code}.png'
        club_badge_img_link = f'<img src="https://github.com/ilyasmohamed/fut-card-creator/blob/master/{club_badge_img_dir}" width="20%">'
        writer.write(f'| | {club_code} | {club_badge_img_link} |\n')

writer.close()

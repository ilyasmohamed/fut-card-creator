try:
    import simplejson as json
except ImportError:
    import json


with open('../assets/nations/countries.json') as f:
    data = json.load(f)

with open('output/countries_table.txt', 'w') as writer:
    writer.write('| Country | Country Code | Flag |\n')
    writer.write('| :-------: | :------------: | :----: |\n')

    for d in data:
        encoded_country_name = data[d]
        flag_img_dir = f'![{d}](assets/nations/png100px/{d.lower()}.png)'
        writer.write(f'| {encoded_country_name} | {d} | {flag_img_dir} |\n')

writer.close()

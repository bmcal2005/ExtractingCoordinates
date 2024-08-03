import json
import csv

with open('c:/Users/bmcal/Downloads/e_coli_core.Core metabolism.json', 'r') as file:
    data = json.load(file)

if isinstance(data, list) and len(data) > 1:
    reactions_data = data[1].get('reactions', {})
else:
    reactions_data = {}

with open('reactions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y', 'full_name', 'bigg_id'])

    #this is to iterate over reactions
    for reaction_id, reaction_info in reactions_data.items():
        x = reaction_info['label_x']
        y = reaction_info['label_y']
        full_name = reaction_info['name']
        bigg_id = reaction_info['bigg_id']

        writer.writerow([x, y, full_name, bigg_id])
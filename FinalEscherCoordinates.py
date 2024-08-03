import json
import csv

# Load the JSON file
with open('c:/Users/bmcal/Downloads/e_coli_core.Core metabolism (1).json', 'r') as file:
    data = json.load(file)

# Extract reactions data
if isinstance(data, list) and len(data) > 1:
    reactions_data = data[1].get('reactions', {})
else:
    reactions_data = {}

# Prepare a list to store all the extracted data
extracted_data = []

# Extract reactions information
for reaction_id, reaction_info in reactions_data.items():
    x = reaction_info['label_x']
    y = reaction_info['label_y']
    full_name = reaction_info['name']
    bigg_id = reaction_info['bigg_id']
    extracted_data.append([x, y, 'reaction', full_name, bigg_id])


if isinstance(data, list) and len(data) > 1:
     metabolites_data = data[1].get('nodes', {})  # Replace with the correct key
else:
     metabolites_data = {}

for metabolite_id, metabolite_info in metabolites_data.items():
     x = metabolite_info.get('x')
     y = metabolite_info.get('y')
     full_name = metabolite_info.get('name')
     bigg_id = metabolite_info.get('bigg_id')  # Assuming there is a bigg_id for metabolites
     extracted_data.append([x, y, 'metabolite', full_name, bigg_id])

# Write extracted data to CSV
with open('eschercoordinates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y', 'type', 'full_name', 'bigg_id'])
    writer.writerows(extracted_data)

print("Data extraction complete. Check 'eschercoordinates.csv' for the results.")
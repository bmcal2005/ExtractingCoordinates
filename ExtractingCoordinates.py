import json
import csv

# Loading JSON file
with open('c:/Users/bmcal/Downloads/e_coli_core.Core metabolism (1).json', 'r') as file:
    data = json.load(file)

# Extract reactions data
if isinstance(data, list) and len(data) > 1:
    reactions_data = data[1].get('reactions', {})
else:
    reactions_data = {}

# List to store all the extracted data
extracted_data = []

# For reactions information
for reaction_id, reaction_info in reactions_data.items():
    x = reaction_info['label_x']
    y = reaction_info['label_y']
    full_name = reaction_info['name']
    extracted_data.append([x, y, 'reaction', full_name])

if isinstance(data, list) and len(data) > 1:
     metabolites_data = data[1].get('nodes', {})  
else:
     metabolites_data = {}

# For metabolites information
for metabolite_id, metabolite_info in metabolites_data.items():
     x = metabolite_info.get('x')
     y = metabolite_info.get('y')
     full_name = metabolite_info.get('name')
     extracted_data.append([x, y, 'metabolite', full_name])

with open('coordinates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y', 'type', 'full_name'])
    writer.writerows(extracted_data)

# Just so I can easily make sure the coordinates extraction worked
print("Data extraction complete. Check 'coordinates.csv'")
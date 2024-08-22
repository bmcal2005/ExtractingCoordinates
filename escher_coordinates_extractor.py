import json
import csv
import os

def getCoordinatesOfEscherDiagram(json_file):
    try:
        # Load the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)

        # Extract reactions data
        if isinstance(data, list) and len(data) > 1:
            reactions_data = data[1].get('reactions', {})
            metabolites_data = data[1].get('nodes', {})
        else:
            reactions_data = {}
            metabolites_data = {}

        # Prepare a list to store all the extracted data
        extracted_data = []

        # Extract reactions information
        for reaction_id, reaction_info in reactions_data.items():
            x = reaction_info.get('label_x')
            y = reaction_info.get('label_y')
            full_name = reaction_info.get('name')
            bigg_id = reaction_info.get('bigg_id')
            extracted_data.append([x, y, 'reaction', full_name, bigg_id])

        # Extract metabolites information and additional node types
        for node_id, node_info in metabolites_data.items():
            x = node_info.get('x')
            y = node_info.get('y')
            full_name = node_info.get('name')
            bigg_id = node_info.get('bigg_id')
            node_type = node_info.get('node_type', 'metabolite')  # Default to 'metabolite' if 'node_type' not found
            extracted_data.append([x, y, node_type, full_name, bigg_id])

        # Generate the output CSV file name
        base_name = os.path.splitext(os.path.basename(json_file))[0]
        output_csv = f"{base_name}Coord.csv"

        # Write extracted data to CSV
        with open(output_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['x', 'y', 'type', 'full_name', 'bigg_id'])
            writer.writerows(extracted_data)

        print(f"Data extraction complete. Check '{output_csv}' for the results.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    getCoordinatesOfEscherDiagram('c:/Users/bmcal/Downloads/e_coli_core.Core metabolism (1).json')

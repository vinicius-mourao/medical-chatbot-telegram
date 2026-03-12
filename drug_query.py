# import necessary libraries
import requests

def search_drug(drug_name):
    """Function to request the drug's JSON file"""
    try:
        response = requests.get(f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}&limit=1", timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException:
        return None
    

def extract_drug_info(drug_data):
    """Function to extract relevant information from the OpenFDA API response"""
    result = drug_data['results'][0]
    info = {
        'brand_name': result.get('openfda', {}).get('brand_name', ['N/A'])[0],
        'manufacturer_name': result.get('openfda', {}).get('manufacturer_name', ['N/A'])[0],
        'purpose': result.get('purpose', ['N/A'])[0],
        'indications_and_usage': result.get('indications_and_usage', ['N/A'])[0],
        'adverse_reactions': '\n'.join(result.get('adverse_reactions', ['N/A'])),
        'warnings': '\n'.join(result.get('warnings', ['N/A'])),
        'do_not_use': '\n'.join(result.get('do_not_use', ['N/A'])),
        'ask_doctor': '\n'.join(result.get('ask_doctor', ['N/A'])),
        'stop_use': '\n'.join(result.get('stop_use', ['N/A'])),
        'pregnancy': '\n'.join(result.get('pregnancy', ['N/A'])),
        'keep_out_of_reach_of_children': '\n'.join(result.get('keep_out_of_reach_of_children', ['N/A'])),
        'dosage_and_administration': result.get('dosage_and_administration', ['N/A'])[0],
        'storage_and_handling': result.get('storage_and_handling', ['N/A'])[0],
        'inactive_ingredient': '\n'.join(result.get('inactive_ingredient', ['N/A'])),
        'questions': result.get('questions', ['N/A'])[0],
        'generic_name': result.get('openfda', {}).get('generic_name', ['N/A'])[0],
        'route': result.get('openfda', {}).get('route', ['N/A'])[0]

    }
    return info

def display_info(info):
    """Function to display the drug's information"""
    print("\n-------------------- Drug Information --------------------")
    print("---------- Basic Information ----------")
    print(f"Brand Name: {info['brand_name']}")
    print(f"Generic Name: {info['generic_name']}")
    print(f"Route: {info['route']}")
    print(f"Manufacturer Name: {info['manufacturer_name']}")
    print(f"Dosage and Administration: {info['dosage_and_administration']}")
    print("------------- Usage -------------------")
    print(f"Purpose: {info['purpose']}")
    print(f"Indications and Usage: {info['indications_and_usage']}")
    print("--------- Safety Information ----------")
    print(f"Warnings: {info['warnings']}")
    print(f"Do Not Use: {info['do_not_use']}")
    print(f"Stop Use: {info['stop_use']}")
    print(f"Pregnancy: {info['pregnancy']}")
    print(f"Keep Out of Reach of Children: {info['keep_out_of_reach_of_children']}")
    print(f"Adverse Reactions: {info['adverse_reactions']}")
    print(f"Ask Doctor: {info['ask_doctor']}")
    print("-- Additional Information -------------")
    print(f"Storage and Handling: {info['storage_and_handling']}")
    print(f"Inactive Ingredients: {info['inactive_ingredient']}")
    print(f"Questions: {info['questions']}")
    print("----------------------------------------------------------")

def main():
    print("OpenFDA Drug Query")
    while True:
        drug_name = input("Enter drug name (or 'exit' to quit): ").strip()
        drug_name = drug_name.replace(" ", "+")
        if drug_name.lower() == 'exit':
            print("Thank you for using the OpenFDA Drug Query!")
            break
        try:
            drug_data = search_drug(drug_name)
            if drug_data is None:
                print("Drug not found or API error.")
                continue
            info = extract_drug_info(drug_data)
            display_info(info)
        except (KeyError, IndexError):
            print("Error occurred while parsing drug information.")
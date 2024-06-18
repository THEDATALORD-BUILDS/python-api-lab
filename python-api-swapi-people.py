#import dependancies
import requests
import csv

#confirm connection to API is successful
def get_character_name(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("name")
    else:
        return ""

#Recursive logic to add 1 to the number after '/api/people/' to get each user name
def get_character_names_recursive(start_id, end_id, base_url="https://swapi.dev/api/people/"):
    if start_id > end_id:
        return []  # Base case: stop when start_id exceeds end_id
    current_url = f"{base_url}{start_id}/"
    character_name = get_character_name(current_url)
    rest_of_names = get_character_names_recursive(start_id + 1, end_id)
    return [character_name] + rest_of_names

# Define the start ID after '/people/' ie '/people/1'
start_id = 1
end_id = 100
#Run the logic and store in variable named 'export_user_names'
export_user_names = get_character_names_recursive(start_id, end_id)
#print results for confirmation in CLI
print(export_user_names)

# Linking 'names' to 'export_user_names' for ease of logic below
names = export_user_names

# Specify the CSV filename
csv_filename = ".\swapi-people-names3.csv"

# Write the variable to the CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name'])

    # Write the data
    for name in names:
        writer.writerow([name])

print(f"Data written to {csv_filename} successfully!")

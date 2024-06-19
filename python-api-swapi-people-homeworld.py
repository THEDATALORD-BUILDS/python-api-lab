import requests
import csv

# Function to get the name of the homeworld
def get_homeworld(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("name")
    else:
        return ""

# Open (or create) a CSV file for writing
with open('swapi_names_homeworlds.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['name', 'homeworld'])

    # Loop over the people IDs
    for i in range(1, 85):
        url = f"https://swapi.dev/api/people/{i}/"
        response = requests.get(url)
        if response.status_code == 200:
            #full response
            data = response.json()
            #parse name
            name = data.get("name")
            #parse homeworld
            homeworld_url = data.get("homeworld")
            homeworld = get_homeworld(homeworld_url)
            #write values
            writer.writerow([name, homeworld])

print("Data written to swapi_names_homeworlds.csv successfully!")

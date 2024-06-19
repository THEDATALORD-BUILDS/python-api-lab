import requests
import csv

# Function to get the name from a URL
def get_name(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("name")
    else:
        return ""

# Open (or create) a CSV file for writing
with open('swapi_names_homeworlds_vehicles.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['name', 'homeworld', 'vehicles'])

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
            homeworld = get_name(homeworld_url)
            #parse vehicles
            vehicles_urls = data.get("vehicles")
            #vehicles values are stored in url so we are getting those values and storing the output string
            vehicles = [get_name(vehicle_url) for vehicle_url in vehicles_urls]
            #write values
            writer.writerow([name, homeworld, vehicles])

print("Data written to swapi_names_homeworlds_vehicles.csv successfully!")

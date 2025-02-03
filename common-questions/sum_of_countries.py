import requests
from geopy.distance import geodesic


def find_countries(countries,Population_limit) : 
    for country in countries :
        for currency in country['currencies'] :
            if currency['code'] in currencies :
                currencies[currency['code']] += 1
            else:
                currencies[currency['code']] = 1

    for country in countries :
        for currency in country['currencies'] :
            currecy_code = currency['code']
            if currecy_code in currencies and currencies[currecy_code] == 1 and country['population'] >= Population_limit:

                unique_countries[country['name']] = {
                    'population': country['population'],
                    'latitude': country.get('latlng', [0.000, 0.000])[0],  # Default to 0.000 if latitode is missing
                    'longitude': country.get('latlng', [0.000, 0.000])[1],  # Default to 0.000 if longitode is missing
                    'currencies': currency['code'] # Store the currency code(s)
                }
     
def find_sum(coordinates) :
    total_distance = 0
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            # Get the coordinates of the two countries
            country1 = coordinates[i]
            country2 = coordinates[j]
            
            # Calculate the distance between the two countries using geodesic
            distance = geodesic(country1, country2).kilometers
            
            # Add the distance to the total
            total_distance += distance
    total_distance = round(total_distance, 2)
    return total_distance





countries = requests.get("https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json").json()
# population_limit = 65847
population_limit = int(input("Enter Population limit: "))
currencies = {} # stores currencies with count
unique_countries = {}  # countries with exclusive currencies
find_countries(countries,population_limit)
first_20_countries = dict(sorted(unique_countries.items(), key=lambda x: x[1]['population'],reverse= True)[:20])
# print(first_20_countries)
coordinates = [(data['latitude'], data['longitude']) for data in first_20_countries.values()]
print(coordinates)
# print(find_sum(coordinates))


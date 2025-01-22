from geopy.distance import geodesic

# List of coordinates (latitude, longitude) of countries
coordinates = [
    (39.9042, 116.4074),  # Beijing, China
    (28.7041, 77.1025),   # New Delhi, India
    (34.0522, -118.2437), # Los Angeles, USA
    (51.5074, -0.1278),   # London, UK
    # Add more countries here...
]

# Initialize a variable to store the total distance
total_distance = 0

# Loop through each pair of countries
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        # Get the coordinates of the two countries
        country1 = coordinates[i]
        country2 = coordinates[j]
        
        # Calculate the distance between the two countries using geodesic
        distance = geodesic(country1, country2).kilometers
        
        # Add the distance to the total
        total_distance += distance

# Round the total distance to 2 decimal points
total_distance = round(total_distance, 2)

print(f"The total sum of distances is {total_distance} kilometers.")

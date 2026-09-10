import requests
import pandas as pd

# TMDB API URL
url = 'https://api.themoviedb.org/3/trending/movie/day?language=en-US'

# headers
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMzIwZDg1MzE5Mzc4ZjRiNTZmYWU0YzVhM2JkZWMzZSIsIm5iZiI6MTc4NzYzMTM3NS44NCwic3ViIjoiNmE4ZDE3MGZhZDZjNmFhNTAxNWM5YjIyIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.IoDwmCY2tilCGd_2qCHCCY4RUe9zuNkSs9Zcj8wHcrI"
}

# Send GET request
response = requests.get(url, headers=headers)

# Extract movie results from JSON
data = response.json()['results']

# Convert API data into DataFrame
df = pd.DataFrame(data)

# Display DataFrame information
df.info()

# Save DataFrame as CSV
df.to_csv('tmdb_movies.csv', index=False)
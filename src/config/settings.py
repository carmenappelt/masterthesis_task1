# NCEI API endpoint and token
API_TOKEN = "VpTIXLAOakCwxykpCjUkBGRHkULwYwya"
BASE_URL = "https://www.ncei.noaa.gov/access/services/data/v1"
STATIONS_API_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"

# Fallback stations if API request fails
STATIONS = [
    {
        "id": "USW00094728",                 # Central Park, New York NY
        "name": "New York – Central Park",
        "lat": 40.779,
        "lon": -73.969,
    },
    {
        "id": "USW00023174",                 # Los Angeles Intl Airport, CA
        "name": "Los Angeles – LAX",
        "lat": 33.942,
        "lon": -118.408,
    },
    {
        "id": "USW00014819",                 # Chicago O’Hare Intl Airport, IL
        "name": "Chicago – O'Hare",
        "lat": 41.980,
        "lon": -87.904,
    },
    {
        "id": "USW00012960",                 # Houston Bush Intercontinental, TX
        "name": "Houston – Bush Intercontinental",
        "lat": 29.984,
        "lon": -95.341,
    },
    {
        "id": "USW00024131",                 # Seattle Tacoma Intl Airport, WA
        "name": "Seattle – Sea-Tac",
        "lat": 47.448,
        "lon": -122.309,
    },
]

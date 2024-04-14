import requests
import csv
import os

def get_mcdonalds_in_paris(api_key):
    """Fetches all McDonald's locations in Paris using Google Places API."""
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    query = "McDonald's in Paris"
    
    params = {
        "query": query,
        "key": api_key,
    }

    locations = []

        while True:
        response = requests.get(url, params=params)
        data = response.json()

        if "results" in data:
            for place in data["results"]:
                locations.append({
                    "name": place.get("name"),
                    "address": place.get("formatted_address"),
                    "lat": place["geometry"]["location"].get("lat"),
                    "lng": place["geometry"]["location"].get("lng"),
                })

        # Check if there is another page of results
        if "next_page_token" in data:
            params["pagetoken"] = data["next_page_token"]
        else:
            break

    return locations
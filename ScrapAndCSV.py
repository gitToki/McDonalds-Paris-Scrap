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
                opening_hours = place.get("opening_hours")
                if opening_hours:
                    weekday_text = opening_hours.get("weekday_text", ["N/A"])
                else:
                    weekday_text = ["N/A"]
                locations.append({
                    "name": place.get("name"),
                    "address": place.get("formatted_address"),
                    "opening_hours": ", ".join(weekday_text)
                })

        # Check if there is another page of results
        if "next_page_token" in data:
            params["pagetoken"] = data["next_page_token"]
        else:
            break

    return locations


def save_to_csv(data, filename):
    """Saves location data to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "address", "opening_hours"])
        writer.writeheader()
        writer.writerows(data)


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
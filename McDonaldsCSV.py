from ScrapAndCSV import get_mcdonalds_in_paris, save_to_csv




api_key = os.getenv("GOOGLE_PLACES_API_KEY")

if not api_key:
    raise EnvironmentError("Missing API key. Please set GOOGLE_PLACES_API_KEY in your environment variables.")

print("Fetching McDonald's locations in Paris...")
locations = get_mcdonalds_in_paris(api_key)

print(f"Fetched {len(locations)} locations. Saving to CSV...")
save_to_csv(locations, "mcdonalds_paris.csv")

print("Data saved to 'mcdonalds_paris.csv'.")
# Import the necessary packages
from google_play_scraper import search, reviews, Sort
import csv

# configure the search
scrapped_data, _ = reviews(
    "id.co.bri.brimo",
    lang="id",
    country="id",
    sort=Sort.NEWEST,
    count=12000
)

# Save the data to a CSV file
with open("brimo_reviews.csv", mode="w", newline="", encoding="utf-8") as file:
    field_names = list(scrapped_data[0].keys())
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(scrapped_data)

print("Done")
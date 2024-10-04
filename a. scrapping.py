from google_play_scraper import search, reviews, Sort
import csv

scrapped_data, _ = reviews(
    "id.co.bri.brimo",
    lang="id",
    country="id",
    sort=Sort.NEWEST,
    count=12000
)

with open("brimo_reviews.csv", mode="w", newline="", encoding="utf-8") as file:
    field_names = list(scrapped_data[0].keys())
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(scrapped_data)

print("Done")
import pandas as pd
from pathlib import Path

# Project directory
DATA_DIR = Path(r"E:\Projects\Data Analytics\Retail Supply Chain\data")

# Input file
stores_file = DATA_DIR / "stores.csv"

# City-to-region mapping
city_regions = {
    "Delhi": 1,
    "Mumbai": 2,
    "Pune": 3,
    "Bangalore": 4
}

# Region lookup table
regions = pd.DataFrame({
    "region_id": [1, 2, 3, 4],
    "region_name": ["Delhi", "Mumbai", "Pune", "Bangalore"]
})

# Read stores
stores = pd.read_csv(stores_file)

# Validate required columns
required_columns = {"store_id", "city", "store_name"}
if not required_columns.issubset(stores.columns):
    raise ValueError(f"Missing columns: {required_columns - set(stores.columns)}")

# Normalize city names
stores["city"] = stores["city"].str.strip()

# Validate cities
unknown_cities = set(stores["city"].dropna().unique()) - set(city_regions)

if unknown_cities:
    raise ValueError(f"Unknown cities found: {unknown_cities}")

if stores["city"].isna().any():
    raise ValueError("Some stores have no city assigned.")

# Add region IDs and names
stores["region_id"] = stores["city"].map(city_regions)
stores["region_name"] = stores["city"]

# Save CSV files
regions.to_csv(DATA_DIR / "regions.csv", index=False)
stores.to_csv(DATA_DIR / "stores_with_regions.csv", index=False)

# Verify
print("Regions created successfully!")
print("\nRegions:")
print(regions.to_string(index=False))

print("\nStores per region:")
print(stores.groupby("region_name").size().to_string())

print("\nTotal stores:", len(stores))
print("\nFiles saved:")
print(DATA_DIR / "regions.csv")
print(DATA_DIR / "stores_with_regions.csv")
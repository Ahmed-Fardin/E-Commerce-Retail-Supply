import pandas as pd
from pathlib import Path
from collections import Counter

# Original CSV location
file_path = Path(
    r"E:\Projects\Data Analytics\Retail Supply Chain\data\stores.csv"
)

# Load data
df = pd.read_csv(file_path)

# Validate required columns
required = {"store_id", "city", "store_name"}
if not required.issubset(df.columns):
    raise ValueError(f"Missing columns: {required - set(df.columns)}")

if df["store_id"].duplicated().any():
    raise ValueError("Duplicate store IDs detected. File not changed.")

# Backup original file
backup_path = file_path.with_name("stores_backup.csv")
df.to_csv(backup_path, index=False)

# Make duplicate names unique
counts = Counter()
new_names = []

for name in df["store_name"].astype(str):
    counts[name] += 1
    occurrence = counts[name]

    if occurrence == 1:
        new_names.append(name)
    else:
        new_names.append(f"{name} Branch {occurrence}")

df["store_name"] = new_names

# Validate before saving
assert len(df) == 100, f"Expected 100 stores, found {len(df)}"
assert df["store_id"].is_unique
assert df["store_name"].is_unique
assert df["city"].notna().all()

# Overwrite original CSV
df.to_csv(file_path, index=False)

print("Store names fixed successfully!")
print(f"Total stores: {len(df)}")
print(f"Unique names: {df['store_name'].nunique()}")
print(f"Backup saved: {backup_path}")

print("\nUpdated store names:")
print(df[["store_id", "city", "store_name"]].to_string(index=False))

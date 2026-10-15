import pandas as pd
from pathlib import Path

ROOT = Path(r"E:\Projects\Data Analytics\Retail Supply Chain\data")

# Load files
products = pd.read_csv(ROOT / "products.csv")
categories = pd.read_csv(ROOT / "categories.csv")
stores = pd.read_csv(ROOT / "stores.csv")
suppliers = pd.read_csv(ROOT / "suppliers.csv")


# ---------------- CATEGORIES ----------------

category_names = [
    "Electronics",
    "Home & Kitchen",
    "Clothing",
    "Beauty & Personal Care",
    "Grocery",
    "Sports & Fitness",
    "Toys & Games",
    "Furniture",
    "Office Supplies",
    "Automotive",
    "Footwear",
    "Jewelry & Accessories",
    "Bags & Luggage",
    "Pet Supplies",
    "Baby Products",
    "Health & Wellness",
    "Books & Stationery",
    "Garden & Outdoor",
    "Tools & Hardware",
    "Mobile Accessories",
    "Computers & Accessories",
    "Appliances",
    "Food & Beverages",
    "Cleaning Supplies",
    "Lighting",
    "Travel Accessories",
    "Musical Instruments",
    "Crafts & Hobbies",
    "Seasonal Products",
    "Miscellaneous"
]

categories["category_name"] = categories["category_id"].map(
    lambda x: category_names[int(x) - 1]
)


# ---------------- SUPPLIERS ----------------

supplier_names = [
    "Reliance Industries",
    "Adani Enterprises",
    "Tata Consumer Products",
    "ITC Limited",
    "Hindustan Unilever",
    "Asian Paints",
    "Dabur India",
    "Godrej Industries",
    "Marico",
    "Britannia Industries",
    "Parle Products",
    "Amul",
    "Patanjali Foods",
    "Havells India",
    "Voltas",
    "Blue Star",
    "Bajaj Electricals",
    "Crompton Greaves",
    "Whirlpool India",
    "Bosch India"
]

suppliers["supplier_name"] = [
    supplier_names[i % len(supplier_names)]
    for i in range(len(suppliers))
]


# ---------------- STORES ----------------

store_locations = {
    "Mumbai": [
        "Andheri",
        "Bandra",
        "Powai",
        "Thane",
        "Borivali",
        "Lower Parel",
        "Goregaon",
        "Worli",
        "Malad",
        "Vashi"
    ],

    "Delhi": [
        "Connaught Place",
        "Saket",
        "Rohini",
        "Dwarka",
        "Vasant Kunj",
        "Karol Bagh",
        "Lajpat Nagar",
        "Greater Kailash",
        "Pitampura",
        "Rajouri Garden"
    ],

    "Pune": [
        "Koregaon Park",
        "Hinjawadi",
        "Viman Nagar",
        "Baner",
        "Kothrud",
        "Wakad",
        "Aundh",
        "Hadapsar",
        "Magarpatta",
        "Shivajinagar"
    ],

    "Bangalore": [
        "Indiranagar",
        "Whitefield",
        "Koramangala",
        "Jayanagar",
        "Electronic City",
        "HSR Layout",
        "Marathahalli",
        "Malleshwaram",
        "Hebbal",
        "Yelahanka"
    ]
}

store_names = []

for i, row in stores.iterrows():

    city = row["city"]
    locations = store_locations.get(city, ["Central"])

    location = locations[i % len(locations)]

    store_names.append(f"{city} {location}")

stores["store_name"] = store_names


# ---------------- PRODUCTS ----------------

brand_map = {
    1: ["Samsung", "Sony", "LG", "Philips", "Panasonic"],
    2: ["Tefal", "KitchenAid", "Prestige", "Pyrex", "Philips"],
    3: ["Nike", "Adidas", "Puma", "Levi's", "H&M"],
    4: ["L'Oreal", "Nivea", "Dove", "Olay", "Neutrogena"],
    5: ["Nestle", "Kellogg's", "Quaker", "Kraft", "Unilever"],
    6: ["Nike", "Adidas", "Puma", "Reebok", "Under Armour"],
    7: ["LEGO", "Hasbro", "Mattel", "Nerf", "Fisher-Price"],
    8: ["IKEA", "Ashley", "Urban Ladder", "Home Centre", "Durian"],
    9: ["Pilot", "Parker", "Staedtler", "Faber-Castell", "3M"],
    10: ["Bosch", "Castrol", "Shell", "Michelin", "3M"],
    11: ["Nike", "Adidas", "Puma", "Reebok", "Skechers"],
    12: ["Casio", "Fossil", "Titan", "Pandora", "Swarovski"],
    13: ["Samsonite", "Tumi", "SwissGear", "Herschel", "American Tourister"],
    14: ["Purina", "Pedigree", "Whiskas", "Royal Canin", "Hill's"],
    15: ["Pampers", "Huggies", "Chicco", "Philips Avent", "Fisher-Price"],
    16: ["Centrum", "GNC", "NOW", "Nature Made", "Optimum Nutrition"],
    17: ["Penguin", "Oxford", "Cambridge", "Moleskine", "Scholastic"],
    18: ["Gardena", "Fiskars", "Bosch", "Keter", "Black+Decker"],
    19: ["Bosch", "DeWalt", "Makita", "Stanley", "Black+Decker"],
    20: ["Anker", "Belkin", "Spigen", "Baseus", "UGREEN"],
    21: ["Logitech", "Dell", "HP", "Lenovo", "ASUS"],
    22: ["Philips", "LG", "Samsung", "Bosch", "Panasonic"],
    23: ["Coca-Cola", "Pepsi", "Nestle", "Red Bull", "Lipton"],
    24: ["Dettol", "Harpic", "Vim", "Mr Muscle", "Clorox"],
    25: ["Philips", "Osram", "Syska", "Havells", "Panasonic"],
    26: ["Samsonite", "Travelpro", "Tumi", "Cabeau", "Eagle Creek"],
    27: ["Yamaha", "Fender", "Gibson", "Roland", "Casio"],
    28: ["Crayola", "Faber-Castell", "Staedtler", "Winsor & Newton", "Daler-Rowney"],
    29: ["Hallmark", "Disney", "LEGO", "Party City", "Wilton"],
    30: ["3M", "IKEA", "OXO", "Rubbermaid", "Stanley"]
}

product_map = {
    1: ["Smart TV", "Wireless Headphones", "Bluetooth Speaker", "Smartwatch", "Digital Camera"],
    2: ["Cookware Set", "Frying Pan", "Dinner Set", "Kitchen Organizer", "Storage Container"],
    3: ["T-Shirt", "Polo Shirt", "Casual Shirt", "Denim Jeans", "Hoodie"],
    4: ["Face Wash", "Moisturizer", "Body Lotion", "Shampoo", "Sunscreen"],
    5: ["Rice", "Pasta", "Breakfast Cereal", "Biscuits", "Cooking Oil"],
    6: ["Running Shoes", "Yoga Mat", "Dumbbell Set", "Training Gloves", "Gym Bag"],
    7: ["Building Set", "Board Game", "Puzzle Set", "Action Figure", "Toy Car"],
    8: ["Office Chair", "Dining Table", "Bookshelf", "Computer Desk", "Storage Cabinet"],
    9: ["Notebook", "Pen Set", "Marker Set", "File Folder", "Desk Organizer"],
    10: ["Car Charger", "Engine Oil", "Floor Mat", "Tire Inflator", "Cleaning Kit"],
    11: ["Sneakers", "Formal Shoes", "Walking Shoes", "Sandals", "Training Shoes"],
    12: ["Wrist Watch", "Bracelet", "Necklace", "Ring", "Earrings"],
    13: ["Travel Backpack", "Laptop Bag", "Suitcase", "Duffel Bag", "Organizer"],
    14: ["Dog Food", "Cat Food", "Pet Bed", "Pet Bowl", "Pet Collar"],
    15: ["Baby Bottle", "Stroller", "Baby Blanket", "Baby Toy", "Care Set"],
    16: ["Protein Powder", "Vitamin Supplement", "Massage Roller", "Health Monitor", "First Aid Kit"],
    17: ["Novel", "Notebook", "Journal", "Planner", "Study Guide"],
    18: ["Garden Hose", "Plant Pot", "Garden Tool Set", "Watering Can", "Garden Gloves"],
    19: ["Drill Set", "Screwdriver Set", "Hammer", "Tool Kit", "Wrench Set"],
    20: ["USB-C Cable", "Phone Charger", "Power Bank", "Phone Case", "Wireless Charger"],
    21: ["Wireless Mouse", "Mechanical Keyboard", "Laptop Stand", "USB Hub", "Webcam"],
    22: ["Electric Kettle", "Microwave Oven", "Air Fryer", "Blender", "Toaster"],
    23: ["Fruit Juice", "Soft Drink", "Chocolate Bar", "Energy Drink", "Coffee"],
    24: ["Laundry Detergent", "Dishwashing Liquid", "Floor Cleaner", "Glass Cleaner", "Disinfectant"],
    25: ["LED Bulb", "Desk Lamp", "Ceiling Light", "Wall Light", "Floor Lamp"],
    26: ["Travel Pillow", "Luggage Scale", "Travel Adapter", "Packing Cube", "Toiletry Bag"],
    27: ["Acoustic Guitar", "Electric Guitar", "Keyboard", "Drum Set", "Microphone"],
    28: ["Painting Set", "Drawing Set", "Craft Kit", "Art Supplies", "Sketch Set"],
    29: ["Gift Box", "Holiday Decoration", "Party Decoration", "Wrapping Set", "Ornament"],
    30: ["Storage Box", "Utility Kit", "Organizer", "Reusable Container", "Household Set"]
}

brands = []
product_names = []

for _, row in products.iterrows():

    category_id = int(row["category_id"])
    product_id = int(row["product_id"])

    brand = brand_map[category_id][product_id % 5]
    product = product_map[category_id][(product_id // 5) % 5]

    # Unique but natural model name
    model = f"Model {product_id}"

    brands.append(brand)
    product_names.append(f"{brand} {product} {model}")

products["brand"] = brands
products["product_name"] = product_names


# ---------------- SAVE ----------------

categories.to_csv(ROOT / "categories.csv", index=False)
products.to_csv(ROOT / "products.csv", index=False)
stores.to_csv(ROOT / "stores.csv", index=False)
suppliers.to_csv(ROOT / "suppliers.csv", index=False)


# ---------------- CHECK ----------------

print("DONE")
print(f"Products: {len(products):,}")
print(f"Unique products: {products['product_name'].nunique():,}")
print(f"Categories: {len(categories):,}")
print(f"Stores: {len(stores):,}")
print(f"Suppliers: {len(suppliers):,}")

print("\nSample stores:")
print(stores[["store_id", "city", "store_name"]].head(15).to_string(index=False))
import json

def load_products():
    with open("products.json", "r") as file:
        return json.load(file)

def find_product(crop_name):
    products = load_products()
    for item in products:
        if item["crop"].lower() == crop_name.lower():
            return item
    return None

if __name__ == "__main__":
    crop_input = input("Enter crop name or ID (e.g., Tomato #124): ")
    result = find_product(crop_input)

    if result:
        print("\n🎯 Matched Product:")
        print(json.dumps(result, indent=4))
    else:
        print("❌ No matching product found.")

import requests
from bs4 import BeautifulSoup
import json

# Prompt the user for product URL page:
url = input("Paste and enter the link: ").strip()

# Mimic the broswer
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
           /537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

# Fetches the page
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find JSON data embedded in the HTML
    script_tags = soup.find_all("script", type="application/ld+json")

    # Extract JSON-LD structured data
    product_data = None
    for script in script_tags:
        try:
            json_data = json.loads(script.string)
            if json_data.get("@type") == "Product":
                product_data = json_data
                break
        except json.JSONDecodeError:
            continue

    # Extract relevant details if JSON was found
    if product_data:
        product_name = product_data.get("name", "N/A")
        upc = product_data.get("gtin13", "N/A")
        sku = product_data.get("sku", "N/A")
        ingredients = product_data.get("ingredients", "N/A")
        lifestyle_needs = product_data.get("suitableForDiet", "N/A")

        # If Category ID inside the category breadcrumb
        category_id = "N/A"
        if "category" in product_data:
            category_id = product_data["category"].split("/")[-1]

        # Print results
        print("\nExtracted Product Information:")
        print(f"Product Name: {product_name}")
        print(f"UPC: {upc}")
        print(f"SKU: {sku}")
        print(f"Ingredients: {ingredients}")
        print(f"Lifestyle & Dietary Needs: {lifestyle_needs}")
        print(f"Category ID: {category_id}")

    else:
        print("Product data not found on the page.")
else:
    print(f"Failed to retrieve page. HTTP Status Code: {response.status_code}")

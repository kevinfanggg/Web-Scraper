import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Get user input for the product URL
product_url = input("Enter Walmart Canada Product URL: ").strip()

# Open browser with existing session
driver = webdriver.Chrome()
driver.get(product_url)
time.sleep(6)

# Function to extract values dynamically based on heading text
def get_field_value(field_name):
    try:
        header = driver.find_element(By.XPATH, f"//h3[contains(text(), '{field_name}')]")
        value = header.find_element(By.XPATH, "./following-sibling::div/span").text
        return value
    except:
        return "Not Found"

# Function to get text of an element using XPath
def get_element_text(xpath):
    try:
        return driver.find_element(By.XPATH, xpath).text
    except:
        return "Not Found"

# Function to get attribute value of an element using XPath
def get_element_attribute(xpath, attribute):
    try:
        return driver.find_element(By.XPATH, xpath).get_attribute(attribute)
    except:
        return "Not Found"

# Scrape Title, Image URL, and Product Details using fixed XPaths
title = get_element_text('//*[@id="main-title"]')
image_url = get_element_attribute('//*[@id="maincontent"]/section/main/div[2]/div[2]/div/div[2]/div/div/section[1]/div[2]/div[1]/img', "src")
product_details = get_element_text('//*[@id="item-product-details"]/div[2]/div/div/div[2]/span')

# Scrape other fields dynamically
category_id = get_field_value("Category ID")
lifestyle_dietary = get_field_value("Lifestyle & Dietary Need")
sku = get_field_value("SKU")
upc = get_field_value("Universal Product Code (UPC check)")
ingredients = get_field_value("Ingredients")

# Data to save
data = {
    "Title": title,
    "Image URL": image_url,
    "Product Details": product_details,
    "Category ID": category_id,
    "Lifestyle & Dietary Need": lifestyle_dietary,
    "SKU": sku,
    "UPC": upc,
    "Ingredients": ingredients
}

# CSV file name
csv_filename = "walmart_product_data.csv"

# Write to CSV (append mode to save multiple entries)
file_exists = False
try:
    with open(csv_filename, "r"):
        file_exists = True
except FileNotFoundError:
    pass

with open(csv_filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())

    # Write headers only if the file is new
    if not file_exists:
        writer.writeheader()

    # Write data
    writer.writerow(data)

print(f"\n✅ Data saved to {csv_filename}")

🚧 **NOTE: THIS PROGRAM IS NOT YET FULLY FUNCTIONAL & FEATURES MAY BE INCOMPLETE** 🚧

This Python script uses Selenium to scrape product information from the Walmart website and saves it to a CSV file. It allows the user to repeatedly enter product URLs, extracts key product details, and appends them to a file under the name **"walmart_product_data.csv."** The script continues to prompt for new URLs until the user types STOP. For the main python program, download the **"WalmartScraper.py** file and follow the instructions. The **"TestVersions"** folder contains experimental/outdated versions of the webscraper. 


🔧 **INSTRUCTIONS**

1.) Paste the following text into Command Prompt and press Enter.

**"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222**

**chrome.exe --temote-debugging-port=9222**

2.) Once Google Chrome tab is opened, paste in desired page to scrape.

3.) Open Code IDE and run code (CTRL + ALT + N)



✅ Example Output
Each product entry in the CSV file will look like:

Title	         | Image URL	  | Product Details	 | Category ID | Lifestyle & Dietary Need	 | SKU	 | UPC	      | Ingredients
Example Product| https://...	| Description text | 123456	     | Gluten-Free	             | 12345 | 0123456789	| Sugar, Water, ...



🚨 Notes
- The script launches a new browser window for each product, which could be optimized by reusing a single session.
- Error handling is included for missing elements (returns "Not Found").
- You must have Selenium and ChromeDriver properly set up in your environment to run this script.

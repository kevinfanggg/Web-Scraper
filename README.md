🚧 **NOTE: THIS PROGRAM IS INCOMPLETE & FEATURES MAY NOT YET BE FULLY FUNCTIONAL** 🚧

This Python script uses Selenium to scrape product information from the Walmart website and saves it to a CSV file. It allows the user to repeatedly enter product URLs, extracts key product details, and appends them to a file under the name **"walmart_product_data.csv."** The script continues to prompt for new URLs until the user types STOP. For the main Python program, download the **"WalmartScraper.py"** file and follow the instructions. The **"TestVersions"** folder contains experimental/outdated versions of the webscraper.  


🔧 **INSTRUCTIONS**

1.) Download the **"WalmartScraper.py** file

2.) Run the **"WalmartScraper.py"** file, using your preferred IDE (VS Code, PyCharm, etc.). Some versions may not be compatible with this program.

3.) Open Code IDE and run (CTRL + ALT + N). The terminal should print "Enter Walmart Canada Product URL (or type STOP to stop scraping):"

4.) Paste your Walmart product link in the terminal input

5.) Wait until the terminal prints: "Data saved to filename.csv"

6.) Repeat or type STOP to end the loop<br>

Each product entry in the CSV file will look like:
![image](https://github.com/user-attachments/assets/df1db2d6-6870-452e-9d3e-b4489a1b5ba3)



🚨 **NOTES**
- The script launches a new browser window for each product, which could be optimized by reusing a single session.
- Error handling is included for missing elements (returns "Not Found").
- You must have Selenium and ChromeDriver properly set up in your environment to run this script.

# Web Automation Script using Selenium

This project provides a set of functions to automate interactions with the Intertop.kz website using Selenium WebDriver. The automation tasks include opening the website, logging in, searching for a product, and adding an item to the shopping cart.

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Selenium package
- Chrome WebDriver (compatible with your version of Chrome browser)

## Installation

1. **Install Selenium**

   ```bash
   pip install selenium

2. **Download Chrome WebDriver**

   Download the Chrome WebDriver from the official ChromeDriver site.
   Ensure the WebDriver executable is in your system's PATH or in the same directory as your script.

## Usage
Open Python file and execute functions:
- open_website(driver)
- login(driver, login, password)
- search_product(driver, search_term)
- add_item_to_cart(driver, item_link)

## Logging
The script uses Python's logging module to log important information and errors. The log messages include timestamps and log levels for better traceability.

## Error Handling
Each function includes a try-except block to catch and log any exceptions that occur during execution. The WebDriver is closed in the finally block to ensure it is properly terminated regardless of success or failure.

## Important Notes
Ensure that the WebDriver version matches your installed version of the Chrome browser.
Modify the XPaths in the script if there are any changes in the structure of the Intertop.kz website.

## Author
- Zhan Kazikhanov (Astana IT University)

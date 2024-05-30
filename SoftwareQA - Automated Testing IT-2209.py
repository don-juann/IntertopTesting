from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()

def open_website(driver):
    try:
        driver.get('https://intertop.kz')
        driver.maximize_window()
        logging.info("Website opened and window maximized")
        time.sleep(5)
    except Exception as e:
        logging.error(f"Error opening website: {e}")
    finally:
        driver.quit()
        logging.info("WebDriver closed")

def login(driver, log_in, pass_word):
    try:
        driver.get('https://intertop.kz')
        logging.info("Navigated to https://intertop.kz")
        
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="auth_block"]/div[1]'))
        )
        login_btn.click()
        logging.info("Login button clicked")

        login_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email_or_phone"]'))
        )
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')

        login_field.send_keys(log_in) 
        password_field.send_keys(pass_word)
        logging.info("Login credentials entered")

        submit_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[4]/button')
        submit_btn.click()
        logging.info("Submit button clicked")

        time.sleep(2)
    except Exception as e:
        logging.error(f"Error during login: {e}")
    finally:
        driver.quit()
        logging.info("WebDriver closed")

def search_product(driver, search_term):
    try:
        driver.get('https://intertop.kz')
        logging.info("Navigated to https://intertop.kz")

        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="v_search_input"]'))
        )
        logging.info("Search bar located")
        
        search_field.send_keys(search_term)
        logging.info(f"Search term '{search_term}' entered")
        
        search_field.send_keys(Keys.RETURN)
        logging.info("Search submitted")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div/div/div[1]'))
        )
        time.sleep(5)
        logging.info("Search results loaded")
    except Exception as e:
        logging.error(f"Error during search: {e}")
    finally:
        driver.quit()
        logging.info("WebDriver closed")

def add_item_to_cart(driver, product_link):
    try:
        driver.get(product_link)
        logging.info("Navigated to the product link")

        size_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="vs2__combobox"]/div[1]/input')) 
        )
        size_dropdown.click()
        logging.info("Size dropdown clicked")

        first_size_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="vs2__option-0"]'))  
        )
        first_size_option.click()
        logging.info("First size option selected")

        add_to_cart_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="basket_add_preview"]'))  
        )
        add_to_cart_btn.click()
        logging.info("Add to cart button clicked")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="header-middle"]/div[4]/div/div[2]/div[3]/div/a/div')) 
        )

        time.sleep(5)
        logging.info("Item added to cart successfully")
    except Exception as e:
        logging.error(f"Error adding item to cart: {e}")
    finally:
        driver.quit()
        logging.info("WebDriver closed")

#open_website(driver)
#login(driver, 'testuser@example.com', 'SecurePassword123')
#search_product(driver, 'adidas кеды')
#add_item_to_cart(driver, 'https://intertop.kz/ru-kz/product/sneakers-nike-8478905?tr_pr=search')

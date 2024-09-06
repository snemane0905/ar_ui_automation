import configparser
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def assert_response(expected_response, actual_response):
    """
    Assert the response with the expected response
    """
    global passed, failed, total
    print("---------Verifying the result---------")
    for key in expected_response.keys():
        total += 1
        try:
            assert expected_response[key] == actual_response[key]
            passed += 1
        except AssertionError:
            failed += 1

def read_config(config=None):
    """
    This method will read the configs required from a config file in parent directory if path is not provided
    """
    try:
        print("---------Reading config---------")
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"\033[91---------The config file does not exist in the path : '{config_file}'---------\033[0m")           
        config.read(config_file)      


    except:
        raise Exception("\033[91mUnexpected error occurred while reading config file\033[0m")

def accept_cookie(driver):
    """
    Accept the cookies shown in the popup
    """
    try:
        print("---------Accepting cookies---------")
        accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="ACCEPT"]')))
        accept_button.click()
    except Exception as e:
        raise Exception ("\033[91m---------Error accepting cookie---------\033[0m")

def allow_notification(driver):
    allow_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='ALLOW']"))) 
    # We can reject notification by 'Don\'t Allow' button
    allow_button.click()
         
try:
    total = 0
    passed = 0
    failed = 0
    # Read the config file to fetch the portal url and chrome driver path
    config = configparser.ConfigParser()
    read_config(config)

    portal_url = config.get('airalo','portal_url')
    chrome_driver_path = config.get('airalo', 'chrome_driver_path')
    
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

     
    # 1. Navigate to Airalo's website to check if the WebDriver is working
    driver.get(portal_url)
    driver.maximize_window()    
    
    # Accept cookied
    accept_cookie(driver)
 
    # Allow notification   
    allow_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='ALLOW']"))) 
    # We can reject notification by 'Don\'t Allow' button
    allow_button.click()
    
    # search for Japan and select the local option
    search_field = WebDriverWait(driver, 5).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search data packs for 200+ countries and regions']")))
    search_field.send_keys("Japan")
    
    japan_option = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Japan')]")))
    japan_option.click()
    
    # # # 3. Select an eSIM Package
    # # Wait for the packages to load and select the first one
    first_package = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][normalize-space()='BUY NOW'])[1]")))
    first_package.click()
  
    # Extract package details by xpath
    title_xpath = '//*[@id="__layout"]/div/span[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div[2]'
    coverage_xpath = '//*[@id="__layout"]/div/span[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div[2]/ul/li[1]/div/p[2]'
    data_xpath = '//*[@id="__layout"]/div/span[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div[2]/ul/li[2]/div/p[2]'
    validity_xpath = '//*[@id="__layout"]/div/span[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div[2]/ul/li[3]/div/p[2]'
    price_xpath = '//*[@id="__layout"]/div/span[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div[2]/ul/li[4]/div/p[2]'
    
    
    title = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, title_xpath)))
    coverage = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, coverage_xpath)))
    data = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, data_xpath)))
    validity = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, validity_xpath)))
    price = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, price_xpath)))
    
    output = {
        'title' : title.text,
        'Coverage' : coverage.text, 
        'data' : data.text,
        'validity' : validity.text,
        'price' : price.text
    }
        
    expected_response = {
        'title' : 'Moshi Moshi',
        'Coverage' : 'Japan',
        'data' : '1 GB',
        'validity' : '7 Days',
        'price' : '4.50 €'  
    }


    # 4. Verify Package Details
    assert_response(expected_response, output)

    # Print output
    print("Total : ", total)
    print('Passed : ', passed)
    print('Failed : ', failed)

    # driver.quit()

except Exception as e:
    print(f"\033[91An error occurred: {e}\033[0m")




   

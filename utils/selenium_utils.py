import json, time, os
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as driver_wait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumUtils:

    @staticmethod
    def get_webdriver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("window-size=1024,768")
        chrome_options.add_argument("--no-sandbox")

        # Initialize a new browser
        driver = webdriver.Chrome(executable_path='/root/chromedriver', chrome_options=chrome_options)
        driver.get('https://datastudio.google.com')
        print("INFO: Successfully create seleium webdriver.")  
        return driver

    @staticmethod
    def add_cookies(driver, cookies_json_path:str):
        with open(cookies_json_path) as json_file: cookies = json.load(json_file)
        for cookie in cookies: 
            driver.add_cookie(cookie)
        time.sleep(5)
        print("INFO: Successfully add cookies.")
        return driver
        
    @staticmethod
    def capture_report_screeen(driver):
        screenshot_name = os.getcwd() + "/temp_dashboard.jpg"
        try:
            expected_xpath = """//div[contains(text(),"Can't access report")]"""
            driver_wait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH,expected_xpath)),
                message="Can't access report - timeout"
            )
            driver.save_screenshot(screenshot_name)
            return screenshot_name, False
        except Exception as e: 
            if "datastudio.google.com" in driver.current_url:
                time.sleep(5)
                driver.save_screenshot(screenshot_name)
                return screenshot_name, True
    
    @staticmethod
    def teardown_webdriver(driver):
        driver.close()
        driver.quit()




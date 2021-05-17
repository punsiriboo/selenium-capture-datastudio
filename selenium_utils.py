import uuid, json, time
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait as driver_wait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumUtils:

    @staticmethod
    def get_webdriver(selenium_remote_driver_url):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1024,768")

        driver = webdriver.Remote(
            command_executor=selenium_remote_driver_url,
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options
        )
        print("INFO: Successfully create seleium webdriver.")
        return driver

    @staticmethod
    def add_cookies(driver, cookies_json_path):
        with open(cookies_json_path) as json_file: cookies = json.load(json_file)
        for cookie in cookies: driver.add_cookie(cookie)
        print("INFO: Successfully add cookies.")
        return driver
        
    @staticmethod
    def capture_report_screeen(driver):
        screenshot_name = f"{uuid.uuid1()}.jpg"
        try:
            expected_xpath = """//div[contains(text(),"Can't access report")]"""
            driver_wait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH,expected_xpath)),
                message="Can't access report - timeout"
            )
            return
        except Exception as e: 
            if "datastudio.google.com" in driver.current_url:
                time.sleep(5)
                driver.save_screenshot(screenshot_name)
                return screenshot_name
    
    @staticmethod
    def teardown_webdriver(driver):
        driver.close()
        driver.quit()




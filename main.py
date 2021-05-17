from flask import Flask
from selenium import webdriver
import os , json, time, datetime
from line_notify import LineNotify
from selen_utils import SeleniumUtils
import chromedriver_binary  # Adds chromedriver binary to path

app = Flask(__name__)

@app.route("/")
def handle_request(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    #region configuration
    with open("private/config.json") as json_data_file: config = json.load(json_data_file)
    ACCESS_TOKEN = config['notify_token']
    REPORT_URL = "https://datastudio.google.com/embed/reporting/{report_id}/page/{page_id}".format(
                report_id=config['report']['id'],
                page_id=config['report']['page']
            )
    SELENIUM_REMOTE_DRIVER_URL = config['selenium_remote_driver_url']
    COOKIES_JSON_PATH = config['cookies_json_path']
    #endregion
    selenium_utils = SeleniumUtils()
    driver = selenium_utils.get_webdriver(SELENIUM_REMOTE_DRIVER_URL)
    notify = LineNotify(ACCESS_TOKEN)
    driver.get(REPORT_URL)
    driver = selenium_utils.add_cookies(driver, COOKIES_JSON_PATH)
    time.sleep(5)
    driver.get(REPORT_URL)
    captured_image_path = selenium_utils.capture_report_screeen(driver)
    if captured_image_path is not None:
        data_date = datetime.datetime.now.strftime("%m/%d/%Y, %H:%M:%S")
        notify.send(
            f"Data Studio Dashboard/n As of {data_date}", 
            image_path=captured_image_path
        )
        selenium_utils.teardown_webdriver(driver)
    else:
        notify.send("Unable to capture report screen\n\n Please contact admin to refresh cookies or validate issue.")
        selenium_utils.teardown_webdriver(driver)
        
    return 'Successfully send line notify dashboard.'



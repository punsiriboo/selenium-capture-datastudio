from flask import Flask
import json, time
from line_notify import LineNotify
from utils import SeleniumUtils


app = Flask(__name__)

@app.route("/")
def handle_request():
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
    COOKIES_JSON_PATH = config['cookies_json_path']
    #endregion
    driver = SeleniumUtils.get_webdriver()
    notify = LineNotify(ACCESS_TOKEN)
    driver = SeleniumUtils.add_cookies(driver, COOKIES_JSON_PATH)
    driver.get(REPORT_URL)
    captured_image_path, captured_status = SeleniumUtils.capture_report_screeen(driver)
    if captured_status is not None:
        data_date = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(time.time()))
        notify.send(f"Dashboard as of {data_date}", image_path=captured_image_path)
        SeleniumUtils.teardown_webdriver(driver)
    else:
        notify.send("Unable to capture report screen\n\n Please contact admin to refresh cookies or validate issue.", image_path=captured_image_path)
        SeleniumUtils.teardown_webdriver(driver)
        
    return 'Successfully send line notify dashboard.'



import time, json
from config import CONFIG
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)
try:
    driver.implicitly_wait(3)

    # 11번가 Page로 이동
    driver.get(CONFIG.get("TargetUrl"))
    # 다음달로 이동 (5월)
    driver.find_element_by_css_selector("#divCalendar1 > div > button.c_product_btn.c_ticket_btn_next.month_next").click()
    # 달력 가져오기
    calendar = driver.find_element_by_css_selector("#divCalendar1")

    # disabled Attribute가 없는 항목만 가져오기
    elements = calendar.find_elements_by_xpath('//table/tbody/tr/td/button[not(@disabled)]')

    remain_dict = {}
    for el in elements:
        try:
            # set except case
            if any(int(el.text) == not_possible_day for not_possible_day in CONFIG.get("ExceptDays")):
                continue
            el.click()

            xpath = '// *[ @ id = "layBodyWrap"] / div / div / div[1] / div / div[2] / div[2] / dl / div / dd / i'
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            remain_sit = driver.find_element_by_xpath(xpath)

            if int(remain_sit.text) > 0:
                remain_dict[el.text] = remain_sit.text

            # For Debugging
            print(f"day:{el.text}, sit: {remain_sit.text}")

        except selenium.common.exceptions.StaleElementReferenceException as e:
            continue

    if len(remain_dict.keys()) > 0:
        requests.post(CONFIG["WebhookUrl"], json={"text": json.dumps(remain_dict)})
except Exception as e:
    print(str(e))
finally:
    driver.quit()


import time, json
import requests
import selenium
from selenium import webdriver

WEBHOOK_URL = ""

driver = webdriver.Chrome('chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(3)

# 11번가 Page로 이동
driver.get("https://ticket.11st.co.kr/Product/Detail?id=265070")
# 다음달로 이동 (5월)
driver.find_element_by_css_selector("#divCalendar1 > div > button.c_product_btn.c_ticket_btn_next.month_next").click()
# 달력 가져오기
calendar = driver.find_element_by_css_selector("#divCalendar1")

# disabled Attribute가 없는 항목만 가져오기
elements = calendar.find_elements_by_xpath('//table/tbody/tr/td/button[not(@disabled)]')

remain_dict = {}
for el in elements:
    try:
        el.click()
        remain_sit = driver.find_element_by_xpath('// *[ @ id = "layBodyWrap"] / div / div / div[1] / div / div[2] / div[2] / dl / div / dd / i')
        time.sleep(3)

        if int(remain_sit.text) > 0:
            remain_dict[el.text] = remain_sit.text
    except selenium.common.exceptions.StaleElementReferenceException as e:
        continue

requests.post(WEBHOOK_URL, json={"text": json.dumps(remain_dict)})

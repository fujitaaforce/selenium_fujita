from selenium import webdriver
import chromedriver_binary
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium_wait import element_has_text_value

driver = webdriver.Chrome()
driver.get('https://a-force.biz/index.aspx#!')

# chatbotの開始
open_chat_bot_buttom = driver.find_element_by_class_name("fa-comment")
open_chat_bot_buttom.click()

# frameの移動
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

# 質問の入力
input_text = driver.find_element_by_css_selector("input.form-control")
input_text.send_keys("今年の採用人数を教えてください。")

# input_textの要素にテキストが入力されているかの確認
wait = WebDriverWait(driver, 10)
element = wait.until(element_has_text_value((By.CSS_SELECTOR, "input.form-control")))

# 送信ボタンの押下
submit_buttom = driver.find_element_by_class_name("btn-primary")
time.sleep(0.1)
submit_buttom.click()

# answerの要素が発生し、取得するまで無限ループ
while True :
    try :
        answer = driver.find_element_by_css_selector("div div.row:nth-child(3)")
    except Exception as e :
        continue
    else :
        break

time.sleep(0.1)

# answer要素の出力
print(answer.text)

driver.close()
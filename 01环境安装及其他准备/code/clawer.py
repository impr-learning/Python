from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager.chrome import ChromeDriverManager
import time

# browser = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome()

browser.get('http://www.baidu.com/')
input = browser.find_element_by_id('kw')

# 第一次输入
time.sleep(3)
input.send_keys('黑洞')
time.sleep(3)
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

# 第二次输入
input.clear()
time.sleep(3)
input.send_keys('世界上最好的语言')
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

# time.sleep(20)
# browser.close()
# exit()

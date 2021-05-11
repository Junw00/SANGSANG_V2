import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import configparser

import urllib.parse as urlparse
from urllib.parse import urlencode, quote_plus
from urllib.parse import urljoin

import json

# json parse
with open('config.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

    URL = json_data["URL"]
    count = json_data["count"]

# count에 수를 string 에서 int로 변환
count_int = int(count)

# URL 구조 추출
url_full = urlparse.urlparse(URL)
url_path = url_full.path.replace('/onclass/video-call/', '0')
url_host = url_full.netloc

# 접속 URL 만들기
url_re = urlparse.urljoin(URL, '/onclass/sign-in')

params = {'roomid': url_path, 'x': '0'}

url_parts = list(urlparse.urlparse(url_re))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params)

url_parts[4] = urlencode(query)

#print(urlparse.urlunparse(url_parts))

#############################################

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("chrome://settings/content") # 크롬 설정 페이지 오픈
print('\nEnter 입력시 시작..')

driver.implicitly_wait(3)

x = str(input()) # 입력받은 값을 변수에 저장

remember = 0 # 몇번째 반복인지 기억하는 변수

print(count + "개 설정됨")

if x == '':
    while remember < count_int:  # index 변수가 count 수 보다 작은 동안 반복        

        driver.execute_script("window.open('" + urlparse.urlunparse(url_parts) + "','_blank')") # 새탭 오픈
                    
        driver.switch_to.window(driver.window_handles[-1]) # 탭 이동

        driver.implicitly_wait(3)
        driver.find_element_by_class_name('start-button-text').click() # 입장 버튼 클릭
        remember += 1

import json
from time import sleep
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_one():

    def setup(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.get('https://work.weixin.qq.com/')

    def test_one(self):
        #这里直接就可以定位到复用页面的元素
        #self.driver.find_element(By.XPATH, '//*//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        # self.driver.find_element(By.XPATH,'//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # sleep(6)
        # cookie = self.driver.get_cookies()
        # with open("cookie.txt", 'w') as f:
        #     json.dump(cookie, f)
        #     print('写入时的cookie：' + str(cookie))

        with open("cookie.txt", 'r') as f:
            # print("从文件中读cookie："+str(json.load(f)))
            cookies: List[Dict] = json.load(f)
            for cookie in cookies:
                if 'expiry' in cookie.keys():
                    cookie.pop('expiry')
                self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.XPATH, '//*//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        self.driver.find_element(By.ID, 'username').send_keys('qazse4')

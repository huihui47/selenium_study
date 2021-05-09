import pytest
from selenium import webdriver
from time import sleep, ctime
import os

options = webdriver.ChromeOptions()
# 这里是浏览器可执行文件的地址
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# 这里是浏览器驱动：chromedriver的下载地址
chrome_driver_binary = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
class TestCase():
    def setup_class(self):
        print("Start!!!")
    def teardown_class(self):
        print("ending!!!")
        driver.quit()
    def setup_method(self):
        # 这里是要测试的网页，打开网页
        driver.get("http://www.baidu.com")
    def teardown_method(self):
        sleep(3)

    def test_selenium(self):
        driver.find_element_by_id("kw").send_keys("Test search")
        # 这里找到id为"su"的控件，模拟鼠标执行点击
        driver.find_element_by_id("su").click()
    def test_selenium2(self):
        driver.find_element_by_id("kw").send_keys(" ")
        driver.find_element_by_id("su").click()
    def test_selenium3(self):
        driver.find_element_by_id("kw").send_keys("#")
        driver.find_element_by_id("su").click()
    def test_selenium4(self):
        driver.find_element_by_id("kw").send_keys("你好！")
        driver.find_element_by_id("su").click()
    def test_selenium5(self):
        driver.find_element_by_id("kw").send_keys("666")
        driver.find_element_by_id("su").click()
    def test_selenium6(self):
        driver.find_element_by_id("kw").send_keys("")
        driver.find_element_by_id("su").click()
    def test_selenium7(self):
        driver.find_element_by_id("kw").send_keys("No1")
        driver.find_element_by_id("su").click()
    def test_selenium8(self):
        driver.find_element_by_id("kw").send_keys("中111")
        driver.find_element_by_id("su").click()
    def test_selenium9(self):
        driver.find_element_by_link_text("新闻").click()
    def test_selenium10(self):
        #测试"换一换"
        driver.find_element_by_id("hotsearch-refresh-btn").click()
    def test_selenium11(self):
        driver.find_element_by_link_text("更多").click()
# coding=utf-8
# 不加这个会报错 non utf-8 coding
# 得到世界著名电影导演的名字
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
url = "https://www.douban.com/note/610393227/"
chrome_option = Options()
chrome_option.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
                          , options=chrome_option)
driver.get(url)
time.sleep(3)
driver.maximize_window()
# print(driver.page_source)


def find_element(the_str):
    # 这个是找字符串的，想找页面那种元素直接driver里面有
    while True:
        if driver.page_source.find(the_str) != -1:
            # 这个打印出来知道是不等于1的，所以需要用不等于-1的情况
            break
        else:
            time.sleep(1)
            continue


driver.find_element_by_xpath("//a[@class='ui-overlay-close']").click()
find_element("阅读全文")
driver.find_element_by_xpath("//a[@class='taboola-open-btn taboola-open']").click()
find_element("任景丰")
find_element("阿伯德拉马纳·希萨柯")
# print(driver.page_source)
name = r'<p>([\u4e00-\u9fa5]{1,})（1'
regex = re.compile(name)
director_list1 = regex.findall(driver.page_source,re.S)
name = r'<p>([\u4e00-\u9fa5]{1,}·[\u4e00-\u9fa5]{1,})（1'
# 这部分主要是匹配老外的名字，中间带·的
regex = re.compile(name)
director_list2 = regex.findall(driver.page_source,re.S)
name = r'<p>([\u4e00-\u9fa5]{1,}·[\u4e00-\u9fa5]{1,}·[\u4e00-\u9fa5]{1,})（1'
# 这部分主要是匹配老外的名字，中间带·的
regex = re.compile(name)
director_list3 = regex.findall(driver.page_source,re.S)
name = r'<p>([\u4e00-\u9fa5]{1,}·[\u4e00-\u9fa5]{1,}·[\u4e00-\u9fa5]{1,}·[\u4e00-\u9fa5]{1,})（1'
# 这部分主要是匹配老外的名字，中间带·的
regex = re.compile(name)
director_list4 = regex.findall(driver.page_source,re.S)
director_list = director_list1 + director_list2 + director_list3 + director_list4
print(director_list)
# 这个列表也不算长，打印出来之后直接复制粘贴就行了
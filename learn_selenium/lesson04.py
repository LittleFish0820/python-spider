"""selenium: 交互"""


import time
from selenium import webdriver


path = "chromedriver.exe"
browser = webdriver.Chrome(path)


url = "http://www.baidu.com"
# url = "https://www.google.com/"
browser.get(url)


time.sleep(2)


# 获取文本框的对象
input = browser.find_element_by_id('kw')
# 在文本框中输入keyword
input.send_keys("周杰伦")


time.sleep(2)


# 获取百度一下的按钮
button = browser.find_element_by_id("su")
# 点击按钮
button.click()


time.sleep(2)


# 滑到底部
js_button = "document.documentElement.scrollTop=100000"
browser.execute_script(js_button)


time.sleep(2)


# 获取下一页的按钮
next = browser.find_element_by_xpath("//a[@class='n']")
# 点击下一页的按钮
next.click()


time.sleep(2)


# 回到上一页
browser.back()


time.sleep(2)


browser.forward()


time.sleep(3)


# 退出
browser.quit()

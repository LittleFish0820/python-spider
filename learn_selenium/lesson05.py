"""selenium: Phantomjs (时代变了，仅作了解)"""


# 1. 无界面浏览器
# 2. 支持页面元素查找，js的执行等
# 3. 由于不进行css和gui渲染，运行效率要比真实的浏览器快
# UserWarning: Selenium support for PhantomJS has been deprecated,
# please use headless versions of Chrome or Firefox instead


from selenium import webdriver
import time


path = "phantomjs.exe"
browser = webdriver.PhantomJS(path)


url = "https://www.baidu.com"
browser.get(url)


browser.save_screenshot('baidu.png')


time.sleep(2)


input = browser.find_element_by_id('kw')
input.send_keys("昆凌")


time.sleep(3)


browser.save_screenshot("昆凌.png")


browser.quit()

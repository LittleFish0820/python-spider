"""selenium: 元素定位"""


from selenium import webdriver


path = "chromedriver.exe"
browser = webdriver.Chrome(path)


url = "https://www.baidu.com"
browser.get(url)


# 根据标签属性的属性值来获取对象
# button = browser.find_element_by_id('su')
# button = browser.find_element_by_name('wd')


# 根据xpath语句来获取对象
button = browser.find_elements_by_xpath("//input[@id='su']")
print(button)


# 根据标签的名字来获取对象
# button = browser.find_element_by_tag_name("input")


# 使用bs4的语法来获取对象
# button = browser.find_element_by_css_selector("#su")


# 填更多里面的直播，会报错。可能有懒加载机制
button = browser.find_element_by_link_text("新闻")
print(button)


browser.quit()

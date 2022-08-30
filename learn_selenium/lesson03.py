"""selenium: 元素信息"""


from selenium import webdriver


path = "chromedriver.exe"
browser = webdriver.Chrome(path)


url = "http://www.baidu.com"
browser.get(url)


input = browser.find_element_by_id("su")


# 获取标签属性的属性值
print(input.get_attribute('class'))


# 获取标签的名字
print(input.tag_name)


# 获取元素文本
print(input.text)


browser.quit()

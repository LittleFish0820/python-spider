"""selenium: 基本使用"""


# 操作谷歌浏览器驱动下载地址
# http://chromedriver.storage.googleapis.com/index.html
# 浏览器右上角 帮助 关于 查看 版本号信息
# 解压得到 .exe 文件


from selenium import webdriver


path = "chromedriver.exe"
browser = webdriver.Chrome(path)


url = "https://www.jd.com/"


browser.get(url)
content = browser.page_source
print(content)


# 不关闭会浪费资源，资源管理器监视搜chromedriver.exe
browser.quit()

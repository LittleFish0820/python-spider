import urllib.request
import os


if not os.path.exists("./lesson03"):
    os.mkdir("./lesson03")


# 下载网页
url_page = "http://www.baidu.com"
urllib.request.urlretrieve(url_page, "./lesson03/baidu.html")  # index.html


# 下载图片
url_img = "https://img1.baidu.com/it/u=2311613120,1101336108&fm=253&fmt=auto&app=138&f=PNG?w=500&h=209"
urllib.request.urlretrieve(url=url_img, filename="./lesson03/git.jpg")


# 下载视频
# 查看网页源代码，定位视频，想办法获取视频地址
url_vedio = "https://vd2.bdstatic.com/mda-khppqciad2idchj5/v1-cae/sc/mda-khppqciad2idchj5.mp4?v_from_s=hkapp-haokan-hbe&auth_key=1661083429-0-0-00efc4cb2412ba88ccda80284d885768&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=2029442044&vid=6714795470514738453&abtest=103525_2-103742_2-103579_1&klogid=2029442044"
urllib.request.urlretrieve(url_vedio, "./lesson03/git.mp4")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from random import randint
import pickle
# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang Facebook
driver.get('https://www.facebook.com')

# Tải cookie từ tệp
cookies = pickle.load(open("FB_cookies.pkl", "rb"))

# Thêm các cookie vào trình duyệt
for cookie in cookies:
    driver.add_cookie(cookie)

# Bây giờ bạn đã đăng nhập vào Facebook với cookie đã lưu

driver.refresh()

input('nhấn phím bất kỳ')


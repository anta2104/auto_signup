from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from captcha import *
import time
from test import *
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from random_email import *
import pyautogui
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trang web badoo.com/signup
driver.get("https://badoo.com/signup/?f=top")
time.sleep(2)

email_input = driver.find_element(By.ID, "login")
email_input.send_keys(randomWord(10) + "@example.com")
time.sleep(2)

password_input = driver.find_element(By.CLASS_NAME, "js-password")
password_input.send_keys("nhattan20026546")

# Bấm nút Sign Up
try:
    signup_button = driver.find_element(By.CLASS_NAME, "new-form__actions")
    signup_button.click()
except StaleElementReferenceException:
    # Thử tìm lại phần tử
    signup_button = driver.find_element(By.CLASS_NAME, "new-form__actions")
    signup_button.click()


time.sleep(2)
# Captcha
while True :
    time.sleep(2)
    captcha_element = driver.find_element(By.ID, "check_code_img")
    screenshot = captcha_element.screenshot_as_png
    with open('captcha.gif', 'wb') as f:
        f.write(screenshot)
    text = solve_captcha('captcha.gif')
    input_captcha = driver.find_element(By.NAME, "checkcode")
    input_captcha.send_keys(text)
    signup_button = driver.find_element(By.CLASS_NAME, "new-form__actions")
    signup_button.click()
    time.sleep(2)
    try:
        captcha_check_label = driver.find_element(By.ID, "captchaCheckLabel")
        continue  # Nếu tìm thấy phần tử, tiếp tục vòng lặp
    except NoSuchElementException:
        break  # Nếu không tìm thấy phần tử, thoát khỏi vòng lặp

time.sleep(8)


# Điền thông tin vào các trường Tên
name_input = driver.find_element(By.ID, "first_name")
name_input.send_keys("John Doe")
time.sleep(2)


# Điền thông tin vào trường Ngày
wait = WebDriverWait(driver, 10)
select_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-signup-day')))

# Click vào trường chọn ngày để mở danh sách các lựa chọn
select_field.click()
time.sleep(1)

option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.option[data-value="2"]')))
option.click()

time.sleep(2)

########## Điền thông tin vào trường tháng ##############
month_element = driver.find_element(By.CSS_SELECTOR, '.js-signup-month') # tìm month field element
month_element.click() # Click vào phần tử select để mở trường select
time.sleep(1)
div_element1 = driver.find_element(By.CSS_SELECTOR, '.js-signup-month')
div_element2 = div_element1.find_element(By.CLASS_NAME, 'dropdown--select')
div_element3 = div_element2.find_element(By.CLASS_NAME, 'dropdown__options')
div_element4 = div_element3.find_element(By.CLASS_NAME, 'scroll--dynamic')
div_element5 = div_element4.find_element(By.CLASS_NAME, 'scroll__inner')
ul_element = div_element5.find_element(By.CLASS_NAME, 'options')
month_input = ul_element.find_element(By.CSS_SELECTOR, 'li[data-qa-value="3"]')
month_input.click()
time.sleep(2)


# Điền thông tin vào trường Năm
wait = WebDriverWait(driver, 10)
select_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-signup-year')))

# Click vào trường chọn ngày để mở danh sách các lựa chọn
select_field.click()
time.sleep(1)

option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.option[data-value="2002"]')))
option.click()

time.sleep(2)

# Điền vào trường thành phố
wait = WebDriverWait(driver, 10)
select_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-location-list')))

# Click vào trường chọn ngày để mở danh sách các lựa chọn
select_field.click()
time.sleep(1)

option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.option[data-value="15_2950_243"]')))
option.click()


time.sleep(1)


# Điền vào trường thành giới tính
gender_input = driver.find_element(By.ID, "male")
gender_input.click()
time.sleep(1)

# Click ô tạo tiếp tục
create = driver.find_element(By.NAME, "create_profile")
create.click()
time.sleep(10)

# tìm đối tượng submit và nhấn nút để tải lên
submit_button = driver.find_element(By.CLASS_NAME, "file-upload__hint")
submit_button.click()
time.sleep(2)

# điền đường dẫn tới tệp tin
pyautogui.write("/home/nhattan/Desktop/Task2/test.jpg")
# ấn phím Enter
pyautogui.press('enter')
time.sleep(8)

# create profile 
create_profile = driver.find_element(By.CSS_SELECTOR, ".react-button.react-button--filled.react-button--md.react-button--color-primary.react-button--narrow")
create_profile.click()
time.sleep(120)
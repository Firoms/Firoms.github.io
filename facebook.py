from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = 'https://ko-kr.facebook.com/'
cOptions = Options()
cOptions.add_argument("--disable-infobars")
cOptions.add_argument("--disable-extensions")
cOptions.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications" : 1
})


id = ''
pw = ''

driver = webdriver.Chrome(chrome_options= cOptions, executable_path = 'C:\\Users\\Coding Lab\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.implicitly_wait(3)
driver.get(URL)
driver.implicitly_wait(3)

driver.find_element_by_name('email').send_keys(id)
driver.find_element_by_name('pass').send_keys(pw)
driver.find_element_by_class_name('login_form_login_button').click()
# driver.find_element_by_xpath('//*[@id="u_0_2"]').click() >>가끔 변함
driver.find_element_by_name('xhpc_message').click()
driver.implicitly_wait(3)
article = '안녕하세요. 반갑습니다.'
driver.find_element_by_class_name('_5yk2').send_keys(article)
driver.find_element_by_class_name('_1mf7').click()
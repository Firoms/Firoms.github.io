from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://reading.gglec.go.kr/r/reading/member/loginForm.jsp"


id = ""
pw = ""

driver = webdriver.Chrome(
    executable_path="E:\\파이썬\\chromedriver_win32\\chromedriver.exe"
)

driver.implicitly_wait(3)
driver.get(URL)
driver.implicitly_wait(3)

driver.find_element_by_name("s_id").send_keys(id)
driver.find_element_by_name("s_pwd").send_keys(pw)
driver.find_element_by_name("s_login").click()
driver.find_element_by_class_name("changeLater").click()

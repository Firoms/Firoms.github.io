"""
selenium을 사용하려면 라이브러리를 install 해줘야한다.
또한, chrome web driver는 자신의 chrome 버전에 맞는 것을 사용해야한다는 것을 꼭 기억하자.
"""

# 독서교육종합시스템
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-fullscreen")

URL = "https://reading.gglec.go.kr/r/newReading/main/main.jsp"

id = input("id를 입력하세요: ")
pw = input("pw를 입력하세요: ")
driver = webdriver.Chrome(
    executable_path="D:\\Coding\\Firoms_Note\\chromedriver.exe", chrome_options=options
)

driver.implicitly_wait(3)
driver.get(URL)
driver.implicitly_wait(3)
driver.find_element_by_id("headerLoginBtn").click()
driver.find_element_by_name("s_id").send_keys(id)
driver.find_element_by_name("s_pwd").send_keys(pw)
driver.find_element_by_id("s_login").click()
driver.find_element_by_class_name("changeLater").click()


# 컴시간 알리미
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-fullscreen")
URL = "http://112.186.146.81:4082/st"

school = "동탄고등학교"
driver = webdriver.Chrome(
    executable_path="D:\\Coding\\Firoms_Note\\chromedriver.exe", options=options
)
driver.implicitly_wait(3)
driver.get(URL)
driver.implicitly_wait(3)
driver.find_element_by_id("sc").send_keys(school)
driver.find_elements_by_tag_name("input")[1].click()
driver.find_element_by_link_text("동탄고등학교").click()
driver.find_element_by_id("ba").click()
driver.find_elements_by_tag_name("option")[33].click()
driver.find_element_by_id("ba").click()

from selenium import webdriver	# 전에 pip install selenium 했던 것을 이용하겠다는 의미
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--start-fullscreen')	#옵션 추가(전체화면으로 시작함)

URL = "https://reading.gglec.go.kr/r/newReading/main/main.jsp" 
# 프로그램을 시작할때 불러올 URL
id = 'edison0528'
pw = 'angel00!'
driver = webdriver.Chrome(
    executable_path="D:\\Coding\\Firoms_Note\\chromedriver.exe", options=options
)
# Chrome Web driver 객체 생성, Chrome Web Driver을 이용함

driver.implicitly_wait(3)	# 오류 방지를 위해 3초 지연
driver.get(URL)	# 아까 작성한 URL을 불러옴
driver.implicitly_wait(3)
driver.find_element_by_id("headerLoginBtn").click()
driver.find_element_by_name("s_id").send_keys(id)
driver.find_element_by_name("s_pwd").send_keys(pw)
driver.find_element_by_id("s_login").click()
driver.find_element_by_class_name("changeLater").click()

'''
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--start-fullscreen')
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
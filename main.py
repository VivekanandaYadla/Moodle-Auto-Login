from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://moodle.iitd.ac.in/login/index.php')

driver.find_element_by_id("username").send_keys('ph1200736')
driver.find_element_by_id("password").send_keys('776e9567')

quiz=driver.find_element_by_id("login").text[51:].split()
driver.find_element_by_id("valuepkg3").send_keys(Keys.BACKSPACE)
if (quiz[1]=='first'):
	driver.find_element_by_id("valuepkg3").send_keys(quiz[3])
elif (quiz[1]=='second'):
	driver.find_element_by_id("valuepkg3").send_keys(quiz[5])
elif (quiz[0]=='add'):
	driver.find_element_by_id("valuepkg3").send_keys(str(int(quiz[1])+int(quiz[3])))
elif (quiz[0]=='subtract'):
	driver.find_element_by_id("valuepkg3").send_keys(str(int(quiz[1])-int(quiz[3])))

driver.find_element_by_id("loginbtn").click()
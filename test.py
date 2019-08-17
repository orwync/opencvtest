from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Sonail\\Downloads\\chromedriver.exe')

driver.get('http://demo.automationtesting.in/Register.html')

print(driver.title)

driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()

time.sleep(5)

driver.close()
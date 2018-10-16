from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://guri.unipampa.edu.br/ptl/sistema/showLogin")
self.assertTrue(True)
driver.close()
elem = driver.find_element_by_name("login")
elem.clear()
elem.send_keys("Seu login aqui")
time.sleep(1)
elem = driver.find_element_by_name("senha")
elem.clear()
elem.send_keys("Sua senha aqui")
elem = driver.find_element_by_id("entrar").click()
time.sleep(1)
driver.get("https://guri.unipampa.edu.br/bib/biblioteca/consultarSituacao/")
driver.find_element_by_id("cbAllEmp").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@title="Renovar"]').click()
self.assertTrue(True)
driver.close()
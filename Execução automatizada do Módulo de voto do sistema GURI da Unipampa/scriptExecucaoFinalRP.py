#!/usr/bin/python 
 
import threading
import time
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def executa(tipoUsuario):
	if tipoUsuario == "Moderador":
		driver = webdriver.Chrome()
		driver.get("http://localhost/sistema/sistemaVoto/")
		driver.set_window_size(808, 886)
		time.sleep(5)
		driver.find_element_by_xpath("//*[@id='div_login']/input[1]").send_keys("renaro")
		driver.find_element_by_id('login').click()
		#time.sleep(10)
		driver.get("http://localhost/sistema/sistemaVoto/reunioes")
		time.sleep(5)
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/table/tbody/tr[2]/td[9]/input').click()
		time.sleep(10)
		driver.find_element_by_xpath('//*[@id="vtab1"]/div[3]/form/div[3]/button').click()
		time.sleep(10)
		driver.get("http://localhost/sistema/sistemaVoto/votacao/esperamod")
		time.sleep(1)
		driver.get("http://localhost/sistema/sistemaVoto/votacao/esperamod")
		time.sleep(1)
		driver.get("http://localhost/sistema/sistemaVoto/votacao/esperamod")
		time.sleep(1)
		driver.get("http://localhost/sistema/sistemaVoto/votacao/esperamod")
		time.sleep(1)
		driver.get("http://localhost/sistema/sistemaVoto/votacao/esperamod")
		time.sleep(1)
		driver.get("http://localhost/sistema/sistemaVoto/votacao/esperamod")
		content = driver.find_element_by_class_name('btn btn-success').click()
		time.sleep(10)
		driver.close()
		
	else:
		driver = webdriver.Chrome()
		driver.get("http://localhost/sistema/sistemaVoto/")	
		driver.set_window_size(808, 886)
		time.sleep(10)
		driver.find_element_by_xpath("//*[@id='div_login']/input[1]").send_keys("rafael")
		driver.find_element_by_id('login').click()
		time.sleep(3)
		driver.get("http://localhost/sistema/sistemaVoto/reunioes")	
		time.sleep(3)
		driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/table/tbody/tr/td[9]/input").click()
		time.sleep(10)
		alert = driver.switch_to_alert()
		alert.accept()
		time.sleep(2)
		driver.find_element_by_xpath("//input[@value='Abstenção']").click()
		time.sleep(2)
		driver.find_element_by_id('bt_votar').click()
		time.sleep(2)
		alert = driver.switch_to_alert()
		alert.accept()
		time.sleep(10)



		driver.close()
		


t = threading.Thread(target=executa,args=("Moderador",))
t.start()

b = threading.Thread(target=executa,args=("mod",))
b.start()

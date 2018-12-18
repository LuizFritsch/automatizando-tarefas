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
		driver.get("http://localhost/sistema/sistemaVoto/login")
		driver.set_window_size(808, 443)
		time.sleep(8)

	else:
		#Tem que ver se ele reseta tudo
		driver = webdriver.Chrome()
		driver.get("http://localhost/sistema/sistemaVoto/login")	
		driver.set_window_size(808, 886)
		time.sleep(8)

t = threading.Thread(target=executa,args=("Moderador",))
t.start()

b = threading.Thread(target=executa,args=("mod",))
b.start()
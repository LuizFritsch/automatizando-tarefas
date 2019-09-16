from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import socket
import csv
import numpy as np

message_text='teste' #this is the message you wanna spread
mobile_no_list=[]

#import numbers from a csv like example on github.com/luizfritsch
def import_numbers(file_name):
    with open(file_name+'.csv', newline='') as csvfile:
        data = np.array(list(csv.reader(csvfile)))
    return(data[:,2])

mobile_no_list = import_numbers('nr12')

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(10) #wait some time to you scan the qr code

def send_whatsapp_msg(phone_no,text):
    if is_connected:
        try:
            driver.get("https://api.whatsapp.com/send?phone="+str(phone_no)+"&text="+text+"")
            driver.find_element_by_xpath('//*[@id="action-button"]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="content"]/div/div/div/a').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
            sleep(1)
            alert = driver.switch_to_alert()
            alert.accept()    
        except Exception as e:
            print ("Erro no Nmr" + phone_no +"!")
        
for mobile_no in mobile_no_list:
    try:
        if int(mobile_no):
            send_whatsapp_msg(mobile_no,message_text)
    except Exception as e:
        sleep(10)
        is_connected()

driver.quit()
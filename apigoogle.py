from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import datetime

url1 = "https://www.farmaconde.com.br/vitacon-cabelos-e-unhas-60-capsulas"
url2 = 'https://www.farmaconde.com.br/protetor-solar-corporal-anthelios-xl-protect-fps70-200ml-la-roche-posay'


# ceps  das lojas  10 -59  
lista=["11690-141","11690-075","12230-030","12230-011","12210-090","12210-970","12215-270","12215-140","12248-513","12248-514","09750-300","09726-412","12327-705","12327-701","11390-150","11380-510","12460-000","12460-000","12710-210","12705-530"]




cep1 = lista[0]
cep2 = lista[1]

nomeArquivo =  datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.jpg')
def loja():
    driver = webdriver.Chrome()
    driver.get(url1)
    driver.fullscreen_window()
    start = time.time()
    driver.find_element(By.XPATH, '//*[@id="btn-cookie-allow"]/span').click()
    driver.find_element(By.XPATH, '//*[@id="cep"]').send_keys(cep1)
    driver.find_element(By.XPATH,'//*[@id="getrate"]/span').click()
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,  '//*[@id="shippings"]/table/tbody/tr[1]/td[2]')
    driver.save_screenshot(datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.jpg'))
    
    end = time.time()
    print(end - start)

    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 't') 

    driver.get(url1)
    driver.fullscreen_window()

    time.sleep(2)
    start = time.time()
    driver.find_element(By.XPATH, '//*[@id="cep"]').send_keys(cep2)
    driver.find_element(By.XPATH,'//*[@id="getrate"]/span').click()
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,  '//*[@id="shippings"]/table/tbody/tr[1]/td[2]')
    driver.save_screenshot(datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.jpg'))
    end = time.time()
    print(end - start)


    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 't') 

    driver.get(url2)
    driver.fullscreen_window()

    time.sleep(2)
    start = time.time()
    driver.find_element(By.XPATH, '//*[@id="cep"]').send_keys(cep2)
    driver.find_element(By.XPATH,'//*[@id="getrate"]/span').click()
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,  '//*[@id="shippings"]/table/tbody/tr[1]/td[2]')
    driver.save_screenshot(datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.jpg'))
    end = time.time()
    print(end - start)


    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 't') 

    driver.get(url2)
    driver.fullscreen_window()

    time.sleep(2)
    start = time.time()
    driver.find_element(By.XPATH, '//*[@id="cep"]').send_keys(cep1)
    driver.find_element(By.XPATH,'//*[@id="getrate"]/span').click()
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,  '//*[@id="shippings"]/table/tbody/tr[1]/td[2]')
    driver.save_screenshot(datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.jpg'))
    end = time.time()
    print(end - start)

    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 't') 
    driver.get(url1)
    driver.fullscreen_window()


    driver.find_element(By.XPATH, '//*[@id="product-addtocart-button"]').click()
    driver.implicitly_wait(30)
    driver.get(url2)
    driver.fullscreen_window()
    driver.find_element(By.XPATH, '//*[@id="product-addtocart-button"]').click()
    driver.implicitly_wait(30)
    
    
    driver.get("https://www.farmaconde.com.br/checkout/cart/")
    driver.refresh()
    driver.fullscreen_window()
    driver.find_element(By.NAME, "postcode").send_keys(cep1)
    driver.implicitly_wait(30)
    
    time.sleep(5)
    driver.save_screenshot(datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.jpg'))
    
    
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 't') 
    driver.get("https://www.farmaconde.com.br/checkout/cart/")
    driver.refresh()
    driver.fullscreen_window()
    driver.find_element(By.NAME, "postcode").send_keys(cep2)
    driver.implicitly_wait(30)
    time.sleep(5)
    driver.save_screenshot(datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.jpg'))
    driver.quit()


loja()
cep1 = lista[2]
cep2 = lista[3]
loja()


cep1 =lista[4]
cep2 = lista[5]
loja()


cep1 =lista[6]
cep2 = lista[7]
loja()


cep1 =lista[8]
cep2 =lista[9]
loja()


cep1 =lista[10]
cep2 = lista[11]
loja()


cep1 =lista[12]
cep2 = lista[13]
loja()


cep1 =lista[14]
cep2 = lista[15]
loja()


cep1 =lista[16]
cep2 = lista[17]
loja()


cep1 =lista[18]
cep2 = lista[19]
loja()



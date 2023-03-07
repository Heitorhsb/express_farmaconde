from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import sys
import time
from selenium.webdriver.chrome.service import Service as ChromeService
import json
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=3')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
#options.add_argument('--headless')
sys.stdout.write("\033[F") #back to previous line
sys.stdout.write("\033[K") #clear line

with open('lojas.json', 'r', encoding='utf8') as f:
    json_str = f.read()
    dicionario = json.loads(json_str, )
    loja = dicionario['loja']
    cep = dicionario['cep']
    
for l , i  in zip(loja, cep):
    try:
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.farmaconde.com.br/extrato-de-propolis-conlife-20ml')
        driver.fullscreen_window()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cep"]')))
        print(driver.find_element(By.XPATH, '//*[@id="cep"]').text)
        driver.find_element(By.XPATH, '//*[@id="cep"]').send_keys(i)
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="getrate"]/span').click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, 'shippings'))).is_enabled()
        loja = driver.find_element(By.ID,'shippings')
        #driver.find_element(By.XPATH,  '//*[@id="shippings"]/table/tbody/tr[1]/td[2]').is_enabled()
        #driver.save_screenshot('i+'.png') 
        #print('{} , {} frete cotando!'.format(l, i))
        
        if "Express" not in loja.text:
            print('Express DESABILIDADO PARA {}, {}'.format(l, i))
        else:
            print('Express HABILIDADO PARA {}, {}'.format(l, i))
    except:
        print('{}, {} frete não cotado!'.format(l, i))
        continue
    
    
    

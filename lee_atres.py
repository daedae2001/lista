import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
x = datetime.datetime.now()
fecha = "%s/%s/%s" % (x.day, x.month, x.year)
#import csv
#from bs4 import BeautifulSoup

# la version del driver debe coincidir con la version de chrome si no falla https://sites.google.com/a/chromium.org/chromedriver/downloads/version-selection
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.atresplayer.com/programacion/")
time.sleep(2)

d0 = driver.find_element_by_xpath(
    '/html/body/sibbo-cmp-layout/div/div[3]/div[4]/div[1]/a[1]')
d0.click()
time.sleep(1)
d1 = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[1]/main/div/div[3]/div[2]/div[1]/div/div[3]/div[18]/div/div')

d1.click()
#mi_pass = driver.find_element_by_xpath('//input[@placeholder="Contraseña"]')
#ingreso =()

""" driver.find_element_by_xpath('//input[@value="Ingresar"]')
mi_mail.send_keys('daedae2001@gmail.com')
mi_pass.send_keys('dae1357924680')
ingreso.click()
time.sleep(15)
"""
time.sleep(1)
d2 = driver.find_element_by_xpath(
    "/html/body/div[2]/div/div[1]/main/div/div[4]/a[2]/div/div")
d2.click()
time.sleep(1)
d3 = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[1]/div/div/ul/li[1]/button')
d3.click()
print(driver.current_url)
# print(driver.page_source)
print(driver.application_cache)
print(driver.capabilities)
print(driver.session_id)
print(driver.service)

tabla = '/html/body/div[2]/div/div[1]/div/div/ul/li[1]/button'


def recorre_especialidad(txt_especialidad, espera):
    try:
        mi_caja_especialidad = driver.find_element_by_xpath(
            '//*[@id="select2-slEspecialidades-container"]')
        mi_caja_especialidad.click()
        mi_caja_imput = driver.find_element_by_xpath(
            '/html/body/span/span/span[1]/input')
        mi_caja_imput.send_keys(txt_especialidad)
        mi_caja_imput.send_keys(Keys.ENTER)
        time.sleep(3)
        # print(driver.page_source)
        mi_dd_lista = driver.find_element_by_xpath(
            '//*[@id="select2-slEspecialidades-results"]/li[1]/ul/li[1]')
        mi_dd_lista.click()
        boton = driver.find_element_by_xpath('//button[@name="action"]')
        boton.click()
        time.sleep(espera)
        #print('a cargar')
        #element_present = EC.visibility_of_element_located((By.xpath, '//*[@id="tableTurnos"]/tbody'))
        #print (element_present.locator )
        #WebDriverWait(driver, 200).until(element_present)
        tb_tabla = driver.find_element_by_xpath('//*[@id="tableTurnos"]/tbody')
        tabla = tb_tabla.get_attribute('innerHTML')
        return tabla
    except:
        #        print ("error al cargar: " +txt_especialidad)
        return txt_especialidad


tabla = ''
tabla = tabla+recorre_especialidad('Cardiologia', 25)
tabla = tabla+recorre_especialidad('Pediatria', 25)
tabla = tabla+recorre_especialidad('Ginecologia', 25)
tabla = tabla+recorre_especialidad('Dermatologia', 25)
tabla = tabla+recorre_especialidad('Clinica medica', 25)
# tabla=tabla+recorre_especialidad('Traumatologia', 150) no da turnos web
tabla = tabla+recorre_especialidad('Endocrino', 25)
tabla = tabla+recorre_especialidad('Gastroenterologia', 25)
tabla = tabla+recorre_especialidad('O.r.l.', 25)


driver.close()
